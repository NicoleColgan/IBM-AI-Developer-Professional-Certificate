# Applications of generative AI

## Generative AI fundimenals
discriminative ai: 
    * distinguish between diff classes of data by deciding which side of the decision boundary the data lies in. 
    * Uses algorithms to differentiate, classify patterns and draw conclusions eg spam filters
    * Cant take context into account or generate new content
Diffusion models: add noise to images then reverse it to create something new

## Capeabilities of generative AI
some i didnt know:
    * data generation and augmentation which can be used for further training
    * virtual worlds
Image generation:
    * GANs
    * VAEs
    * Examples:
        * StyleGAN can make high-quality new images
        * DeepArt makes complex and detailed artwork from a sketch
        * DALLE makes images from text
Audio:
    * WaveGAN can create speech, music, environmental noises
    * Googles Tacotron 2 uses advanced tts to create realistic synhetic speach taking into account tone, pitch, modulation, pronounciation, rhythm, expressions - would be good for a course
Video: 
    * videoGPT creates videos from promps and user can guide generation process eg style, timing etc
VAEs: generates patterns to produce similar outputs
GANs: produce highly realistic images and art
autoregressive models create things step by step so good for language generation
RNNs uses time series

## Applications
* Use cases in IT:
    * Software delivery process
    * Infrastructure management
    * Code generation
    * Testing: generating synthetic test data and test cases
    * monitoring and detecting anomolies: IBM Watseon AIOps
    * CI/CD: Gitlab dio automatically creates change logs and release notes, automatically updates deployment templates and scripts
    * Predictive maintanance
    * Code reviews
    * automated documentation
* NoleJ can be used for ai-generated e learning to produce interactive videos, glossaries, summaries, quizzes
* Duolingo uses gpt for translation
* KAI GPT is a banking GPT
* roboadvisors can be used for investment
* Watsonx Orechestrate can automate HR tasks like created job requisitiions, screening CVs, scheduling interviews and onboarding candidates

## Ecomic potential of generative AI
Garter and McKinsey are a research and advisory firm that track the impact of AI on business and they split the business opportunities into 3 categories:
1. revenue opportunities from creating new products with AI
2. Cost and productivity opportunities by employees using ai to do tasks like generating docs etc
3. Risk mitigation opportunities eg using ai to detect bugs in code which reduces risks often before theyre even spotted by customers

## Tools for text generation
LLMs learn patterns and structured during training which allow it to interpret context, grammer, and semantics
* GPT4All can be installed on your machine to be run as a privacy chatbot that keeps your data safe and doesnt leak it. you dont even need internet
* PrivateGPT is another example that uses LLMs
* you can link these tools to your orgs documents
* theres a redo feature with gemini if your not happy with the response

## Tools for image generation
* Free AI image generator - Freepik
* Image-to-image translation means using an image to create another image. used in converting sketched to realistic images, converting satellite images to maps, converting security cam images to high resolution images, enchancging details in medical images
* style-transfer and fusion: extracting style from one image and applying it to another
* Inpainting: filling missing parts of an image: art restoration, foresics, removal of unwanted imaged, blendign virtual objects into real-world scenes
* outpainting: extensing an image by maybe extending its borders to create a larger image, enchance image resolution, painting panoramic views
* stable diffusion is an opensource text-to-image model. Diffusion models are generative models that can create high resolution images. primarily fr text-to-image but can be used for image-to-image inpainting, and outpainting
* styleGan is a model that can seperate the image content from the style to allow for styling without changing the content. This means better control for manipulating specific features
* DeepArt.io is a platform that turns photos into artwork of different styles
* Adobe firefly is good for editing images
image generation models: styleGAN, stable diffusion, DALL-E

## Tools for audio and video generation
* TTS: algorithm trained on human speech
* Tools like Synthesia or Murf.ai can be used and you can choose from different voices, languages and emotions, speed etc
* Audio enchancement tools:
    * Descript: removes background noise, enchances souns wuality, allows for addition of sound effects
    * Audo AI: cleans up unwanted noise

## Tools for code generation
* CodeTester allows you to run and access code online without setting up config and all on our computer
* Programiz is an online python compiler

## Generative ai v agentic
While Generative AI is reactive and responds to prompts, AI agents are proactive and can pursue goals through a series of actions with minimal human intervention. 

Agentic AI uses the reasoning power of Large Language Models (LLMs) to break down complex tasks into smaller, logical steps, a process known as "chain of thought reasoning."

## Glossary
Diffusion model	A type of generative model that is popularly used for generating high-quality samples and performing various tasks, including image synthesis. They are trained by gradually adding noise to an image and then learning to remove the noise. This process is called diffusion.

Discriminative AI	A type of artificial intelligence that distinguishes between different classes of data.

Generative pre-trained transformer (GPT)	A series of large language models developed by OpenAI. They are designed to understand language by leveraging a combination of two concepts: training and transformers.
