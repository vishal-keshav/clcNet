import tensorflow as tf

meta_path = './graphs/model.ckpt.meta'
output_node_names = ['MobileNet/Predictions/Reshape_1']

def main():
    with tf.Session() as sess:
        # Restore the graph
        saver = tf.train.import_meta_graph(meta_path)
        # Load weights
        saver.restore(sess, tf.train.latest_checkpoint('./graphs'))
        # Freeze the graph
        frozen_graph_def = tf.graph_util.convert_variables_to_constants(
            sess,
            sess.graph_def,
            output_node_names)

        # Save the frozen graph
        with open('model_frozen.pb', 'wb') as f:
          f.write(frozen_graph_def.SerializeToString())

if __name__ == '__main__':
    main()
