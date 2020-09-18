Recurrent Neural Networks
=========================
In this section I explore the use of recurrent neural networks (rnn) to predict and generate text based on some sample input. 

### Inspiration
The inspiration for this section initially came from the [Adam Geitgey](https://github.com/ageitgey) series "Machine Learning is Fun!". In Part 2 of this series, Adam introduces both the concept of a Neural Network and a Recurrent Neural Network.

A Neural Network being a collection of nodes which can each take input and apply some arbitrary calculation to produce an output. Each node (or neuron?) on its own can provide some estimate against the given input toward a correct output. Combining many of these nodes creates a network of calculation that can solve complex problems. The opportunity opened by a neural network here is that it is effectively stateless. An input given to our neural network will always give the same output. Without any form of memory, a neural network cannot do something like, generate grammatically correct text.

Enter the Recurrent Neural Network which gives memory to our once forgetful algorithm. In this implementation, each calculation accounts for previously made calculations. Through this we can both predict and generate text that is _more_ context appropriate. 

## Install

Install Torch (a computing framework for ML algorithms):
```zsh
git clone https://github.com/torch/distro.git ~/torch --recursive
cd ~/torch; bash install-deps;
./install.sh
```

Once this installation completes, you'll need to source your shell configuration file. I'm on zsh so I use:
```zsh
source ~/.zshrc
```
Check that you have the torch prompt available with the command `th`

Install the HDF5 Lua library:
```zsh
brew tap homebrew/science
brew install hdf5@1.18

# Below must be done to link to the correct HDF5 version
cp -r /usr/local/Cellar/hdf5@1.8 /usr/local/Cellar/hdf5
brew switch hdf5 1.8.21_2
export HDF5_INCLUDE_PATH='/usr/local/Cellar/hdf5/1.8.21_2/include'
```

Add the torch-hdf5 library to your Torch framework:
```zsh
git clone git@github.com:deepmind/torch-hdf5.git ~/torch/torch-hdf5
cd torch-hdf5
luarocks make hdf5-0-0.rockspec
```

Don't forget the HDF5 Python library:
```zsh
virtualenv venv
source venv/bin/activate
pip install h5py
```

Finally install torch-rnn (what we wanted the whole time):
```zsh
git clone git@github.com:jcjohnson/torch-rnn.git ~/torch/torch-rnn
```

## Run
Running with this network happens in three separate steps

**Prepare**
- First, we must prepare our sample text. This transforms our text into file types that can then be used by torch
- Example: `cd ~/torch/torch-rnn && python scripts/preprocess.py --input_txt data/tiny-shakespeare.txt --output_h5 data/tiny_shakespeare.h5 --output_json data/tiny_shakespeare.json`

**Train**
- Now, we are ready to train a RNN with the sample text. Here we are building the model based on the text from the previous step. Training will run through many (default: 50) as it attempts to minimize the "loss" detected between each epoch.
- This step will take awhile!
- `th train.lua -input_h5 data/tiny_shakespeare.h5 -input_json data/tiny_shakespeare.json -gpu -1`

**Sample**
- We can now sample generated text from the network. Many checkpoint files will be created under (1 for every 1000 iterations of training)
- `th sample.lua -checkpoint cv/checkpoint_10000.t7 -length 2000 -gpu -1` (note, you may need to provide the absolute path to your checkpoint file)

Notice how the sample improves with each checkpoint file created.

Checkpoint 1000:
```
l?' Moon,
And that be wire whichers arm belly's but is about is
noth I war envajew, Tirance I have do contar
is tand blood put bone; wander wolmy deithan tomman
The devife know be not king you cointle it theart
Of thyself sain uncomes as as ay to-wargh
I'l
```

checkpoint 15000:
```
GLOUCESTER:
Youse! for leavens,
To be confer'd the resolusure for them
Is trument on badly like with Pruch all
hadder chained and him.

BUCKSS OF YORK:
What I intent I should from enemies,
With so trials and surew'd power faces with t
```