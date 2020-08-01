# BBBert20

This repository contains the source files used to produce the paper "Can Twitter data estimate Reality Show outcomes?", accepted in the 2020 edition of the Brazilian Conference on Intelligent Systems (BRACIS). 

Our proposal consists in extract information from a social network (Twitter), and use it to predict the eliminated candidated from the 2020 edition of a popular brazilian reality show. The following sections describe the content of each folder in this repository.

## Analysis

Contains jupyter-notebooks, related to the analysis of the collected and classified tweets related to each candidate nominated for elimination. Each notebook contains a visualization of the quatities of positive, neutral and negative tweets from each candidate. In addition, each notebook performs feature extraction, extracting the feature to build the examples that will be used in our regression analysis. The complete dataset builded by the examples can be found [here](https://github.com/liafacom/bbb2020).

## Infos

Contains informations such as followers of the Twitter account of each candidate and candidates nominated for elimination in each elimination (17 in total) with their respective rejection (informed by the reality show, after the elimination). These informations are used as features for regression.

## Model Analysis

Contains notebook and scripts used to perform regression using the percentage of votes for elimination as our target value. We used the examples generated by the Analysis folder as our dataset and evaluated the choosen models using k-fold cross-validation. To determine the parameters used in each model, we performed Grid-Search over different sets of parameters for each model. The folder also contains an initial feature analysis of the features extracted previously, determining their correlation and importance using different techniques.

## Interpretation

Contains notebooks in wich was performed an analysis over the features extracted previously. We listed the most important features choosen by the interpretable models tested. We also investigate the features choosen by the models using Recursive Feature Elimination.

## Tweet Collection

Contains the tweets-ids of the tweets used in this project and their respective classification (positive, neutral or negative).

## How to cite this work

    Waiting for publication ...