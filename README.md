# PracticalD2T Hackathon

## Main Task: Weather Forecast Generation 🌦️

Your task is to build a system for automatically **generating weather forecasts**. 

The system will have access to [OpenWeather API](https://openweathermap.org/api) which provides access to up-to-date weather from anywhere in the world.

The forecasts should be:
- automatically generated by **open-source** code (+ if possible, open language models),
- **human-readable**,
- **accurate** with respect to the input data,
- concise, complete, captivating, insightful (as much as possible).

### OpenWeather API
For starters, you can find a set of Python scripts for interacting with the [OpenWeather API](https://openweathermap.org/api) in the `scripts/openweather` directory.

You can use each script in either online or offline mode:
- for **online** use, use the argument `-l` / `--location` which is a free-form string describing an address anywhere around the world, e.g. "Prague, Czechia". (The location gets automatically geocoded to GPS coordinates using the [Nominatim](https://nominatim.org) library.)
- for **offline** use, use the argument `-j`/`--json` which is a path to the downloaded JSON file. (This is the preffered form of using the scripts, see the *API key* section).

The script outputs the response a nicely formatted chart, using only a subset of data. Feel free to go through the [docs](https://openweathermap.org/api) and extract the data you actually need!

On [free tier](https://openweathermap.org/price), OpenWeather API provides access to the following data:
- [current weather](https://openweathermap.org/current)
- [5-day forecast (with 3-hour resolution)](https://openweathermap.org/forecast5)
- [air pollution](https://openweathermap.org/api/air-pollution)



#### API key
You will be given to a shared API key. The key is on free tier which is **limited to 1000 requests per day**. 

Please, use it solely for **pre-downloading several data files** for the locations and dates of your choice (up to 1000 requests / # teams) and use the local files for development and testing.

You can also create your own free account(s) to get extra requests.


#### Data files
In the `data` folder, you can find various pre-downloaded files for various locations.

### Subtask #1: Generate the current weather description
The task is to generate a **description of the current weather** in the city(-ies) of your choice.

The system should be flexible enough to work with different kinds of conditions and values, emphasizing the important features of the weather.

👉️ See the [current weather API](https://openweathermap.org/current) description for details.

### Subtask #2: Generate a 5-day forecast
The task is to generate a **5-day forecast** for the city(-ies) of your choice.

The forecast should contain both the general outlook and the details about individual days, drawing on differences and/or similarities between the days to make the description fluent and coherent

👉️ See the [forecast API](https://openweathermap.org/forecast5) description for details.

### Subtask #3: Generate air pollution report
The task is to generate an **air pollution** report for the city(-ies) of your choice.

The report should be useful for the city inhabitants. Therefore, it should not contain only a "dry" description of the values, but also relevant recommendations.

👉️ See the [air pollution API](https://openweathermap.org/air-pollution) description for details.

### Subtask #4: Generate a weather forecast in the local language [advanced]
If you are feeling adventurous, you may extend any of the previous tasks to the multilingual setting. 

In particular, it would be useful to generate the weather report in the local language of the city. How many languages can your system handle at once?

### Evaluation
The most important part of the hackathon is **evaluating the quality of the generated reports**. 

Here are various axes you can evaluate the output on:

- **fluency** - Is the report without syntactical / grammatical errors and is it easily readable?
- **semantic accuracy** - Is the report faithful to the input data, or does it contain false information?
- **completeness** - Does the report contain all the features you wanted to include?
- **consistency** - Is the system able to produce outputs consistently across various inputs?

You have several options on how to perform the evaluation:

#### Referenceless Automatic Metrics
Referenceless metrics take as an input the generated output alone. 

These metrics can help us evaluate the **fluency and readability** of the outputs.

- **LM perplexity** -  How much is a selected language model *likely* to generate the report? (see e.g. [perplexity on HF metrics](https://huggingface.co/spaces/evaluate-metric/perplexity))
- **Quality Estimation** - What is the estimated quality of the report based on the report alone? (see e.g. [COMET-QE](https://huggingface.co/spaces/evaluate-metric/comet/blob/main/README.md), [GEMBA](https://arxiv.org/pdf/2302.14520.pdf))


#### Automatic Metrics: Reference-based
Reference-based metrics take as input the generated output and a reference. 

Since we generally do not have human-written references, we need to focus on the metrics that compare the generated text to the input data. These metrics can help us evaluate the **semantic accuracy** of the output.

- NLGI - 
- **[QuestEval](https://github.com/ThomasScialom/QuestEval)** 

- automatic hallucination metrics
- weathergov?


#### Manual Evaluation
We plan to perform a small-scale **in-house manual evaluation** near the end of the hackathon.

The idea is to **let other hackathon participants evaluate the outputs** of your model. 

For the evaluation process, you should prepare a randomly-selected subset of outputs of your system you want to evaluate.

We will specify the details based on the progress and ambitions of individual teams.

## Alternative Tasks

### Our World In Data

The server [Our World In Data](https://ourworldindata.org/) provides [open data](https://github.com/owid/owid-datasets/tree/master/datasets) in machine-readable format on many interesting topics, including [climate change](https://ourworldindata.org/charts#climate-change), [COVID-19](https://ourworldindata.org/charts#covid-19), or [Annual scholarly publications on AI](https://ourworldindata.org/grapher/annual-scholarly-publications-on-artificial-intelligence).

You can download each data source underlying the chart in a CSV format.

The basic task is: "automatically generate a caption for the chart of your choice". 

But of course, you can be more creative. What about "report interesting trends" or "describe connections across charts"?

### Report on LLM data processing capabilities

This task is a bit more investigative. The goal is to compile a table with capabilities of different LLMs to "digest" different kinds of structured inputs.

 Which models can work from scratch with CSV, JSONs, etc.? And do the accept any input, or are there any cases which cause problems (abbreviations in headers, missing headers, deep nesting, ...)?

The ultimate goal is then to find cases where the LLMs **cannot** successfully process structured data – the output either contains hallucinations or does not make sense at all.

The inputs can be either handcrafted or syntethically generated, the outputs should generally contain descriptions / summaries of the data. Your task is to evaluate and annotate the outputs.

### Explainable data-to-text generation
This task is more linguistically-oriented, and can be in principle combined with any of the previous tasks. The goal is to generate **intermediate representations** of the output text that would help with controlling the output and explain the reasoning process of the model.

The intermediate representations can be on the different levels of abstraction: predicate-argument, deep syntax, surface syntax, etc. (see some of the intermediate representations [here](https://aclanthology.org/W19-8659/)).

The representations should be faithful both to the input data and to the output text, providing an additional level of control over the model.

Besides the inputs from the previous tasks, you can also use some of the more standard data-to-text datasets such as [WebNLG](https://huggingface.co/datasets/web_nlg), [E2E](https://huggingface.co/datasets/GEM/e2e_nlg), or [SportSett:Basketball](https://github.com/nlgcat/sport_sett_basketball). For quick visualization and easy loading of these (and many other) data-to-text datasets you can use [Tabgenie](https://github.com/kasnerz/tabgenie) ([live demo](http://quest.ms.mff.cuni.cz/rel2text/tabgenie)).


*(Credits to Simon Mille for coming up with the last two tasks.)*

## Outcome & Takeaways


## LLM access
TODO our API


### Google Colab
Alternatively, you can use Google Colab notebooks.

**Advantages:** You do not need to rely on our infrastructure, you can re-use existing Jupyter notebooks and you can use the web-ui interface for rapid development.

**Disadvantages:** It may be harder to integrate the notebooks with your custom codebase. Also, the GPUs may not be available or sufficient for the models you want to run.

**Useful links**:
- https://github.com/camenduru/text-generation-webui-colab - colab notebooks for running [text-generation-webui](https://github.com/camenduru/text-generation-webui) with various LLMs