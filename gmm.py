#��1�����Ƚ�ģ����ȫת���ɶ������㣬���ݸ�˹�ܶȺ�����ʽ�ֱ����k����ɸ�˹ģ�͵�logֵ����logP(x|z)��ֵ
def _estimate_log_gaussian_prob(X, means, precisions_chol, covariance_type):
# ���㾫�Ⱦ����1/2�η�log_det�����뾫�Ⱦ�����ͨ��cholesky��ȡ��
    log_det = _compute_log_det_cholesky(precisions_chol, covariance_type, n_features)
# ��Ӧ��������Э�������ͣ��ֱ���㾫�Ⱦ����루x-u)����ǲ���log_prob
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
	# �������logP(x|z)��ֵ
	return -.5 * (n_features * np.log(2 * np.pi) + log_prob) + log_det   

#��2��P(x|z)*P(z)����ÿ��ģ�͵ĸ��ʷֲ�P(x,z),���������������
def _estimate_weighted_log_prob(self, X):
	return self._estimate_log_prob(X) + self._estimate_log_weights()

#��3�����ʼ����ÿ��ģ�͵ĺ������logP(z|x)����Q����
def _estimate_log_prob_resp(self, X):
	weighted_log_prob = self._estimate_weighted_log_prob(X)
	#����P(X)
	log_prob_norm = logsumexp(weighted_log_prob, axis=1)
	with np.errstate(under='ignore'):
		# ��������,����ÿ����˹ģ�͵ĺ�����ʣ���ռ�ȣ����������
		log_resp = weighted_log_prob - log_prob_norm[:, np.newaxis]
    return log_prob_norm, log_resp
#(4)�������Ϻ���
#�������������ĸ��ʾ�ֵ����ÿ����˹�ֲ���Qֵ
def _e_step(self, X):
	log_prob_norm, log_resp = self._estimate_log_prob_resp(X)
    return np.mean(log_prob_norm), log_resp
	
	
	
#2.��ӦM step
def _m_step(self, X, log_resp):
	#���������õ�ÿ����˹ģ�͵�Qֵ(log_resp)�����¹����ֵself.means_��Э����self.covariances_����ǰ���ϸ���˹ģ�͵�������Ŀself.weights_�������������Ȩ�أ�ʵ��ָ������Ŀ��
	n_samples, _ = X.shape
	self.weights_, self.means_, self.covariances_ = (_estimate_gaussian_parameters(X, np.exp(log_resp), self.reg_covar,self.covariance_type))
	#���µ�ǰ����˹ģ�͵�������ʣ���P(Z)
	self.weights_ /= n_samples
	#����cholesky�ֽ���㾫�Ⱦ���
	self.precisions_cholesky_ = _compute_precision_cholesky(self.covariances_, self.covariance_type)
	
#Ȼ���ظ����Ϲ��̣��������EM�㷨��ʵ������