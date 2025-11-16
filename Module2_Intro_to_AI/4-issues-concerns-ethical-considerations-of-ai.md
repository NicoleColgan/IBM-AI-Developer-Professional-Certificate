# Ethical considerations and responsible use of ai

## ethical considerations
* Include human-in-the-loop
* environmental impact
* data protection
* continuous improvment practises eg feedback mechanisms
* bias
* transparency
* accessibiulity to all segments in society
* use diverse data sets

## Considerations around generative AI
* IP and ownership is complex with ai - does the devs own its output or the person writing the promps
* legal and regulations is needed. Need to have data protection
* privacy and ocnfidentiality in data sets. private AI is created specifially for an organisation which helps data confidentiality
* Hallucination - innacurate or made up. To minimise this, improve data wuality, refine alg, validate input
* CustomGPT.ai makes private bots based on your business content
* Techincal considerations:
    * data quality and quantity
    * Model complexity: more complex = better performance but might be more expensive and harder to understand
    * scalability
    * Robustness
* Deep fakes can make fake ids that can be used to open bank accounts, get loans or access secure locations 

## Hallucination
reasons: data quality, generation method (reinforcement kearning etc), input context (prompts - we need to give it ans contexr)
* to reduce: prompt eng, active mitigation strtey ( settings of llm eg temp - lower=deterministic), multi-shot prompting (giving it multiple examples of the task and output in the prompt)

**Multi-shot prompting** is a technique used with Large Language Models (LLMs) where you provide **multiple examples** (more than one or two) of the desired task and output within the prompt itself to guide the model's response.

## 1\. The "Shot" is an Example

In prompting terminology, a "shot" refers to an example of an input-output pair you give to the LLM to demonstrate the task:

  * **Zero-Shot Prompting:** No examples are provided. The model relies entirely on its pre-trained knowledge.
  * **One-Shot Prompting:** You provide **one** example.
  * **Few-Shot Prompting / Multi-Shot Prompting:** You provide **two or more** examples. "Multi-shot" simply emphasizes the use of several examples to build a strong pattern.

**Example (Multi-Shot Prompt):**

```
**Task: Classify sentiment as POSITIVE, NEGATIVE, or NEUTRAL.**

Example 1:
Text: I found the movie to be quite boring and too long.
Sentiment: NEGATIVE

Example 2:
Text: The customer service was friendly and resolved my issue instantly.
Sentiment: POSITIVE

Example 3:
Text: The color of the shirt is fine, but it arrived two days late.
Sentiment: NEUTRAL

Text: The new software update is perfect and makes my work much faster.
Sentiment: [MODEL COMPLETES HERE]
```

## Perspective of key players around ai ethics
* IBMS pilars of trust: explainability, fairness (people), robust (abnormal input), transparent (how it was developed), privacy
* Microsoft: human-in-the-loop to enable intervention, continuous improvements and monitoring, audits, Algorithm assesment, internal review bodies, responsible AI standard
* Google: socially beneficial, avoid bias, safe, accountable, privacy, standards in scientufic excellence, ensure its used good, review process for AI project
* IBM has a initiative called AI alliance that aims to build trust in AI by fostering open-community, accelerate response AI innovation, prioritise scientific rigor, trust, safetm security, diversity, and economic competitiveness. It also ensures ai education, research, dev, deploement and governance are responsible.

# The importance of AI governance
* AI governance refers to rules, standards, and processes to ensure resposible and ethical dev and deployment of ai systems
* Essentially gaurdrails that ensure the ethcial to minimise risks and maximise benefits
* It reduces costs, increases efficiency, and does automatic tasks
* Since humans can be bias, we influence the data that we feed to the model which can be reflected in the model output
* privacy/copyright infringement from model being trained on private data
* lack of transparency from black box model
* Need monitoring so they dont degrade with bad incoming data/ up to date
* Need guidlines & regulations (NIST AI Risk Management framework and EU AI Act)

# How to implement AI Ethics
guidlines:
    * augmentation no replacement
    * customer permission to use data
    * explainability
Activities to ensure:
    * dichotomy mapping: list all benefits and harm of each feature eg using data to provide benefit but what if that data gets leaked
    * Fix harm by implementing gaurdrails that the ai has to follow (eg storing in safe db), data, follow some framework for creatign ai safely

## Cognitive Computing

-   **Q: What are the core elements of cognitive computing?**
    -   **A:** **Perception, learning, and reasoning.**
    -   **Explanation:** Cognitive computing systems aim to simulate human thought processes. This involves **Perception** (taking in data), **Learning** (improving through experience), and **Reasoning** (using logic and knowledge to draw conclusions and make decisions).

# Glossary
Big data: A dynamic, large, and disparate volume of data being created by people, tools, and machines.
Data readiness: The technique involves removing inconsistencies, filling gaps, and ensuring the data is relevant to the problem of the data.
Edge AI:	A type of AI that lives on the device itself rather than relying on the cloud.
Generative AI: Variational autoencoders (VAEs)	VAEs are a type of generative AI model that works by transforming input data through encoding and decoding. They have three main parts: an encoder network, a latent space, and a decoder network.
Generative AI: Generative adversarial networks (GANs)	GANs involve two neural networks: the generator and the discriminator. The generator creates new data samples, and the discriminator checks if the data is real or fake.
Generative AI: Autoregressive models	Autoregressive models create data sequentially, considering the context of earlier generated elements. These models predict the next element in the sequence based on the previous one.
Generative AI: Transformers	Transformers are generally used in natural language processing (NLP) tasks. They consist of encoder and decoder layers, enabling the model to effectively generate text sequences or perform cross-language translations.
Neural network: Perceptron	The simplest type of artificial neural network consisting of only input and output layers.
Neural network: Feed-forward	A type of artificial neural network in which information flows in one direction, that is, in the forward direction. Each neuron in a layer receives input from neurons in the previous layer and then passes its output to neurons in the next layer.
Neural network: Deep feed-forward	A type of neural network that is similar to the feed-forward network with just more than one hidden layer.
Neural network: Modular	A type of neural network that combines two or more neural networks to arrive at the output.
Neural network: Convolutional neural network (CNN)	A type of neural network that is particularly well-suited for analyzing visual data.
Neural network: Recurrent neural networks (RNNs)	A type of neural network where the neurons in hidden layers receive an input with a specific delay in time. This allows the RNN to consider the context of the input.
