import tensorflow as tf

meta_path = './graphs/model.ckpt.meta'
checkpoint_path = 'model.ckpt'
output_node_name = ['Predictions:0']

def main():
    with tf.Session() as sess:
        # Restore the graph
        saver = tf.train.import_meta_graph(meta_path)
        # Load weights
        saver.restore(sess, tf.train.latest_checkpoint(checkpoint_path))
        # Freeze the graph
        frozen_graph_def = tf.graph_util.convert_variables_to_constants(
            sess,
            sess.graph_def,
            output_node_names)

        # Save the frozen graph
        with open('model_frozen.pb', 'wb') as f:
          f.write(frozen_graph_def.SerializeToString())


"""def optimize_graph():
        input_graph_def = tf.GraphDef()
    with tf.gfile.Open("frozen_model_1.pb", "r") as f:
        input_graph_def.ParseFromString(f.read())

    output_graph_def = optimize_for_inference_lib.optimize_for_inference( input_graph_def, [input_name],
                                                                         [output_name], tf.float32.as_datatype_enum)

    with tf.gfile.FastGFile("optimized_model_1.pb", "w") as f:
        f.write(output_graph_def.SerializeToString())"""

if __name__ == '__main__':
    main()
