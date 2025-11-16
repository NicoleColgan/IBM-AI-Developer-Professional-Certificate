# Business and career transformations through AI

## AI agents
* engage with surroundings, collect & process data, execute tasks indeppendently to meet human goals. they can make decisions, solve problems & adapt to new info
* working: 
    * perception (sensors, cameras etc to gather data about env eg detecting pedestrians)
    * understand (process data with algorithm, indentify objects, speed, movement)
    * Decision making: use knowledge base and logic eg determine when to turn
    * Action: do action like controlling stearing
    * Learning: improve using ml eg analysing past experiences
* Characteristics of Agents:
    * social ability: allows to communicate and collaborate with others
    * Autonomy: make decisions by working alone
    * Reactiveness: respond quickly to changes
    * Proactivenes: take initiatives and make decisions
* Multiagent systems = multiple agents working together eg gmail
* compound system integrates other components eg db into the ai system
* ReAct agents: (Reason + Act) user query -> reason (plan) -> Act (maybe using tools) -> observe (how did my output do - is it good) -> either answer or iterate and go back to reasoning step until answer is good enough
* Control logic is how we decide how the answer is produced. It can be more programatic (us telling it how to solve the problem) or agentic (agent decides how to answer it)
* For narrow problems like answering questions about the weather, it makes sense to use more of a programatic route cause we say - use this weather db to answer the suqestion
* For larger problems, it makes more sense to use agentic because for example in a chatbot, the user could ask about anything so we should let the llm decide how to answer and what tools/process to use to answer the question

## Robotics and automation
* components of robots:
    * Sensors: how the robot detects things in the env. Kind of like the robots eyes and ears. Used to gather info and help navigation and detecting obsticles
    * Actuators: thing that makes the movement and interaction ie the robots muscles eg electric moors, hydraulics
    * Controllers: logic that acts like the robots brain that runs software to control the robots parts. Interprets data and tell the muscles to move
* Robots can integrate ai to be smarter eg an ai vacum cleaner can use sensors to detect furniture or dirt then use controllers to map the home and chose the best cleaning path. Actuators then adjust the wheel direction so it can move in the right direction
* Robots that work alongside humans (or other robots) are called "Cobots" or collaborative robots. eg when manufacturing a car, one robot could hold the screw in place while the other one twists it
* Used in many industried eg in health care, if we have a surgery that involves a lot of precision, a robot could be safer cause its not prone to shaking etc so it will be more precise, agriculture robots can plant, harvest, monitor crop health
* Robotic process automation (RPA) a software that automates repetitive tasks and helps create, use and control virtual robots. These actually do the work not just control the things that do. They act as the human when they work with digital systems & systems. When we refer to rpa we are usually just referring to the virtual robot doing the task but in reality it just means we dont have to do everything to get the robot to work
* Can work in many industries eg in hr it can manage the recruitment process by screening cvs, scheduling interviews, and handling comunication. It can also handle leave requests by reviewing the request and rejecting and accepting it and sending neccessary communication

## Intro to RAG

### **What is Retrieval Augmented Generation (RAG)?** 💡

**RAG** is a framework that combines two main processes to enhance the output of a Large Language Model (LLM): **Retrieval** and **Generation**.

It solves the problem of LLMs being limited to only the data they were initially trained on, allowing them to access external, real-time, or private data sources (like your company's documents or a specific knowledge base).

### **How RAG Works (The Three-Step Process)**

Instead of the LLM relying solely on its internal memory, RAG follows these steps: 

1.  **Retrieval (Finding the Data):**
    * When a user submits a question (a prompt), the RAG system first searches a **separate, external knowledge base** (your documents, a database, etc.) for relevant information.
    * This is typically done by converting the prompt and the documents into **embeddings** (numerical representations) and finding the chunks of text that are most semantically similar to the question.
2.  **Augmentation (Adding Context):**
    * The most relevant chunks of text retrieved in Step 1 are then added to the user's original question to create a **new, enriched prompt**.
    * This enriched prompt now contains the specific, relevant context that the LLM needs to formulate an accurate answer.
3.  **Generation (Answering the Question):**
    * The LLM (the "chatbot") receives this augmented prompt and uses the provided external context to generate a precise, factual answer.
    * The LLM's role shifts from trying to "recall" facts from its training to simply **summarizing and synthesizing** the information handed to it in the prompt.

### **Key Advantages**

-   **Integration of Private Data:** Allows the LLM to safely and effectively answer questions based on your organization's internal, proprietary, or specific documents (like a manual or sales reports).
-   **Reduces Hallucination:** By forcing the LLM to reference specific, provided facts, RAG significantly lowers the chance of the model generating incorrect or fabricated information ("hallucinations").
-   **Timeliness & Accuracy:** You can continuously update the external knowledge base without having to retrain the entire, expensive LLM.
-   **Traceability:** Answers can often be linked back to the specific source documents, making the system more trustworthy.
