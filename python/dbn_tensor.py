import tensorflow as tf

class RBM:
    def __init__(self, n_visible, n_hidden):
        self.n_visible = n_visible
        self.n_hidden = n_hidden

        self.W = tf.Variable(tf.random.normal([n_visible, n_hidden], stddev=0.01))
        self.h_bias = tf.Variable(tf.zeros([n_hidden]))
        self.v_bias = tf.Variable(tf.zeros([n_visible]))

    def sample_h(self, v):
        prob_h = tf.nn.sigmoid(tf.matmul(v, self.W) + self.h_bias)
        return prob_h, tf.cast(tf.random.uniform(tf.shape(prob_h)) < prob_h, tf.float32)

    def sample_v(self, h):
        prob_v = tf.nn.sigmoid(tf.matmul(h, tf.transpose(self.W)) + self.v_bias)
        return prob_v, tf.cast(tf.random.uniform(tf.shape(prob_v)) < prob_v, tf.float32)

    def contrastive_divergence(self, v, lr=0.01):
        v0 = v

        prob_h0, h0 = self.sample_h(v0)
        prob_v1, v1 = self.sample_v(h0)
        prob_h1, _ = self.sample_h(v1)

        # Weight updates
        self.W.assign_add(lr * (tf.matmul(tf.transpose(v0), prob_h0) -
                                tf.matmul(tf.transpose(v1), prob_h1)) / tf.cast(tf.shape(v0)[0], tf.float32))
        self.v_bias.assign_add(lr * tf.reduce_mean(v0 - v1, axis=0))
        self.h_bias.assign_add(lr * tf.reduce_mean(prob_h0 - prob_h1, axis=0))
