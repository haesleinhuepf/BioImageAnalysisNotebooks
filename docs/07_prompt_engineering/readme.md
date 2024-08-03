# Prompt engineering

In this chapter, we will learn about prompt engineering. Prompts are used to request information or code from large language models such as [chatGPT](https://chat.openai.com/) and [Dall-E](https://openai.com/dall-e-3). We will also use [huggingface](https://huggingface.co/), [LangChain](https://github.com/hwchase17/langchain), [darth-d](https://github.com/haesleinhuepf/darth-d/), and [bia-bob](https://github.com/haesleinhuepf/bia-bob) to execute specific tasks.

Note: Generated text/code/images are not always reproducible. I had to execute some of the notebooks in this chapter multiple times to make them show useful examples. When executing them again, you may get different results and error messages. As the output also depends on software installed on OpenAI's remote server, these notebooks may not produce the same result ever again in the far future.

## Installation instructions

The OpenAI API and LangChain can be installed using mamba and pip.

```
mamba install openai==1.5.0 -c conda-forge
```

```
pip install langchain==0.0.350
```

In order to make it work, you need to get a [paid] subscription to the [openAI API](https://openai.com/blog/openai-api). Note: Executing the notebooks in this chapter may cost actual money.
Furthermore, it is recommended to generate an API key and store it in the `OPENAI_API_KEY` environment variable.

For running Huggingface models, you need to install these libraries:

```
mamba install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
```

```
pip install diffusers==0.24.0 transformers accelerate
```

Darth-d can be installed using mamba:

```
mamba install darth-d==0.4.0 -c conda-forge
```

For using bia-bob, we need to install it using pip:

```
pip install bia-bob==0.6.1
```
