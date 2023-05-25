# Prompt engineering

In this chapter we will learn about prompt engineering. Prompts are used to request information or code from large language models such as from chatGPT / OpenAI. We will also use [LangChain](https://github.com/hwchase17/langchain) execute custom tasks.

Note: Generated code is not always reproducible. I had to execute some of the notebooks in this chapter multiple times to make them show useful examples. When executing them again, you may get different results and error messages. As the output also depends on software installed on OpenAI's remote server, these notebooks may not produce the same result ever again in the far future.

## Installation instructions

The OpenAI API and LangChain can be installed using pip.

```
pip install openai
pip install langchain
```

In order to make it to work, you need to get a [paid] subscription to the [openAI API](https://openai.com/blog/openai-api). Note: Executing the notebooks in this chapter may cost actual money.
Furthermore, it is recommended to generate an API key and store it in the `` environment variable.
