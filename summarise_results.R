library(dplyr)

sim_res = read.csv('possel_error_sim.csv')

str(sim_res)

summary = summarise(group_by(sim_res, combo), mean_theta=mean(theta_1), lwr_theta=quantile(theta_1, 0.025), upr_theta=quantile(theta_1, 0.975),
                                              mean_gamma=mean(gamma_1), lwr_gamma=quantile(gamma_1, 0.025), upr_gamma=quantile(gamma_1, 0.975),
                                              mean_error=mean(e_1), lwr_error=quantile(e_1, 0.025), upr_error=quantile(e_1, 0.975))

write.csv(summary, 'sim_res.csv', row.names=F)