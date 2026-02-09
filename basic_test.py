import tensorflow as tf
import bacpipe

#gpus = tf.config.experimental.list_physical_devices('GPU')
#for gpu in gpus:
#    tf.config.experimental.set_memory_growth(gpu, True)

bacpipe.settings.device = 'cuda'
bacpipe.config.overwrite = True
bacpipe.config.dashboard = False
bacpipe.config.models = [
    "birdnet",
    "perch_bird",
]
bacpipe.config.evaluation_task = ["classification"]
bacpipe.play()
