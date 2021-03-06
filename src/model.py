from keras.layers import Input, Dense, Flatten, Dropout, Lambda
from keras.layers import Conv1D, MaxPooling1D, GlobalAveragePooling1D
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K

from keras.models import Model
from keras.engine.topology import Layer

class BaseModel():

    def __init__(self, input_shape, output_size):
        self.input_shape = input_shape
        self.output_size = output_size

        self.build_model()
        
        print(self.model.summary())

    def fit(self, x_train, y_train, **kwargs):
        return self.model.fit(x_train, y_train, **kwargs)

    def compile(self, *argv, **kwargs):
        self.model.compile(*argv, **kwargs)

    def evaluate(self, *argv, **kwargs):
        return self.model.evaluate(*argv, **kwargs)

    def save(self, path):
        self.model.save(path)


class ECGModel1D(BaseModel):

    def __init__(self, *args, **kwargs):
        super(ECGModel1D, self).__init__(*args, **kwargs)

    def build_model(self):
        inputs = Input(shape=self.input_shape)

        x = Conv1D(32, 1, activation='relu')(inputs)
        x = Conv1D(32, 1, activation='relu')(x)

        x = Conv1D(64, 2, activation='relu')(x)
        x = Conv1D(64, 2, activation='relu')(x)

        x = Dense(64, activation='relu')(x)
        x = Dense(64, activation='relu')(x)
        x = Flatten()(x)
        
        output = Dense(self.output_size)(x)

        model = Model(inputs=inputs, outputs=output)

        self.model = model


class ECGModel2D(BaseModel):

    def __init__(self, *args, **kwargs):
        super(ECGModel2D, self).__init__(*args, **kwargs)

    def build_model(self):
        inputs = Input(shape=self.input_shape)

        x = Conv2D(1024, (3, 3), activation='relu')(inputs)
        x = Conv2D(512, (3, 3), activation='relu')(x)
        x = Conv2D(256, (3, 3), activation='relu')(x)

        x = MaxPooling2D(pool_size=(2, 2))(x)

        x = Dropout(0.25)(x)
        x = Flatten()(x)

        x = Dense(128, activation='relu')(x)
        x = Dropout(0.5)(x)
        
        output = Dense(self.output_size)(x)

        model = Model(inputs=inputs, outputs=output)

        self.model = model
