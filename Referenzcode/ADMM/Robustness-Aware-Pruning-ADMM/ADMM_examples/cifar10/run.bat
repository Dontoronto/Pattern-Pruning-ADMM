#admm compression in natural setting
#python -u new_main.py --config_file config.yaml.example --stage pretrain
python -u main.py --config_file config.yaml.example --stage pretrain
#python -u main.py --config_file config.yaml --stage admm
#python -u main.py --config_file config.yaml --stage retrain

#admm compression in adversarial setting
#python -u adv_main.py --config_file config.yaml.example --stage pretrain
#python -u adv_main.py --config_file config.yaml --stage admm
#python -u adv_main.py --config_file config.yaml --stage retrain