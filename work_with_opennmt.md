some commands for [opennmt](https://github.com/OpenNMT/OpenNMT-py/tree/master/onmt)
--------

- preprocess

        $ python preprocess.py -train_src data/src-train.txt -train_tgt data/tgt-train.txt -valid_src data/src-val.txt -valid_tgt data/tgt-val.txt -save_data data/demo -src_seq_length 10000 -tgt_seq_length 10000 -src_seq_length_trunc 400 -tgt_seq_length_trunc 100 -dynamic_dict -share_vocab -shard_size 100000
    
Text summarization::
    

    >>> text = """Automatic summarization is the process of reducing a text document with a \
    computer program in order to create a summary that retains the most important points \
    of the original document. As the problem of information overload has grown, and as \
    the quantity of data has increased, so has interest in automatic summarization. \
    Technologies that can make a coherent summary take into account variables such as \
    length, writing style and syntax. An example of the use of summarization technology \
    is search engines such as Google. Document summarization is another."""

    
* train
    * simple nn
    
    $ python train.py -save_model models/002/002 -data data/demo -copy_attn -global_attention mlp -word_vec_size 256 -rnn_size 512 -layers 1 -encoder_type brnn -train_steps 210000 -max_grad_norm 2 -dropout 0\.2 -batch_size 128 -valid_batch_size 16 -optim adagrad -learning_rate 0.15 -adagrad_accumulator_init 0.1 -reuse_copy_attn -copy_loss_by_seqlength -bridge -seed 777 -save_checkpoint_steps 100000 -report_every 10000 -world_size 1 -gpu_ranks 0
    
  * transformer
  
  ```$ python -u train.py -data ../../../data/en/opennmt/4traine/demo -save_model ../../../models/en/opennmt/003/003 -layers 4 -rnn_size 512 -word_vec_size 512 -valid_batch_size 16 -max_grad_norm 0 -optim adam -encoder_type transformer -decoder_type transformer -position_encoding -dropout 0\.2 -param_init 0 -warmup_steps 8000 -learning_rate 2 -decay_method noam -label_smoothing 0.1 -adam_beta2 0.998 -batch_size 4096 -batch_type tokens -normalization tokens -max_generator_batches 2 -train_steps 200000 -accum_count 4 -share_embeddings -copy_attn -param_init_glorot -save_checkpoint_steps 100000 -report_every 10000 -world_size 1 -gpu_ranks 0```
  * re-training
  
  ```$ python train.py -save_model models/002/002 -data data/demo -copy_attn -global_attention mlp -word_vec_size 256 -rnn_size 512 -layers 1 -encoder_type brnn -train_steps 300000 -max_grad_norm 2 -dropout 0\.2 -batch_size 128 -valid_batch_size 16 -optim adagrad -learning_rate 0.15 -adagrad_accumulator_init 0.1 -reuse_copy_attn -copy_loss_by_seqlength -bridge -seed 777 -save_checkpoint_steps 100000 -report_every 10000 -world_size 1 -gpu_ranks 0 -train_from models/002/002_step_210000.pt -reset_optim keep_states```

* translate

```$ python translate.py -gpu 0 -batch_size 20 -beam_size 10 -src data/src-test.txt -model models/001/001_step_200000.pt -output models/001/translate_001.txt -verbose -stepwise_penalty -coverage_penalty summary -beta 5 -length_penalty wu -alpha 0.9 -block_ngram_repeat 3 -ignore_when_blocking "." "</t>" "<t>"```
