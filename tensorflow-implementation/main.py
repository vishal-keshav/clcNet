# Module Author: bulletcross@gmail.com

# System imports
import tensorflow as tf
import numpy as np
import os

# User imports
import contants as c
import model_def as m
import data_util as d
import ops_util as o

def main():
    print('**********CLC-Network Tensorflow implementation*************')

    logs_path = os.path.join(os.getcwd(), 'tf_log')
    if not os.path.isdir(logs_path):
        os.mkdir(logs_path)

    # Declare placeholders
    x,y = o.declare_placeholders(c)

    #Construct computation graph
    out = m.clc_architecture(x, c)
    dp = d.data_provider(c)

    with tf.name_scope("mse_loss"):
        loss = tf.reduce_mean(tf.losses.mean_squared_error(labels = y, predictions = out)) + l2_loss
    tf.summary.scalar('mse_loss', loss)


    with tf.name_scope("train"):
        train_op = tf.train.AdamOptimizer(c.lr_rate).minimize(loss)

    # Logging through tensorboard
    merged_summary = tf.summary.merge_all()
    writer = tf.summary.FileWriter(logs_path)
    saver = tf.train.Saver()

    print('**************Graph defined, training******************')
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        writer.add_graph(sess.graph)

        for epoch in range(0, c.nr_epochs):
            for step in range(0, c.nr_step):
                batch = dp.get_batch()
                _, step_loss = sess.run([train_op,loss], feed_dict = {x: batch.x, y:batch.y})
                summary = sess.run(merged_summary, feed_dict = {x: feed_x, y:feed_y, keep_prob: 1.0})
                writer.add_summary(summary, epoch*batch_size+step)
                print('Epoch= %d, step= %d,loss= %.4f' % (epoch, step, step_loss))

        chk_name = os.path.join(logs_path, 'model.ckpt')
        save_path = saver.save(sess, chk_name)

if __name__ == "__main__":
    main()
