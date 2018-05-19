#（1）首先将模型完全转换成对数计算，根据高斯密度函数公式分别计算k个组成高斯模型的log值，即logP(x|z)的值
def _estimate_log_gaussian_prob(X, means, precisions_chol, covariance_type):
# 计算精度矩阵的1/2次方log_det（代码精度矩阵是通过cholesky获取）
    log_det = _compute_log_det_cholesky(precisions_chol, covariance_type, n_features)
# 对应上面四种协方差类型，分别计算精度矩阵与（x-u)相乘那部分log_prob
    if covariance_type == 'full':
        log_prob = np.empty((n_samples, n_components))
        for k, (mu, prec_chol) in enumerate(zip(means, precisions_chol)):
            y = np.dot(X, prec_chol) - np.dot(mu, prec_chol)
            log_prob[:, k] = np.sum(np.square(y), axis=1)
    elif covariance_type == 'tied':
        log_prob = np.empty((n_samples, n_components))
        for k, mu in enumerate(means):
            y = np.dot(X, precisions_chol) - np.dot(mu, precisions_chol)
            log_prob[:, k] = np.sum(np.square(y), axis=1)
    elif covariance_type == 'diag':
        precisions = precisions_chol ** 2
        log_prob = (np.sum((means ** 2 * precisions), 1) -
                    2. * np.dot(X, (means * precisions).T) +
                    np.dot(X ** 2, precisions.T))
    elif covariance_type == 'spherical':
        precisions = precisions_chol ** 2
        log_prob = (np.sum(means ** 2, 1) * precisions -
                    2 * np.dot(X, means.T * precisions) +
                    np.outer(row_norms(X, squared=True), precisions))
	# 最后计算出logP(x|z)的值
	return -.5 * (n_features * np.log(2 * np.pi) + log_prob) + log_det   

#（2）P(x|z)*P(z)计算每个模型的概率分布P(x,z),求对数则就是相加了
def _estimate_weighted_log_prob(self, X):
	return self._estimate_log_prob(X) + self._estimate_log_weights()

#（3）最后开始计算每个模型的后验概率logP(z|x)，即Q函数
def _estimate_log_prob_resp(self, X):
	weighted_log_prob = self._estimate_weighted_log_prob(X)
	#计算P(X)
	log_prob_norm = logsumexp(weighted_log_prob, axis=1)
	with np.errstate(under='ignore'):
		# 忽略下溢,计算每个高斯模型的后验概率，即占比，对数则相减
		log_resp = weighted_log_prob - log_prob_norm[:, np.newaxis]
    return log_prob_norm, log_resp
#(4)调用以上函数
#返回所有样本的概率均值，及每个高斯分布的Q值
def _e_step(self, X):
	log_prob_norm, log_resp = self._estimate_log_prob_resp(X)
    return np.mean(log_prob_norm), log_resp
	
	
	
#2.对应M step
def _m_step(self, X, log_resp):
	#根据上面获得的每个高斯模型的Q值(log_resp)。重新估算均值self.means_，协方差self.covariances_，当前符合各高斯模型的样本数目self.weights_（函数名起的像权重，实际指的是数目）
	n_samples, _ = X.shape
	self.weights_, self.means_, self.covariances_ = (_estimate_gaussian_parameters(X, np.exp(log_resp), self.reg_covar,self.covariance_type))
	#更新当前各高斯模型的先验概率，即P(Z)
	self.weights_ /= n_samples
	#根据cholesky分解计算精度矩阵
	self.precisions_cholesky_ = _compute_precision_cholesky(self.covariances_, self.covariance_type)
	
#然后重复以上过程，就完成了EM算法的实现啦。