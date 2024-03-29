# Hackathon @ PracticalD2T 2023
This repository contains instructions, code, and data for the hackathon at the [**PracticalD2T workshop**](https://practicald2t.github.io) which takes place on 11 Sep 2023 at SIGDIAL/INLG, Prague.

## Main Task: Weather Forecast Generation 🌦️

Your task is to build a system for automatically **generating weather forecasts**. 

The system will use the [OpenWeather API](https://openweathermap.org/api) which provides access to up-to-date weather from anywhere in the world.

The forecasts should be:
- **automatically generated by open-source code** (+ if possible, open language models),
- **human-readable**,
- **accurate** with respect to the input data,
- optionally: concise, complete, captivating, insightful, etc.

### Data Access
For starters, you can find a set of Python scripts for interacting with the [OpenWeather API](https://openweathermap.org/api) in the `scripts/openweather` directory.

You can use each script in either online or offline mode:
- for **online** use, use the argument `-l` / `--location` which is a free-form string describing an address anywhere around the world, e.g. "Prague, Czechia". (The location gets automatically geocoded to GPS coordinates using the [Nominatim](https://nominatim.org) library.)
- for **offline** use, use the argument `-j`/`--json` which is a path to the downloaded JSON file. (This is the preffered form of using the scripts, see the *API key* section).

By default, the script outputs the response a pretty-printed chart based on a subset of data. Feel free to go through the [docs](https://openweathermap.org/api) and extract the data from the response you actually need!

On [free tier](https://openweathermap.org/price), OpenWeather API provides access to the following data which we will use for the task:
- [current weather](https://openweathermap.org/current)
- [5-day forecast (with 3-hour resolution)](https://openweathermap.org/forecast5)
- [air pollution](https://openweathermap.org/api/air-pollution)



#### API key
You will be given to a shared OpenWeather API key. The key is on free tier which is **limited to 1000 requests per day**. 

Please, use it solely for **pre-downloading several data files** for the locations and dates of your choice (up to 1000 requests divided by # of teams) and use the downloaded files for development and testing.

To get extra requests, you can create your own free account(s).


#### Data files
In the `data` folder, you can find pre-downloaded files for various locations. You can use the data in the `dev` subfolders for development. Feel free to also download the data for the locations of your choice (up to the API limits).

Please, do not optimize for the data in the `test` subfolders: we will use these for final evaluation of you system.

### ☀️ Subtask #1: Generate the current weather description
The task is to generate a **description of the current weather** in the city(-ies) of your choice.

The system should be flexible enough to work with different kinds of conditions and values, emphasizing the important features of the current weather.

See the [**current weather API**](https://openweathermap.org/current) description for details.

### 🌦️ Subtask #2: Generate a 5-day forecast
The task is to generate a **5-day forecast** for the city(-ies) of your choice.

The forecast should contain both the general outlook and the details about individual days, drawing on differences and/or similarities between the days to make the description fluent, coherent, and meaningful.

See the [**forecast API**](https://openweathermap.org/forecast5) description for details.

### 🌬️ Subtask #3: Generate air pollution report
The task is to generate an **air pollution** report for the city(-ies) of your choice.

Consider that the report should be useful for the inhabitants of the city. It should contain not only a "dry" description of the values, but also relevant recommendations.

See the [**air pollution API**](https://openweathermap.org/air-pollution) description for details.

### 🇺🇳 Subtask #4: Generate a weather forecast in the local language [ADVANCED]
Feeling adventurous? Extend any of the previous tasks to the multilingual setting!

Specifically, try to generate the weather report in the local language of the location.

How many languages can your system handle?

### Evaluation
**Evaluating the quality of the generated reports** is the most important part of the hackathon. Therefore, make sure you devote enough time for it.

Here are various qualities you can should evaluate the output on:

- **fluency** - Is the report without syntactical / grammatical errors and is it easily readable?
- **semantic accuracy** - Is the report faithful to the input data, and does it contain all the attributes you wanted to include?
- **consistency** - Is the system able to produce outputs consistently across various inputs?

Here are several options on how to perform the evaluation:

#### Referenceless Automatic Metrics
Referenceless metrics take as an input the **generated output** alone. 

These metrics can help us evaluate the **fluency and readability** of the outputs.

- **LM perplexity** -  How much is a selected language model *likely* to generate the report? (see [perplexity on HF metrics](https://huggingface.co/spaces/evaluate-metric/perplexity))
- **Quality Estimation** - What is the estimated quality of the report, based on the report alone? (see [COMET-QE](https://huggingface.co/spaces/evaluate-metric/comet/blob/main/README.md), [GEMBA](https://arxiv.org/pdf/2302.14520.pdf))


#### Automatic Metrics: Reference-based
Reference-based metrics take as input the **generated output** and a **reference**. 

Since we generally do not have human-written references, we need to focus on the metrics that compare the generated text to the input data. These metrics can help us evaluate the **semantic accuracy** of the output.

- **NLI** - Are all of the output facts entailed in the input data and vice versa? (see [nlgi](https://github.com/ufal/nlgi_eval), you can ask Zdeněk for help)
- **QuestEval** - Is it possible to answer questions from the output based on the input data? (see [QuestEval](https://github.com/ThomasScialom/QuestEval))
- standard **semantic overlap metrics** - [BERTScore](https://huggingface.co/spaces/evaluate-metric/bertscore), [BLEURT](https://huggingface.co/spaces/evaluate-metric/bleurt), etc., - Is the semantics of the output close to the semantics of the input?
  -  using input data as references, potentially first transforming the input to text with simple templates


#### Manual Evaluation
Manual evaluation with human annotators can bring valuable insights and more precise scores than automatic metrics.


Close the end of the hackathon, we plan to perform a small-scale in-house manual evaluation. The idea is to **let other hackathon participants evaluate the outputs** of your model. 

For the evaluation process, you should prepare outputs of your system on the test set(s).

(We will specify the details during the day based on the progress and ambitions of individual teams.)

## Alternative Tasks

### Our World In Data

The server [Our World In Data](https://ourworldindata.org/) provides [open data](https://github.com/owid/owid-datasets/tree/master/datasets) in machine-readable format on many interesting topics, including [climate change](https://ourworldindata.org/charts#climate-change), [COVID-19](https://ourworldindata.org/charts#covid-19), or [Annual scholarly publications on AI](https://ourworldindata.org/grapher/annual-scholarly-publications-on-artificial-intelligence).

You can download each data source underlying the chart in a CSV format.

The basic task is to automatically generate a caption for the chart of your choice. 

Of course, you can be more creative: reporting interesting trends, describing connections across charts, etc.

### Report on LLM data processing capabilities

This task is more investigative. The goal is to compile a table with capabilities of LLMs to "digest" different kinds of structured inputs.

 Which models can work from scratch with CSV, JSONs, etc.? And do the accept any input, or are there any cases which cause problems (abbreviations in headers, missing headers, deep nesting, ...)?

The ultimate goal is then to find cases where the LLMs **cannot** successfully process structured data – the output either contains hallucinations or does not make sense at all.

The inputs can be either handcrafted or syntethically generated. The outputs should generally contain descriptions / summaries of the data. Your task is to evaluate and annotate the outputs.

### Explainable data-to-text generation
This task is more linguistically-oriented, and can be in principle combined with any of the previous tasks. The goal is to generate **intermediate representations** of the output text that would help with controlling the output and explain the reasoning process of the model.

The intermediate representations can be on the different levels of abstraction: predicate-argument, deep syntax, surface syntax, etc. (see some of the intermediate representations [here](https://aclanthology.org/W19-8659/)).

The representations should be faithful both to the input data and to the output text, providing an additional level of control over the model.

Besides the inputs from the previous tasks, you can also use some of the more standard data-to-text datasets such as [WebNLG](https://huggingface.co/datasets/web_nlg), [E2E](https://huggingface.co/datasets/GEM/e2e_nlg), or [SportSett:Basketball](https://github.com/nlgcat/sport_sett_basketball). For quick visualization and easy loading of these (and many other) data-to-text datasets you can use [Tabgenie](https://github.com/kasnerz/tabgenie) ([live demo](http://quest.ms.mff.cuni.cz/rel2text/tabgenie)).


*(Credits to Simon Mille for coming up with the last two tasks.)*

## Outcome & Takeaways
You will **present your results** to the workshop audience at the end of the hackathon.

The form of the presentation is up to you and depends on your time constraints. You can prepare a slide deck, a single slide, a set of notes, or just start a discussion on the topic.

We plan to **summarize the findings on the workshop website**.

In case we find out that multiple teams arrived to meaningful findings, we may summarize the workshop outputs in a publication.


## LLM access
You can access LLMs running on our cluster through the API at `http://quest.ms.mff.cuni.cz/nlg/practicald2t-node{node_number}/generate` with the following parameters:

- `prompt` - the input text
- `max_length` - the maximum length of the generated output (default: 100)
- `temperature` - the temperature of the sampling (default: 0.9)
- `repetition_penalty` - the repetition penalty (default: 1.2)
- `do_sample` - whether to sample or use greedy decoding (default: True)
- `top_p` - the top-p sampling parameter (default: 0.95)
- `top_k` - the top-k sampling parameter (default: 50)

See [scripts/generation/example.py](scripts/generation/example.py) to get an idea of how to use the API.

We have currently 8 NVIDIA RTX A4000 GPUs with 16GB of memory each, we can try to allocate more / larger GPUs if needed. 

We can also swap the models for the ones you are interested in (in case we can fit them on our GPUs).

Generally, we would like to have a single model per team to minimize the delay. Please, agree on the node number you will be using with the other teams.

Currently running models:

| Node number | GPU     | Model                                                                               | Status  |
| ----------- | ------- | ----------------------------------------------------------------------------------- | ------- |
| 1           | 1 x 16G | [`llama-2-7b-chat-hf`](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) (fp16) | running |
| 2           | 1 x 16G | [`llama-2-7b-chat-hf`](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) (fp16) | running |
| 3           | 1 x 16G | [`llama-2-7b-chat-hf`](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) (fp16) | running |
| 4           | 1 x 16G | [`llama-2-7b-chat-hf`](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) (fp16) | running |
| 5           | 4 x 16G | [`bloomz-7b1`](https://huggingface.co/bigscience/bloomz-7b1) (fp32)                 | running |


### Google Colab
Alternatively, you can use Google Colab notebooks. 

Here are some potentially useful links (untested):
- https://github.com/camenduru/text-generation-webui-colab - colab notebooks for running [text-generation-webui](https://github.com/camenduru/text-generation-webui) with various LLMs
- https://medium.com/@aitor.porcellaburu/run-open-source-llm-for-free-in-google-colab-kaggle-84dd64a0a23a - links to various LLM notebooks
- https://towardsdatascience.com/fine-tune-your-own-llama-2-model-in-a-colab-notebook-df9823a04a32 - finetuning LLaMa 2

**Advantages:** You do not need to rely on our infrastructure & you can re-use existing Jupyter notebooks and web UI for rapid development.

**Disadvantages:** It may be harder to integrate the notebooks with your custom codebase. Also, the GPUs may not be available or sufficient for the models you want to run.

