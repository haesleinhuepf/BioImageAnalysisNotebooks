# Algorithm validation

In this chapter we will explore techniques for determining segmentation quality and quality of spot detection algorithms.

## See also
* [The Analysis of Method Comparison Studies (D.G. Altman and J.M. Bland 1983)](https://www-users.york.ac.uk/~mb55/meas/ab83.pdf)
* [Method comparison and Bland-Altman plots](https://www.youtube.com/watch?v=PbSrSupnZFQ)
* [Sklearn: Metrics and scoring](https://scikit-learn.org/stable/modules/model_evaluation.html)
* [Lena Maier-Hein, Annika Reinke, et al. Metrics reloaded: Pitfalls and recommendations for image analysis validation](https://arxiv.org/abs/2206.01653)
* [(Bench)mark: Pitfalls in AI Validation | Annika Reinke](https://www.youtube.com/watch?v=HnRcKln5amw)
* [Quality assurance of segmentation results blog post](https://focalplane.biologists.com/2023/04/13/quality-assurance-of-segmentation-results/)

## Installation of requirements

In this chapter we will use the [statsmodels library](https://www.statsmodels.org/stable/index.html) for statistical testing. 
You can install it using mamba/conda or pip:

```
mamba install -c conda-forge statsmodels
```

```
pip install statsmodels
```
