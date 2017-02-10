---
layout:     post
title:      "Evaluation of the RASM Land Surface Climate"
date:       2016-07-01 12:00:00
author:     "Joe Hamman"
header-img: "img/home-bg.jpg"
comments: true
---

My dissertation work has focused on developing, implementing, and improving the land surface model components within the Regional Arctic System Model (RASM; [1](http://www.oc.nps.edu/NAME/RASM.htm), [2](http://uw-hydro.github.io/current_project/rasm)). RASM is a high-resolution regional Earth System Model applied over a pan-Arctic study domain. Included in RASM are five main model components: the Weather Research and Forecasting (WRF) model, the Los Alamos Sea Ice Model (CICE), the Variable Infiltration Capacity (VIC) model, the RVIC streamflow routing model, and the Parallel Ocean Program (POP) model. These five model components are coupled via CESM's flux coupler (CPL 7).

![RASM](/img/rasm_schematic_domain.png)

*Left: RASM coupling schematic. Right: RASM model domain.*

We were tasked with working with the land surface components within RASM (VIC and RVIC). In this post, I'll be highlighting a few of the main points that came out of the first [RASM land surface climate paper](http://dx.doi.org/10.1175/JCLI-D-15-0415.1), published in the *Journal of Climate* a few days ago. A second paper that covers the coupling of the RVIC streamflow routing model will be submitted to the *Journal of Geophysical Research: Oceans* soon.

## Land surface climate in the Regional Arctic System Model

#### Summary

This work introduces a new land surface scheme as part of the Regional Arctic System Model (RASM) and presents the baseline evaluation of the dominant terrestrial processes at play in the Arctic climate system. This study is intended to lay the groundwork for future model application and development of RASM. This work introduced a novel coupling of the VIC model within a coupled Earth System Model. Perhaps most notably, a novel coupling between VIC and WRF. In the process of validating the VIC mode, we identified areas where both RASM and global reanalyses could be improved, namely in the simulation of turbulent heat fluxes and runoff generation. The primary goal of this study was to identify areas where the RASM land surface scheme is performing well and areas for future development. This work used the fully-coupled implementation of RASM and evaluated the performance of the land surface scheme relative to a range of observation, remote sensing and model based dataset. The performance of the model was assessed based on RASM’s ability to represent the first order behavior of Arctic land surface processes such as the seasonal cycle of snow, the differences between the tundra and taiga in terms of turbulent heat fluxes, and the partitioning of precipitation into evaporation and runoff. Recommendations for further model development related to atmosphere-canopy interactions and frozen soils were presented.

#### Domain wide model performance

It is important that a regional model, such as RASM, be able to adequately capture the large-scale seasonal, annual, and spatial patterns in the climate. This work provides spatio-temporal statistics that are meant to illustrate RASM's performance across the model domain. In the figure below, the seasonal and annual 2-meter air temperatures from RASM are compared to those from two global reanalyses. While annual differences are fairly small, RASM exhibits cold season biases at high latitudes that can exceed 5 degrees Celsius. These biases are thought to be due to problems within the resolution of clouds within WRF (See Cassano et al., in revision). Notably, in the summer months (JJA), when you might argue the land-atmosphere coupling is the strongest, the biases are much smaller.

![RASM](/img/rasm_airtemps.png)

*Seasonal and annual average air temperature from RASM (top) and differences with and ERA-Interim and Merra reanalyses (bottom rows); Period: 1989-2014.*

#### Grid-cell scale performance

In order to better understand how the model is performing at the local scale, we have also compared the diurnal cycle of temperature and energy budget terms to an observed dataset. In this case, the observations came from the FluxNET dataset and allow us to compare hourly flux tower observations to the RASM simulated data from the nearest model grid cell. In the figure below, the diurnal cycles are shown for two locations: BOREAS Old Black Spruce and Happy Valley, AK. These  were chosen as characteristic forrest and tundra sites, respectively. Interesting details can been seen for both sites. While the BOREAS site has a persistent cold bias, the behavior (shape) of the diurnal cycle of temperature is well resolved. The opposite tends to be true for the Happy Valley site, where the mean is well resolved but the shape of the diurnal cycle is too dampened.

![RASM](/img/rasm_diurnal_cycle.png)

*Observed July averaged diurnal cycle at the BOREAS Old Black Spruce site (left column) and the Happy Valley, Alaska site (right column) flux tower locations compared to the RASM simulated diurnal cycle at the nearest grid cell location. The top row shows surface air temperature and the bottom row shows net radiation (Rn), latent heat (LH), and sensible heat (SH). Time period: 1994-­1995.*

#### Hydrologic budgets at the basin scale

The scarcity of distributed hydrologic measurements of runoff, precipitation, and evapotranspiration, make the evaluation of basin scale land-atmosphere hydrometerological processes difficult. Here, we use streamflow measured at individual gauge locations as an integrated measure of the performance of the land surface model in terms of the relationship between the hydrology and surface energy budget. In the figure below, we present scatter plots of observed and modeled (RASM and MERRA) streamflow and precipitation. While there is some scatter in each of the plots, the Lowess best-fit line demonstrates disparate model behavior in terms of streamflow from RASM and MERRA despite similar statistics and performance in the annual precipitation. Just looking at the MERRA results, its clear that MERRA over predicts the evapotranspiration (and latent heat) across much of the Arctic land areas.

![RASM](/img/runoff_behavior.png)

*Comparison of observed precipitation (A2006) and streamflow (R-­ArcticNet) to RASM and RMERRA at 690 individual basins. The blue line is a Lowess best-­fit model. The Root Mean Square Error (RMSE; mm/day), and Bias (mm/day) statistics are shown in the top left corner of each panel. Climatological mean of coincident records between 1980-­2014.*

#### Conclusions:

1. This paper was intended to introduce the RASM land surface climate and provide a baseline publication for future studies and model development.
2. The RASM land surface was evaluated in terms of its performance relative to a number of different datasets describing a range of important terrestrial processes.
3. Our evaluation explored the behavior and performance of RASM across a range of spatio-temporal scales.
4. Future development of RASM will focus on the improvement of canopy and frozen soil processes within VIC.

#### References:
- Hamman, J., B. Nijssen, M. Brunke, J. Cassano, A. Craig, A. DuVivier, M. Hughes, D.P. Lettenmaier, W. Maslowski, R. Osinski, A. Roberts, and X. Zeng, 2016: Land surface climate in the Regional Arctic System Model. Journal of Climate, [doi:10.1175/JCLI-D-15-0415.1](http://dx.doi.org/10.1175/JCLI-D-15-0415.1).
- Cassano, J., A. DuVivier, A. Roberts, M. Hughes, M. Seefeldt, M. Brunke, A. Craig, B. Fisel, W. Gutowski, J. Hamman, M. Higgins, W. Maslowski, B. Nijssen, R. Osinski, X. Zeng, 2016: Near surface atmospheric climate of the Regional Arctic System Model (RASM). Journal of Climate, in revision.
