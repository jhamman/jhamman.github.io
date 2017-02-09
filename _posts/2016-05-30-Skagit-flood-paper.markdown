---
layout:     post
title:      "Skagit Flooding"
date:       2016-05-30 12:00:00
author:     "Joe Hamman"
header-img: "img/home-bg.jpg"
comments: true
---

Recently, Nortwest Science published a special issue on [Climate Change Impacts in the Skagit River Basin](http://dx.doi.org/10.3955/046.090.0102). Included in that special issue was the [paper](http://dx.doi.org/10.3955/046.090.0106) that came out of my Master's work. The idea behind the work was to combine a series of modeling capabilities as a proof of concept for how we can start planning for changes in flood regimes given our current knowledge of climate change.

![skagit_floods](/img/skagit_floods.png)

*Example flood inundation map in the Skagit river basin.*

The work itself was by no means an exhaustive evaluation of modeling approaches for climate impacts studies. Instead, we aimed to show that you can combine tools in a modeling chain to provide projections of future flood risk. The modeling chain in our study was roughly:

- Emission Scenarios (A1B)
- GCMs (ECHAM5)
- Downscaling Methods (Statistical, Dynamic)
- Hydrologic Model (VIC)
- Streamflow Routing Model (Lohmann et al 1996)
- Reservoir Operations Model (SkagitSim)
- Hydrodynamic Flood Model (Flo2D)

The Flo2D model is the same model used by FEMA and USACE for their flood mapping activities. This allowed us to provide a "real-world" demonstration of the impacts of changes in flood magnitude and sea level rise.

Following up on my work, The Skagit Climate Science Consortium (SC2) funded work to provide an interactive mapping tool that allows users to visualize future flood scenarios.  The tool turned out really nice and is publicly available here: [http://www.skagitclimatescience.org/flood-scenario-map/](http://www.skagitclimatescience.org/flood-scenario-map/).

#### Refs:
- Northwest Science Special Issue: http://dx.doi.org/10.3955/046.090.0102
- Hamman, J., A. Hamlet, S. Lee, E. Grossman, and R. Fuller, 2016: Combined Effects of Projected Sea Level Rise, Storm Surge, and Peak River Flows on Water Levels in the Skagit Floodplain. Northwest Science, [doi:10.3955/046.090.0106](http://dx.doi.org/10.3955/046.090.0106).
