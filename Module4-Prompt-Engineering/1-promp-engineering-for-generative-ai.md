# Prompt Engineering

## What is a prompt
building blocks of a well designed prompt:
    1. Instructions: good guidlines to follow
    2. Context: for generating relevant content
    3. Input data: Any info provided as part of the prompt eg info to use like test results or a data set
    4. Output indicator: telling it how to produce a good output like lenght, style, structure

## Prompt engineering
prompt engineering means designing effective prompts
Process of creating effective prompts:
    1. Define the goal: What you want the model to generate eg summarise my test
    2. Craft initial prompt
    3. Test prompt: from model
    4. Analyse response: does it align with goals and note where it fell short
    5. Refine the prompt: with details from testing and analysis. Maybe give more context, rephrase.
    6. iTERATE THE PROCESS: Repeas last 3 steps till you get a good response

## Best practices for prompt creation
essential domains:
    * clarity
    * precsion
    * context
    * persona eg pretend you are an astronaut...

## Common prompt engineering tools
Uses for tools:
    * Suggestions for promps based on the input you give it and the output you want
    * Context to help it better understand - how to structure it
    * Iterative refinement of prompt to find most effecive
    * bias mitigation features
    * create domain-specific prompts
    * can offer pre-defined prompt for specific use cases
Tools:
    * IBM Wastsonx.ai: 
        * Prompt lab allows you to experiment with diff prompts using diff llms & build prompts based on what the diff llms need
        * Prompt lab provides sample prompts for diff use cases like summarisation, classification, generation.
        * Add instructions
    * Spellbook:
        * an ide that lets you build llm powered apps and experiment with diff prompts for lots of use cases lie text gen, classification, qa, autocompletion and summarisation
        * has a prompt editor to test 
        * Has prompt templates and pre-build prompts
    * Dust:
        * browser tool
        * allows for chaining of prompts and you can save versions
        * supports api integration
    * prompt perfect:
        * useed to optimise prompts for diff llms
        * autocompletion and diff tools
    * Playground AI platform helps generates prompts for stable diffusion model for image generation
    * Langchain for python
    * PromptBase helps design prompts for many models especially visual like midJourney DALL-E, stable diffusion, Llama, chatGPT#

## Prompt eng basics
* few-shot prompting
* chain of thought - follow instructions one-by-one
* role playing