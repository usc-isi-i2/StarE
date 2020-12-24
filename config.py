DEFAULT_CONFIG = {
    'BATCH_SIZE': 128,
    'DATASET': 'wd50k_100_new',
    'DEVICE': 'cpu',
    'EMBEDDING_DIM': 200,
    'ENT_POS_FILTERED': True,
    'EPOCHS': 100,
    'EVAL_EVERY': 5,
    'LEARNING_RATE': 0.0001,

    'MAX_QPAIRS': 15,  # control how many 0s in an item
    'MODEL_NAME': 'stare_transformer',
    'CORRUPTION_POSITIONS': [0, 2],
    
    # important args
    'SAVE': True,
    'STATEMENT_LEN': -1,
    'USE_TEST': True,
    'WANDB': False,
    'LABEL_SMOOTHING': 0.1,
    'SAMPLER_W_QUALIFIERS': True,
    'OPTIMIZER': 'adam',
    'CLEANED_DATASET': True,  # should be false for WikiPeople and JF17K for their original data

    'GRAD_CLIPPING': True,
    'LR_SCHEDULER': True
}


STAREARGS = {
    'LAYERS': 2,
    'N_BASES': 0,
    'GCN_DIM': 200,
    'GCN_DROP': 0.1,
    'HID_DROP': 0.3,
    'BIAS': False,
    'OPN': 'rotate',
    'TRIPLE_QUAL_WEIGHT': 0.8,
    'QUAL_AGGREGATE': 'sum',  # or concat or mul
    'QUAL_OPN': 'rotate',
    'QUAL_N': 'sum',  # or mean
    'SUBBATCH': 0,
    'QUAL_REPR': 'sparse',  # sparse or full. Warning: full is 10x slower
    'ATTENTION': False,
    'ATTENTION_HEADS': 4,
    'ATTENTION_SLOPE': 0.2,
    'ATTENTION_DROP': 0.1,
    'HID_DROP2': 0.1,

    # For ConvE Only
    'FEAT_DROP': 0.3,
    'N_FILTERS': 200,
    'KERNEL_SZ': 7,
    'K_W': 10,
    'K_H': 20,

    # For Transformer
    'T_LAYERS': 2,
    'T_N_HEADS': 4,
    'T_HIDDEN': 512,
    'POSITIONAL': True,
    'POS_OPTION': 'default',
    'TIME': False,
    'POOLING': 'avg'
    
}

DEFAULT_CONFIG['STAREARGS'] = STAREARGS

# print(DEFAULT_CONFIG)