# Simulations for Hayes et al

Generating simulated datasets:

```bash
wolfram -script snpdfe_spike_gen_cmdargs.m 0 0.05 sfs_n100_g0_e0.05.txt
wolfram -script snpdfe_spike_gen_cmdargs.m 10 0.05 sfs_n100_g10_e0.05.txt
wolfram -script snpdfe_spike_gen_cmdargs.m 0 0.1 sfs_n100_g0_e0.1.txt
wolfram -script snpdfe_spike_gen_cmdargs.m 10 0.1 sfs_n100_g10_e0.1.txt
```

Running anavar:

```bash
mkdir /shared/evolgen1/shared_data/hayes_et_al_sims
python run_anavar.py -sim_data sfs_n100_g0_e0.05.txt -out_dir /shared/evolgen1/shared_data/hayes_et_al_sims/anavar/
python run_anavar.py -sim_data sfs_n100_g10_e0.05.txt -out_dir /shared/evolgen1/shared_data/hayes_et_al_sims/anavar/ 
python run_anavar.py -sim_data sfs_n100_g0_e0.1.txt -out_dir /shared/evolgen1/shared_data/hayes_et_al_sims/anavar/ 
python run_anavar.py -sim_data sfs_n100_g10_e0.1.txt -out_dir /shared/evolgen1/shared_data/hayes_et_al_sims/anavar/ 
```

Processing results:

```bash
ls /shared/evolgen1/shared_data/hayes_et_al_sims/anavar/*res.txt | python gather_res.py > possel_error_sim.csv
Rscript summarise_results.R
```