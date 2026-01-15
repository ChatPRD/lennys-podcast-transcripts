---
guest: Karina Nguyen
title: OpenAI researcher on why soft skills are the future of work | Karina Nguyen
youtube_url: https://www.youtube.com/watch?v=DeskgjrLxxs
video_id: DeskgjrLxxs
description: 'Karina Nguyen leads research at OpenAI, where she’s been pivotal in
  developing groundbreaking products like Canvas, Tasks, and the o1 language model.
  Before OpenAI, Karina was at Anthropic,...

  '
duration_seconds: 4474.0
duration: '1:14:34'
view_count: 22860
channel: Lenny's Podcast
keywords:
- churn
- metrics
- roadmap
- prioritization
- iteration
- revenue
- hiring
- culture
- management
- strategy
- vision
- persona
- design
- ux
- ui
---

# OpenAI researcher on why soft skills are the future of work | Karina Nguyen

## Transcript

Lenny Rachitsky (00:00:00):
Not only are you working at the cutting edge of AI and LLMs, you're actually building the cutting edge.

Karina Nguyen (00:00:06):
When I first came to Anthropic and I was like, "Oh my God, I really love front-end engineering." And then the reason why I switched to research is because I realized, "Oh my God, Claude is getting better at front-end. Claude is getting better at coding. I think Claude can develop new apps."

Lenny Rachitsky (00:00:20):
What skills do you think will be most valuable going forward for product teams, in particular?

Karina Nguyen (00:00:26):
Creative thinking and you kind of want to generate a bunch of ideas and filter through them and not just build the best product experience. I think it's actually really, really hard to teach the model how to be aesthetic or really good visual design or how to be extremely creative in the way they write.

Lenny Rachitsky (00:00:42):
What do you think people most misunderstand about how models are created?

Karina Nguyen (00:00:46):
When you taught the model, some of the self-knowledge of you actually don't have a physical body to operate in the physical world, the model would get extremely confused.

Lenny Rachitsky (00:00:58):
Today my guest is Karina Nguyen. Karina is an AI researcher at OpenAI where she helped build Canvas, tasks, the o1 chain-of-thought model and more. Prior to OpenAI, she was at Anthropic where she led work on post-training and evaluation for the Claude 3 models, built a document upload feature with 100K context windows and so much more. She was also an engineer at New York Times, was a designer at Dropbox and at Square. It's very rare to get a glimpse into how someone working on the bleeding edge of AI and LLMs operates and how they think about where things are heading. Canvas

(00:01:31):
In our conversation, we talk about how teams that OpenAI operate and build products, what skills she thinks you should be building as AI gets smarter, how models are created, why synthetic data will allow models to keep getting smarter and why she moved from engineering to research after realizing how good LLMs are going to be at coding. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It's the best way to avoid missing feature episodes and it helps the podcast tremendously. With that, I bring you Karina Nguyen. 

(00:02:02):
This episode is brought to you by Enterpret. Enterpret unifies all your customer interactions from Gong calls to Zendesk tickets to Twitter threads to app store reviews, and makes it available for analysis. It's trusted by leading product orgs like Canva, Notion, Loom, Linear, monday.com, and Strava, to bring the voice of the customer into the product development process, helping you build best-in-class products faster. What makes Enterpret special is its ability to build and update customer-specific AI models that provide the most granular and accurate insights into your business, connect customer insights to revenue and operational data in your CRM or data warehouse to map the business impact of each customer need and prioritize confidently, and empower your entire team to easily take action on use cases like win-loss analysis, critical bug detection and identifying drivers of churn with Enterpret's AI system, Wisdom.

(00:02:53):
Looking to automate your feedback loops and prioritize your roadmap with confidence, like Notion, Canva and Linear? Visit E-N-T-E-R-P-R-E-T.com/Lenny to connect with the team and to get two free months when you sign up for an annual plan. This is a limited time offer. That's Enterpret.com/Lenny. This episode is brought to you by Vanta. And I am very excited to have Christina Cacioppo, CEO and co-founder Vanta, joining me for this very short conversation.

Christina Cacioppo (00:03:22):
Great to be here. Big fan of the podcast and the newsletter.

Lenny Rachitsky (00:03:25):
Vanta is a longtime sponsor of the show, but for some of our newer listeners, what does Vanta do and who is it for?

Christina Cacioppo (00:03:32):
Sure. So we started Vanta in 2018. Focused on founders, helping them start to build out their security programs and get credit for all of that hard security work with compliance certifications like SOC 2 or ISO 27001 today, we currently help over 9,000 companies, including some startup household names like Atlassian, Ramp and LangChain start and scale their security programs and ultimately build trust by automating compliance, centralizing GRC, and accelerating security reviews.

Lenny Rachitsky (00:04:04):
That is awesome. I know from experience that these things take a lot of time and a lot of resources and nobody wants to spend time doing this.

Christina Cacioppo (00:04:10):
That is very much our experience, but before the company and to some extent during it. But the idea is with automation, with AI, with software, we are helping customers build trust with prospects and customers in an efficient way. And our joke, we started this compliance company so you don't have to.

Lenny Rachitsky (00:04:26):
We appreciate you for doing that. And you have a special discount for listeners, they can get $1,000 off Vanta at Vanta.com/Lenny, that's V-A-N-T-A.com/Lenny for $1,000 off Vanta. Thanks for that, Christina.

Christina Cacioppo (00:04:41):
Thank you.

Lenny Rachitsky (00:04:45):
Karina, thank you so much for being here. Welcome to the podcast.

Karina Nguyen (00:04:48):
Thank you so much, Lenny, for inviting me.

Lenny Rachitsky (00:04:50):
I'm very excited to have you here because not only are you working at the cutting edge of AI and LLMs, you're actually building the cutting edge of AI and LLMs. You recently launched this feature, which basically... the first agent feature of OpenAI. I also just did this survey, I don't know if you know about this. I did a survey of my readers and asked them what tools do you use every day in your work and most use? And ChatGPT was number one, above Gmail, above Slack, above anything else. 90% of people said they use ChatGPT regularly. 

Karina Nguyen (00:05:23):
That's quite good. 

Lenny Rachitsky (00:05:23):
It's absurd. It wasn't around two years ago.

Karina Nguyen (00:05:25):
Yeah.

Lenny Rachitsky (00:05:26):
Also, we're recording this the week that OpenAI announced Stargate, which is this half trillion dollar investment in AI infrastructure. So there's just a lot happening constantly in AI and you have a really unique glimpse into how things are working, where things are going, how work gets done. So I have a lot of questions for you. I want to talk about how you operate and how you work at OpenAI, where you think things are going, what skills are going to matter more and less in the future, and also just where things are going broadly. So how does that sound?

Karina Nguyen (00:05:55):
Sounds great. Thank you so much. Yeah, I was extremely lucky to join early days Anthropic and learned a lot of things there. And I joined OpenAI around eight months ago. So, yeah, I'm excited to dive more in into-

Lenny Rachitsky (00:06:11):
Okay, I'm going to definitely ask you about the differences between those, but I want to start more technical and just dive right in. I want to talk about model training. People always hear about models being trained, these big models, how much data takes, how long it takes, how much money toss it takes, how we're running out of data, which I want to talk about. Let me just ask you this question. What do you think people most misunderstand about how models are created?

Karina Nguyen (00:06:36):
Model training is more an art than a science. And in a lot of ways we, as model trainers, think a lot about data quality. It's one of the most important things in model training is like how do you ensure the highest quality data for certain interaction model behavior that you want to create? But the way you debug models is actually very similar the way you debug software. So one of the things that I've learned early days at Anthropic was we've discovered especially this Claude 3 training, when you taught the model some of the soft-knowledge of, "Hey, you actually don't have a physical body to operate in the physical world." But then at the same time you had data that taught the model some of the function calls, which is like, "This is how you set the alarm."

(00:07:30):
And so the model would get extremely confused about whether it can set an alarm, but it doesn't have a body in the physical world. So it's like the model gets confused and sometimes it'll over accuse. So sometimes it says, "Look, I don't know. Sorry, I cannot help you." And so there is always a balance trade off between how do you make the model to be more helpful for users, but also not being harmful in other scenarios. And so it's always about how do you make the model more robust and operate across a variety of diverse scenarios.

Lenny Rachitsky (00:08:09):
That is so funny. I never thought about that. Most of the data that it's trained on is kind of assuming it's like a human describing the world and how they operate. It assumes there's a body and you could do things, and the model is told you don't have a body.

Karina Nguyen (00:08:20):
Yeah.

Lenny Rachitsky (00:08:21):
Okay. I want to talk a little bit about data while we're on this topic. I know you have strong opinions here. There's this meme that models are going to stop getting smarter because they're running out of data. They're trained in a large part on the internet and there's only one internet and they've already been trained on it, what more can you show them about the world? And there's this trend of synthetic data, this term synthetic data. What is synthetic data? Why do you think it's important? Do you think it's going to work?

Karina Nguyen (00:08:47):
I think there are two questions here. We can unpack one at a time. But people say we are hitting the data wall. I think people think more in the terms of pre-trained large models that are trained on the entire internet to predict the next token. But what actually the model is learning during that process is actually how do you compress the compression algorithm here? The model learns to compress a lot of knowledge and it learns how to model the world. So the next prediction of the word, like, "Teach me how to drive," basically. And you only have a few words that will match that, a car. So the model actually learns about the world in itself. So it's like it's modeling human behavior, sometimes it's modeling... And when you talk to pre-trained models which are very, very large, they're actually extremely diverse and extremely creative because you can talk to almost any Reddit user through a pre-trained model.

(00:09:56):
But I think what's happening right now with new paradigm of o1 series is that the scaling in post-training itself is not hitting the wall. And that's because basically we went from raw data sets from pre-trained models to infinite amount of tasks that you can teach the model in the post-training world via reinforcement learning. So any task, for example, how to search the web, how to use the computer, how to write, wow, all sorts of tasks that you trying to teach the model all the different skills. And that's why we're saying there's no data wall or whatever, because there will be infinite amount of tasks and that's how the model becomes extremely super intelligent. And we are actually getting saturated in all benchmarks. 

(00:10:52):
So I think the bottleneck is actually in evaluations that we don't have all the frontier, like evals like, I don't know, GPQA, which is a Google-proof question answering, PhD level intelligence. The benchmark is getting to, I don't know, more than 60, 70%, which is what PhD gets. So it's literally hitting the wall in like evals.

Lenny Rachitsky (00:11:19):
I want to follow both those threads. So the first is on this idea of synthetic data. Is a simple way to understand it, that the models are generating the data that future models are trained on and you ask it to generate all these ways of doing stuff, all these tasks as you described, and then the newer models trained on this data that the previous model generated?

Karina Nguyen (00:11:39):
Some tasks are synthetically curated. So this is an active research area is how can you synthetically construct new tasks with models to learn. Sometimes when you develop products, you get a lot of data from the product and user feedback and you can use that data too in this cross-training world. Sometimes you still want to use human data because actually some of the tasks can be really, really hard to teach. Experts only know certain knowledge about some chemicals or biological knowledge, so you actually need to tap into the experts' knowledge a lot. So yeah, I think to me synthetic data training is more for product... It's a rapid model iteration for similar product outcomes. And we can dive more into it, but the way we made Canvas and tasks and new product features for ChatGPT was mostly done by synthetic training.

Lenny Rachitsky (00:12:52):
Let's actually get into that. That's really interesting. I want to talk about evals, but let's follow that thread. So talk about how this helped you create Canvas.

Karina Nguyen (00:12:56):
So when I first came to OpenAI, I really had this idea of, "Okay, it would be really cool for ChatGPT to actually change the visual interface but also change the way it is with people." So going from being a chatbot to more of a collaborative agent, and the collaborator is a step towards more genetic systems that become innovators ultimately. And so the entire team of applied engineers, designers, products, research got formed in the air almost out of nothing. It's just like a collection of people who just got together and we rapidly started iterating with each other. 

(00:13:46):
Actually Canvas is one of the... I would say the first project at OpenAI, where researchers and applying engineers started working together from the very beginning of the product development cycle. And I think there's a lot of things that we have learned on the way, but I definitely came with the mindset of, "We need to do a really rapid model situation such that it would be much easier for engineers to work with the latest model possible, but also learn from user feedback or early internal dog food. How do we improve the model very rapidly?"

(00:14:28):
And it's really hard to kind of like figure out how people... when you deploy a product, how people would be able to use it. And so the way you synthetically train the model is physically figuring out what are the most core behaviors that you wanted the product feature to do. And for Canvas, for example, it came down to three main behaviors. It was how do you trigger Canvas for prompts like, "Write me a long essay," when the user intention is mostly iterating over long documents? Or, "Write me a piece of code," or when to not trigger Canvas for prompts like, "Can you tell me more about President..." I don't know, some of the general questions. So you don't want to trigger Canvas because the user intention is mostly getting answer, not necessarily iterate over the long document. 

(00:15:28):
The second behavior is how do we teach the model to update the document when the user asks? So one of the behaviors that we taught the model is actually have some agency and autonomy to literally go to the document and select specific sections and either delete it or edit, so highlight it and rewrite certain sections. Sometimes the user would just say, "Change the second paragraph to be something friendlier," and we would have to teach the model to literally find the second paragraph in the document and change it to a friendly tone. So basically you teach both how to trigger edit itself, but also how do you teach the model to get higher quality edit for the document?

(00:16:21):
In case of coding, for example, there's also the question of how good the model is of completely rewriting the document, versus having a very specific target edits. So that's another layer of decision boundary within edit itself is, "Let's select the entire document and rewrite completely, or do you want to have a very targeted custom behavior." And when we first launched the model, we would bias the model towards more rewrites because we saw the quality of the rewrites were much higher. But over time you are shifting based on user feedback and what you're learning from iterative deployment.

(00:17:02):
Lastly, the third behavior that we taught synthetically the model is how to make comments on any document. So the way we used that is we would use o1 model to seem a way of user conversation, let's say like, "Write me a document about XYZ." But then we used o1 to produce the document and then we injected user prompt to be like, "Oh, make some comments, critique my piece of writing or critique this piece of writing that you just made." And then we taught the model to make comments on the document on very specific [inaudible 00:17:45] So it's also what kind of comments you want the model to make. Do they make sense or not? How do you teach the quality of that? And it all came down to measuring progress via very robust evals. But, yeah, this is how you used o1 and a synthetic data generation for the training.

Lenny Rachitsky (00:18:07):
Okay, that's so interesting. So you talk about this idea of teaching the model and you mentioned how it's using synthetic data to teach the model different behaviors is a simple way to think about it. Basically that's where you do that by showing it what success looks like using basically evals. Is that the simple way to think about it? Like, "Here's what you doing this successfully would look like," and that teaches it, "Okay, I see this is what I should be doing [inaudible 00:18:31]"

Karina Nguyen (00:18:30):
Yeah, great. Yeah, amazing. Yeah, you got it.

Lenny Rachitsky (00:18:33):
Okay, got it. I want to start unpacking what your day-to-day looks like as you're building these sort of things. Is it like you sitting there talking to some version of ChatGPT, crafting these evals?

Karina Nguyen (00:18:44):
Sometimes I do that. Sometimes I do sit with ChatGPT. Actually, I think I learned this so much from Anthropic, is people spend so much time prompting models and where quality's a really bad batch all the time, and you actually get a lot of new ideas of how do you make the model better? It's like, "This response is kind of weird. Why's it doing this?" And you start debugging or something, or you start figuring out new methods of how do you teach the model to respond in the different way, have better personality, let's say. 

(00:19:19):
So it's the same thing of how personality is made in the models with those. It's very similar methods. But, yes, I think my time at OpenAI have changed. I think when I first came, I was mostly research IC work so I was like building a lot of... I was running code, training models, write evals, working with PMs and designers to learn, teach them how to even think about evaluation. I think that was really cool experience and I think it was just like an adoption of, "How do we do this product management of AI feature for our AI models?" Yeah, but now it's mostly management and mentorship. I'm still doing IC research code up to 4:00 PM, although. But I just kind of changed. 

Lenny Rachitsky (00:20:21):
All right, don't talk too much about being a manager.

Karina Nguyen (00:20:23):
Okay. 

Lenny Rachitsky (00:20:23):
Because everyone's in firing their managers. "Who needs managers anymore?" That's what I hear now. Just kidding. It's interesting that so much of your time was spent on teaching product teams how evals integrate and how important it is. And I've heard this a few times and I haven't personally experienced it yet, so I think it's an important thread to follow is just how writing these evaluations is going to become increasingly an important part of the job of product teams, especially when they're building AI features and working with LLMs. So can you just talk a bit more about what that looks like? Is it sitting there with an Excel spreadsheet basically showing, "Here's the input, here's the output, here's how good the result was"? Talk about what that actually looks like very practically.

Karina Nguyen (00:21:02):
It certainly depends on what you're developing, but there are various types of evaluations. Sometimes I do ask product managers, or there's also new roles that we have, model designers, to go through some of the user feedback maybe or think of various user conversations that should have triggered... Under these circumstances, it should trigger Canvas. And then you have this ground truth label of, "Okay with this conversation it should look trigger Canvas, under this conversation it should not trigger Canvas." And you have this very deterministic kind of eval that for decision-making behaviors is like this.

(00:21:46):
When we were launching tasks, for example, how do you make correct schedules is actually really hard for the model. But we built out some of the deterministic evaluations that is like, "Okay, if the user says 7:00 PM, the model should say 7:00 PM." So if you can have deterministic evals whether it's pass or fail. And the way it works is all the... Sometimes I ask product managers to just go create a double sheet, have different tabs and what's the current behavior, what's the ideal behavior and why, and some notes. 

(00:22:27):
And sometimes they usually use it with evals, sometimes we use it for training. Because if you give the spreadsheet to o1 model, it can probably figure out how to teach itself a good behavior. And I think there are second type of evals that is more prevalent is human evaluations. And you can have specific trainers or you can have internal people to when you have a conversation of the prompt and then you have various completion of models, you choose the win rate. Which model is the best? Which model produce the highest quality comment or edit? And then you can have continuous win rates. And as you develop new models it should always win over the previous models. So it depends on what you want to measure.

Lenny Rachitsky (00:23:22):
So interesting. Basically what I'm hearing, and there's something I'm learning about as I talk to people, is product development might move from this, "Here's a spec PRD, let's build it together and then cool, let's review it. Are we happy with this?" From that to, "Hey, AI, build this thing for me and here's what correct looks like," and I'm spending all my time on what does correct look like on evals essentially. 

Karina Nguyen (00:23:47):
You definitely want to measure progress of your model and this is where evals is, is because you can have prompted model as a baseline already. And the most robust evals is the one where prompted baselines get the lowest score or something. And then because then you know if you're trained a good model, then it should just hill climb on that eval all the time, while not also regressing on other intelligence evals. That's what I'm saying, it's more of an art than science. It's like, "Okay, if you optimize the model for this behavior, you don't want to brain damage in other areas of intelligence or..." This is happening all the time in every lab, in every research team. 

(00:24:35):
I would say prompting is also a way to prototype new product ideas. Early days at Anthropic when I was working file uploads feature, I remember I was just prompting the model to just... I remember we were launching a hundred key contexts. I was just prototyping this in their local browser. I did the demo. People really, really loved it. And they just wanted API for file uploads or something. And then that's when it clicked to me, and also one of the blog posts a long time ago, it clicked on me prompting is a new way of product development or prototyping for designers and for product managers. 

(00:25:20):
For example, one of the features that I want to do is have a personalized starter prompts. So whenever you come to Claude, it should recommend you starter prompts based on what your interests are. And so you can literally do it prompting for that. 

Lenny Rachitsky (00:25:42):
Mm-hmm. To experiment with that. 

Karina Nguyen (00:25:44):
Another feature was generating titles for the conversations. It's a very small micro experience but I'm really proud of. The way we did that was we took five latest conversation from the model, asked the model, "What's the style of the user?" And then for the next new conversation, the generated title will be of the same style. It's just like really little micro experiences like this. 

Lenny Rachitsky (00:26:12):
That's so cool. Did you do that at Anthropic or at OpenAI?

Karina Nguyen (00:26:14):
At Anthropic.

Lenny Rachitsky (00:26:16):
Okay, cool. I love the file upload feature that Claude has by the way. ChatGPT doesn't have that yet, is that right?

Karina Nguyen (00:26:16):
I think has the way. 

Lenny Rachitsky (00:26:23):
[inaudible 00:26:23]

Karina Nguyen (00:26:22):
I think the way it's implement is very different though.

Lenny Rachitsky (00:26:25):
Okay. Maybe it's the PDF feature, because I use it all the time with Claude.

Karina Nguyen (00:26:28):
Yeah. 

Lenny Rachitsky (00:26:28):
Okay.

Karina Nguyen (00:26:28):
That's cool.

Lenny Rachitsky (00:26:29):
Somebody needs to get on that. Main, it's wild how many features you built that I use every day and that many people use every day. This prototyping point you made is really important. It's something that comes up a ton on this podcast also of how that... is maybe the way that AI has most impacted the job of product builders recently is just prototyping instead of going from showing just like, "Here's a PRD, here's a design." PMs are more and more just, "Here's the prototype with the idea that I have," and it's working. You can play with it.

Karina Nguyen (00:26:54):
Yeah.

Lenny Rachitsky (00:26:55):
Yeah. Okay, I want to spend a little more time on how you operate. So you talked about you built this in launch of this tasks feature, is that the way to describe your tasks?

Karina Nguyen (00:27:04):
Yeah. 

Lenny Rachitsky (00:27:06):
So talk about how that emerged and let's better understand just how you collaborate with product teams and how OpenAI works in that way, whatever you can share there.

Karina Nguyen (00:27:14):
I think Canvas and tasks are going into the bucket of projects where it's more short or medium terms. And actually the way Canvas and tasks came about to be was it started with one person prototyping and creating a spec. It's kind of like PRD. It's like creating a spec of the behavior of the model. I don't think tasks is extremely groundbreaking feature necessarily. What makes it really cool is because the models are so general... Model can now search, they can write sci-fi stories, they can search for stocks, they can summarize the news every day. Because the models are so general giving something familiar to people that notifications is very familiar, having reminders is very familiar. So feeling like a form factor for the people who are very familiar, same as Canvas, Google Docs is very familiar, but then you add magical AI moment and it becomes very powerful.

(00:28:26):
But the way it comes usually operationally... Yeah, size is like a prototype, literally prompted prototype of how you would want the model to behave. For tasks, for example, you need to design... Literally design thinking is like okay, well, if the user says, "Remind me to go to lunch at 8:00 AM tomorrow," what information does the model need to extract from that prompt in order to create a reminder? And so this is how you design a spec for a new feature, like a tool. Canvas and tasks are all tools. So it's like how do you create the tool stack?

(00:29:09):
And then it's mostly like developing JSON schema. It was like, "Okay, from this problem maybe the model should extract the time that the user requested." And then you think about which format do you want the time to be? And then how do you want the model to notify you is basically the user should give instruction to the model. And then this instruction would fire off every day or something at that particular time. So, for example, if you say, "Every day I want to learn know about the latest AI news," the model should rewrite into, "Okay search for the latest AI news and this task will get fired at that particular type that the user requested."

(00:30:02):
And then your design is like tool spec. Actually, I don't know. I feel like sometimes it's through conversations I... Either people ask me to join the [inaudible 00:30:15] team and they're like, "Oh my god, we need researchers." Or like, "We need some support. We need to train the models," or sometimes. Canvas was mostly like I just pitched the idea of... It got staffed quite immediately during the break, so it's dependent on the project. And then usually with staffing is mostly a product manager, model designer, actual product designer, a couple of researchers and a bunch of applied engineers. Depends on the complexity of a project. And then for tasks it took, I don't know, like two months or so to go from zero to one basically.

Lenny Rachitsky (00:30:54):
Oh wow.

Karina Nguyen (00:30:54):
For Canvas this was like four, five months, I guess, to go from zero to one. And then you teach product managers how to build evals and maybe how do we not only ship the better feature, but how do we think longer term? What kind of cool features did you want tasks to have? I think it would be nice for tasks to be a little bit more personalized. It'd be nice to have to create tasks via voice on a mobile, right? This is how you get research roadmap right here is thinking how the feature will be developed in the future. 

(00:31:39):
And then from there it's like you start getting data sets. With evals, you want to make sure that goes well. And then you need to have a trade-off between what methods you want to use. And the reason why I really love relying purely on synthetic data instead of collecting data from humans is because it's much more scalable, it's cheap, less than half. You literally sample from the model and you teach the core behaviors of the models and that will generalize to all sorts of diverse coverage.

(00:32:15):
And when you launch the beta feature, you learn so much from the users that you can... All your synthetic sets can be shifted in the distribution and how the users behave on the product behavior. And this is how we improve. And this is what happened with Canvass too when we launched from beta to GA. 

Lenny Rachitsky (00:32:34):
Okay. 

(00:32:35):
This episode is brought to you by Loom. Loom lets you your screen, your camera and your voice to share video messages easily. Record a Loom and send it out with just a link to gather feedback, add context or share an update. So now you can delete that novel link email that you were writing. Instead, you can record your screen and share your message faster. Loom can help you have fewer meetings and make the meetings that you do have much more productive. 

(00:33:02):
Meetings start with everyone on the same page and end early. Problem solved, time saved. We know that everyone isn't a one-take wonder when it comes to recording videos. So Loom comes with easy editing and AI features to help you record once and get back to the work that counts. Save time, align your team, stay connected and get more done with Loom. Now part of Atlassian, the makers of Jira. Try Loom for free today at Loom.com/Lenny. That's L-O-O-M.com/Lenny.

(00:33:34):
Something that I want to help people understand, and I don't even 100% understand this, is what's the simplest way to understand the job of a researcher versus say a model designer and other folks involved? What's the simplest way to understand what researchers do at OpenAI?

Karina Nguyen (00:33:48):
So the project that I described are mostly product-oriented. Research is mostly product research. Another component of my team is actually more longer term exploratory projects. And it's more about developing new methods, understanding those methods under a variety of circumstances. So basically developing methods, you need to follow very similar recipe of building evals but it's much more sophisticated evals. You want to have outer distribution or if you want to measure generalization, you need to capture that. 

(00:34:26):
But it is basically more sciencey in a way where... If we talk about synthetic data, one of the hardest things about synthetic data is how do you make it more diverse? Diversity in synthetic data is one of the most important questions right now. And so it's like exploring ways to inject diversity as a general method that will work for all is one of the research explorations. Other ones is more developing new capabilities. I feel like it's always about you work on this new method and you have signs of life that it's working, either you think of how do you make it more general or you think of how do you make it very useful? And this is how the longer-term projects become more medium, short-term project.

Lenny Rachitsky (00:35:15):
That makes sense. Essentially working on developing ways to make the model smarter, o4, o5, o6. New ways to... o1 was a big breakthrough, right? 

Karina Nguyen (00:35:25):
Yeah. 

Lenny Rachitsky (00:35:25):
The way it operates where it's not just, "Here's your answer," it actually thinks and takes time to think through the process of coming up with an answer. Okay. 

Karina Nguyen (00:35:33):
Yeah. 

Lenny Rachitsky (00:35:34):
Very helpful. Speaking of that, of thinking about the future, where things are going, I want to spend some time on just this insight that basically you are building the cutting edge of AI, at the very bleeding edge of where AI is going and where it is. And so I'm very curious to hear just your take on how you think things are going to change in the world and how people work based on where you see things are going. And I know it's a broad question, but let's say in the next three years, how do you see the world changing? How do you see people's way of working changing?

Karina Nguyen (00:36:08):
It's a very humbling experience to be in both labs, I guess. To me when I first came to Anthropic and I was like, "Oh no, I really love front-end engineering." And then the reason why I switched to research is because I realized at that time it's like, "Oh my god, Claude is getting better at front-end. Claude is getting better at coding. I think Claude can develop new apps or something and so it can develop new features for the thing that I'm working." So it was kind of like this meta realization where it's like, "Oh my god, the world is actually changing." And when we first launched 100K context at that time, obviously I'm thinking about form factors that's like file uploads were very natural, very familiar to people. But you can imagine we could just make infinite chats in the Claude.ai app, as if it's 100K context. 

(00:37:04):
But because file uploads... It's like form follows function. It's like the form factor, the file uploads can enable people to just literally upload anything, the books, any reports, financial and ask any task to the model. And then I remember it was either enterprise customers, financial customers were really interested in that. It's like, "Oh wow." It's actually one of the very common tasks that people do in that setting. It's kind of crazy to see how some of the redundant tasks are getting automated basically by these smart models.

(00:37:48):
And they're entering the era where, I actually don't know for example sometimes if o1 gives me the correct answer or not because I'm not an expert in that field. And it's like, "I don't even know how to verify the outputs of the models." It's because all my experts know they can verify this. So, yes, so basically there are trends that are going on. The first trend is the cost of reasoning and intelligence is drastically going down.

(00:38:22):
I had a blog post about this. Maybe I should update on latest benchmarks, because at that time everybody was doing one benchmark and they'd be... quickly saturated the benchmarks. So I'm like, "Now we need to do the same plot but with another frontier eval." But the cost of intelligence is going down because it becomes that much cheaper. Small models are becoming even smarter than large models and that's because of the distillation research. 

(00:38:56):
This happened with Claude 3 Haiku. I was working with the training on the Claude 3 Haiku and I realized it was much smarter than Claude 2, which was way bigger, lots [inaudible 00:39:08]. But the power of small models become very intelligent and fast and cheap. We are moving towards that world. That has multiple implications, but the news is that people will have more access AI and that's really good. Builders and developers will have much better access to AI, but also it means all the work that has been bottlenecked by intelligence will be unblocked. 

(00:39:40):
I'm thinking about healthcare, right? Instead of going to a doctor, I can ask ChatGPT or give ChatGPT a list of symptoms and ask me, "Would I have a cold, flu, something else?" I can literally get the access to doctor almost. And there's been some research studies around that.

Lenny Rachitsky (00:40:05):
There was a New York Times story about that where they compared doctors to doctors using ChatGPT to just ChatGPT and just ChatGPT was the best of them. All doctors made it worse.

Karina Nguyen (00:40:18):
Yeah, that's crazy. Yeah. Yeah, that's crazy, right? Education I think I would have dreamt if I had the tool like ChatGPT when I was young and would learn so much. But it's like people can now learn almost anything from these models. So they can learn new language, they can learn how to build new look apps and write anything they do want. It's humbling to have... launch Canvas and bring that thing to the people, enable them to do something else that they couldn't have ever before. There's something magical around this experience. 

(00:40:57):
Education will have massive implications. I guess like scientific research, I think it's the dream of any AI research is to automate AI research. It's kind of scary, I'd say, which makes me think that people management will stay. It's one of the hardest thing to... Emotional intelligence with the models, creativity in itself is one of the hardest things. So writers, I don't think people should be worried as much. I think will alleviate a lot of redundant tasks for people.

Lenny Rachitsky (00:41:34):
This is awesome. Okay, I want to follow this thread for sure. And it's funny that what you described as you were an engineer at Anthropic and you're like, "Okay, Claude is going to be very good at engineering. This isn't going to be a potentially career long term, so I'm going to move into research and AI is going to need me for a long time to build it, to make it smarter."

Karina Nguyen (00:41:53):
I would say we still have... I think Canvas team has still have really cool front engineers that are really people who really care about interaction, design, interacting experience. I don't think models are there yet I think if... But we can get the models to this top 1% of front-ends and things for sure.

Lenny Rachitsky (00:42:16):
So what I want to move on to next along these lines is just, and this is just speculation, but what skills do you think will be most valuable going forward for product teams in particular? So folks are listening and they're like, "Okay, this is scary. What should I be building now to help me stay ahead and not be in trouble down the road?" What skills do you think are going to be more and more important to build?

Karina Nguyen (00:42:42):
Yeah, I think creative thinking. You want to generate a bunch of ideas and filter through them and not just build the best product experience. Listening. You want to build something that the most general model will not replace you. And oftentimes you build something and you make it really, really good for specific set of users and actually the mode is now in your user feedback. The mode is more in whether you listen to them, whether you can rapidly iterate. The mode is in here. I don't think we are yet to... There are so many ideas, I think there's an abundance of ideas that you can work on. I wouldn't be worried. I feel like in fact I just think people in AI field are like... I wish they were a little bit more creative and connecting the dots across the print fields or something like that to develop really cool new generation and new paradigms of interactions with this AI.

(00:43:53):
I don't think we've cracked this problem at all. A couple of years ago I was telling some people, I was like, "You want to build for the future." So it's like it doesn't necessarily matter whether the model is good or not, good right now, but you can build product ideas such that by the time the models will be really good, it'll work really well. I think it just happened naturally. For example, at Anthropic the Claude artifacts... And I feel early days of Canvas was, back in 2022 before ChatGPT, writing ideas was our knowledge [inaudible 00:44:36]. But I feel like Claude 1.3 model itself was not there to have made really extreme good high quality edits. For example, like coding. 

(00:44:47):
And I feel like I see startups like Kaeser was doing super well. And that's because they iterate so fast. They invent new ways of training models. They move really fast. They listen to what users like, massive distributions. Yeah, it's kind of cool. 

Lenny Rachitsky (00:45:08):
That's really helpful actually. So what I'm hearing is that soft skills essentially are going to be more and more important, powerful. You just talked about management, leading people, being creative and coming up with innovative insights, listening. There's a post I wrote that I'll link to where I try to analyze how AI will impact product management. And we're actually very aligned, and my sense was the same thing, that soft skills are going to become more and more important. And the things that are going to be replaced is the hard skills, which is interesting because usually people value the hard skills like coding, design, writing really well. And it's interesting that AI is actually really good at that because it's taking a bunch of data, synthesizing it and writing, creating a thing, versus all these fuzzy things around of what influences, convinces people to do things and aligning and listening, like you said, creativity, anything along those lines come up as I say that.

Karina Nguyen (00:46:01):
I think it's actually a really, really hard to teach the model how to be aesthetic or do really good visual design or how to be extremely creative in the way they write. I still think ChatGPT kind of sucks at writing and that's because it's bottlenecked by this creative reasoning. I think characterization is one of the most important... I think for a manager, I feel like... 

(00:46:28):
Actually, AI research progress is bottlenecked by management, research management. It's because you have constrained set of compute and you need to allocate the compute to the research paths that you feel the most convinced about. It was like you need to have a really high conviction in the research paths to put the compute, and it's more return on investment kind of situation. It's like, "Okay, I'm thinking a lot about across all my projects, which projects are higher priority?" Prioritization and also on the lower level, "Which experiments are really important to run right now and which are not?" and cut through the line. So I was thinking prioritization, communication, management. People skills like empathy, understanding people, collaboration.

(00:47:23):
I think Canvas wouldn't be an amazing launch if it wasn't about people and I think it's a wonderful group of people. And I get a chance to work with people like Lee Byron who's a co-creator at GraphQL and some of the best Apple designers. It's so cool to see... and how do you create this collaboration between people. It's just something that's still humane, I think.

Lenny Rachitsky (00:47:52):
Let me just follow through a little bit. I imagine people listening are like, "Okay, but once we have AGI or SGI it's like it'll do all this." There's a world where like, "Why isn't all this done?" I think it's easy to just assume all that. I'm curious this idea of creativity and listening, why you think AI isn't good at it, other than it's just very hard to train it to do this well. Is there anything there of just why this is especially difficult for AI and LLMs to get good at?

Karina Nguyen (00:48:20):
I think currently it's difficult for many reasons. I think it's still an active research area and it's something that I think my team is working on. It's like, "Okay, how do we teach the models to be more creative in the writing?" And so I'm thinking this new paradigm of wise that the models think more should actually lead to better writing in itself. But when it comes down to idea generation or discriminating of what is a good visual design or not, I feel like it hasn't had learned examples from people to discriminate it very well. I do think it's because there are not that many people who are actually really... It's not accessible to models to learn from these people I guess. So I definitely think that's why it sucks.

Lenny Rachitsky (00:49:19):
Yeah, that makes sense. Basically there's not enough of you yet, researchers teaching it to do these things, slash people that have incredible taste and creativity that can teach these things. You could argue this will come. 

Karina Nguyen (00:49:31):
Right. 

Lenny Rachitsky (00:49:31):
But we don't need to keep going down that thread. Let me ask you a specific question. In this post I wrote, I made this argument that a lot of people disagreed with that strategy is something that AI tooling will become increasingly great at and take over. There's the sense that that's the thing that people will continue to be much better at and you can't offload to AI basically developing your strategy, telling you what to do to win. My case is, "Isn't strategy, just take all the inputs, all the data you have available, understand the world around you and come up with a plan to win?" It feels like AI and LLM would be incredibly smart at this. What's your take?

Karina Nguyen (00:50:10):
I think so too. I think again, you teach the model all sorts of tools and capabilities and reasoning and it's like when it comes down to... For Canvas right now, it would be very cool for the model just aggregate all the feedback from users, summarize me the top five most painful flows on user experiences. And then the model itself is very capable of thinking of knowing how it's been made, figure out how to create a dataset for itself to train on it. And I don't think that we are far away from that self-improvement, models becoming self-improved by...

(00:50:54):
That, and the part of development, is basically self-improving. It's kind of like its own organism or something. Again, like strategies, it's more like data analysis and coming up with... I think what models are really good at is connecting the dots, I think. It's like if you have user feedback from this source, but you also have an internal dashboard with metrics and then you have other feedback or input and then it can create a plan for you, recommendations even.  And I think this is one of the most common use cases for ChatGPT too, is coming up with these sort of things.

Lenny Rachitsky (00:51:47):
That makes sense essentially a human can only comprehend so much information at once and look at so much data at once to synthesize takeaways. And as you said, these context windows are huge now. Here's all the information, what's the most important thing I should do?

Karina Nguyen (00:51:59):
Yeah, same as scientific research. Ideally the model would be able to suggest ideas, new ideas, or iterate on the experimental given the empirical results of the previous experiments like how do you come up with new ideas or the methods?

Lenny Rachitsky (00:52:18):
Yeah. Oh, man. Okay, so just to close the loop on this conversation, this part of the thread is the skills you're suggesting people focus on building and leaning into is soft skills like creativity, managing influence, collaboration, looking for patterns. Is that generally where your mind is at?

Karina Nguyen (00:52:40):
Yeah, I'm thinking a lot about how do we make organizations more effectively and I think this is mostly management, I guess. It's like how do you organize research teams or generally teams combined... Compose teams such that they will be at their maximally succeed or at the maximal performance of what can possibly... We can literally create the next generation of computers. It's just the matter of conviction and the way you manage through that. It's scaling organizations or scaling product research, I guess.

Lenny Rachitsky (00:53:15):
Yeah, I think you're basically building this thing and not efficiently doing it is limiting the potential of the human species right now.

Karina Nguyen (00:53:16):
Right. 

Lenny Rachitsky (00:53:26):
It's mismanagement within the research team in OpenAI and Anthropic and some of these other models.

Karina Nguyen (00:53:32):
Yeah, it's kind of crazy to think about it.

Lenny Rachitsky (00:53:33):
Holy moly. Okay, so speaking of Anthropic and OpenAI, you've worked at both. Very few people have worked at both companies and have seen how they operate. I'm curious just what you've noticed about the differences between these two, how they operate, how they think, how they approach stuff. What can you share along those lines?

Karina Nguyen (00:53:48):
It's more similar than different. Obviously there was a lot of... There are some differences always comes to nuances. I would say culture. I really love Anthropic and I have a lot of friends there. And I also love OpenAI and they still have a lot of friends though. So it's not about enemies. I feel like there's in AI, it's all like, "Yeah, they're competitors. There's enemies." It's actually like one big community of people doing the same thing. I would say what I've learned from Anthropic is this real care and craft towards model behavior, model craft, model training. 

(00:54:32):
And I've been thinking a lot about, "Okay, what makes Claude Claude and what makes ChatGPT ChatGPT?" And it's like I still have some sense of operational processes that leads to the outputs, to the model. It's the outputed model. And it's like the reason why Claude has so much more personality and is more like a librarian... I don't know. I don't know. I am visualizing Claude being like a librarian at some point, very nerdy or something. ... is because I feel like it's the reflection of the creators who are making this model. And a lot of details around the character and the personality and whether the model should follow up on this question or not. 

(00:55:19):
What's the correct ethical behavior for the model in these scenarios? A lot of crafts and curated datasets. This is where I learned that part of art, I guess, at Anthropic. I would say Anthropic is much smaller. When I joined it was, what, like 70 people? When I left it was tons of people. And obviously the culture changed so much. I really enjoyed being early days startup lives, and people knew each other as a family. But the culture shifted. 

(00:55:53):
I would say that I learned from Anthropic that they're much better at focusing and prioritization of... Very hardcore prioritization, I guess. And they need to do it. But I think OpenAI's much more innovative and much more risk-takers in terms of product or research. Actually, in way your full-time job can be just teaching the model how to be creative writers. And it's like there's some luxury in this research freedom that comes with scale, maybe. I don't know. I'd say I have much more creative product freedom to do almost anything, I guess, within OpenAI, evolve ChatGPT into the vision that we want. It's more probably bottoms-up, I guess.

Lenny Rachitsky (00:56:51):
Yeah, that's how I was thinking about it. It feels like OpenAI is more bottoms-up, distributed, people bubble up ideas, try stuff. And that leads to more products launching, I imagine more things just kind of being tried versus more of a, "Let's just make sure everything we do is awesome and great and craft and thinking deeply about every investment."

Karina Nguyen (00:57:08):
Right. 

Lenny Rachitsky (00:57:08):
That's really interesting. I've never heard it described this way. Karina, we've covered so much ground. This is going to help a lot of people with so many ways of thinking about where the future's going. Before we get to our very exciting lightning round, I'm curious if there's anything else that you think might be helpful to share or get into?

Karina Nguyen (00:57:23):
One of my regrets, I guess, when I was early days at Anthropic was that... I think there was some luxury of the time, because pre-ChatGPT, to actually come in with a bunch of ideas and prototype almost every day. And I think that we did a lot of cool ideas like Claude, and Slack was actually one of the first tool-usey products. It's like Claude could operate in your workplace now. It's kind of cool because you can add Claude to summarize the thread. So maybe you have an entire conversation with someone and then you want a summary of what happened you can ask Claude, "Summarize this." 

(00:58:07):
Also, it was really fun to iterate on the model itself. It's like when you just talk to the model in Slack forever. It created some social element, it was kind like [inaudible 00:58:19] and this Discord, people learned so much about prompting and how to work with Claude. Actually, one of the features that was early tasks prototype is every Monday Claude would just summarize the entire channel. Or every Friday we'd just summarize a bunch of channels and give the news about the organization, or something. 

(00:58:48):
And it's kind of like really cool form factor. I think thinking about form factor's a really important question in AI, especially we haven't even figured out how do we create an awesome product experience with o-series models. It's like the paradigm between synchronous real time give an answer paradigm into more asynchronous paradigm of agents working on the background. But then now the question is the agents should build trust with you, right? And trust builds over time, which is like with humans. And you start this collaboration which is why this collaboration model with you and the model is so important because you build trust and the model learns from your preferences so that it can become more personalized and it will start predicting the next action that you want to take on the computer or something. And it's more predictive, much more... We went from personal computers to personal model basically here.

Lenny Rachitsky (00:59:54):
Why is it not a thing? That seems like such an obvious feature that every LLM should have as a Slack bot version of them. Is that a thing I can help you install? Or is that not a thing right now?

Karina Nguyen (01:00:03):
I know that Claude and Slack was sunset in 2023 or something. I think it was after ChatGPT was mostly the focus on customer use cases or enterprise use cases.

Lenny Rachitsky (01:00:17):
Mm-hmm. Bummer. 

Karina Nguyen (01:00:19):
I think the form factor of Claude and Slack was kind of constrained a little bit when you want to talk about new features.

Lenny Rachitsky (01:00:28):
Bummer. I want that.

Karina Nguyen (01:00:30):
I know that ChatGPT had Slackbar tools. I don't know, maybe it will come back sometime.

Lenny Rachitsky (01:00:35):
All right, I would pay for that. Any other memories from that time of early days? Because that's a really special place to have been is early days Anthropic. Any other memories or stories from that time that might be interesting to share?

Karina Nguyen (01:00:48):
I think the very first launch when we felt... When click from use, again, was 100K context launch is when the models could input the entire book and give you a summary of the book or something. Or the financial... or catalog multi files financial reports and then give you an answer to the question, to very specific questions. I think there was something in there that was kind like, "Oh my god, this is a really cool new capability." Not model capability, but more like the capabilities that came from the product form factor itself rather than the model capability as much. 

(01:01:34):
I think other prototypes that we were thinking about... There's one part having a Claude workspaces and it's kind of the same idea of Claude and I would have this shared workspace and that share workspace is like a document and we can iterate on the document. And I feel like sometimes the ideas, [inaudible 01:01:55] and they're locked for two years, just like in this case. 

Lenny Rachitsky (01:02:00):
It's interesting, there's these milestones that kind of open up our view of what is happening and where things are going. ChatGPT think was the first of just like, "Wow, this is much better than I would've thought." You talked about 100K context windows where you could upload a book and ask it questions and have it summarize. I actually use that all the time. When I have interview guests and they wrote a book, I sometimes don't have time to read the whole book. So I use it to help me understand what the most interesting parts are. And then I actually dive into the book, just to be clear. And then, I don't know, maybe voice was another one where you could talk to say ChatGPT. Is there any other moments there that you're like, "Wow, this is much better than I thought it was going to be?"

Karina Nguyen (01:02:39):
Yeah, I think the computer use agents, like the model operating the desktop. And you can essentially think of new kind of experience where the model can learn the way you browse. And from that preference it can just browse as just like you. It's kind of simulated persona. And it's actually very similar to the idea of like, "Okay, maybe Sam Altman doesn't have a lot of time. Maybe I want to talk to his simulation and ask..." Or, for example, I really appreciate some of the technical mentorship. Yeah, cool. But he doesn't have a lot of time so it's like I really want to ask him this questions. How do you respond with simulated environments like this would be really cool.

Lenny Rachitsky (01:03:37):
That's a great place to plug Lennybot, have one of those. It's trained on all of my podcasts and newsletters. 

Karina Nguyen (01:03:42):
Oh, cool. 

Lenny Rachitsky (01:03:43):
It sits on many models. I don't know which exactly they use, but it's exactly that. And it's not even me, it's all the guests that have been on the podcast and on newsletter as I wrote. And you could just ask it, "How do I grow my product? How do I develop a strategy?" And it's actually shockingly good.

Karina Nguyen (01:03:58):
Do you feel like it reflects who you are?

Lenny Rachitsky (01:03:58):
Yeah. 

Karina Nguyen (01:03:58):
Or would it be... Okay. 

Lenny Rachitsky (01:04:01):
The best part of it is you can talk to it. There's an ElevenLabs voice version that's trained on my voice from this podcast, and it's actually very good and people have told me they sit there for hours talking to it. 

Karina Nguyen (01:04:15):
Wow.

Lenny Rachitsky (01:04:15):
And somebody told it, "Interview me like I am on Lenny's podcast, ask me questions about my career." And he did a half hour podcast episode with Lennybot.

Karina Nguyen (01:04:24):
Oh my god, that's so fun.

Lenny Rachitsky (01:04:27):
It's incredible. Future is wild.

Karina Nguyen (01:04:29):
Yeah. I think content transformation is... I would imagine sometime when you generate a sci-fi story in Canvas, you can transform this into audiobook where you have very natural content transformation of one media to another media. I think one of my earliest inspiration is one of the last episodes of Westworld where, I don't want to spoil, but where Dolores comes to her work at that time and she comes to this new workspace and she starts writing a story. And then as she writes a story, a 3D, virtual reality, starts creating on the fly. So I kind of want to create that. Kind of cool. 

Lenny Rachitsky (01:05:24):
Wow. Speaking of medium, I guess I was wondering if I should go in this direct or not, but real quick. Kevin Weill/Kevin Weill, I don't know exactly how to pronounce his last name, the CPO of OpenAI.

Karina Nguyen (01:05:35):
Kevin Weill, uh-huh.

Lenny Rachitsky (01:05:37):
Is it Weill or Weill? 

Karina Nguyen (01:05:37):
I think Weill. 

Lenny Rachitsky (01:05:39):
Weill. Okay. Okay. Let's just say that. We'll go with that. 

Karina Nguyen (01:05:40):
I hope, yeah. 

Lenny Rachitsky (01:05:43):
He did a panel at the Lenny and Friends Summit last year and he made this really fascinating point that chat is a really interesting interface for these tools because they're just getting smarter and smarter and smarter and smarter and smarter. And chat continues to work as a paradigm to just interact with them, similar to a human. You could talk to Albert Einstein. You could talk to someone not very smart and it's all conversation still. And so it's a really flexible way to interact with increasingly good intelligence. At some point it'll not be so great, and you were talking about all these ways that you're adding additional ways to interact. But it's interesting chat proved to be a really powerful layer on top of all this stuff. 

Karina Nguyen (01:06:22):
Yeah, that's real cool. I feel like chat also has social element which is very humane. It's like, yeah, you sometimes want to get into group chat. And having conversations with AI is kind of like a group chat in itself, as messaging. Actually, this idea of how do you build features like this? I see tasks as this general feature that will scale very nicely as the models would develop new capabilities themselves. The models will be able to do better searches and create new... come up with more creative writing on render, react apps and like HTML apps. And you can have everyday new puzzle for you, every day continue the story from the previous days. It scales very nicely.

Lenny Rachitsky (01:07:14):
You mentioned something as we were getting into this extra section that we ended up going down is this idea of the agents using a computer. I know this is actually something you are going to launch today, the day we're recording it, which will be out by the time this comes out, called Operator, can you talk about this very cool feature that people will have access to?

Karina Nguyen (01:07:33):
Yeah, so I unfortunately did not work on that, but I'm really, really excited about this launch. It's basically an agent that can complete the task in its own virtual computer, in its own virtual environment. You can do any literally task like order me a book on Amazon. And then ideally the model will either follow up with you which book do you want, or know you so well that it start recommending, "Oh, here is the five books that I might recommend you to buy." And then you hit, "Yeah, help me buy." And then the model goes off into its own virtual little browser and complete the task and buy the book on the Amazon. And then if you give the model credentials, credit cards, obviously it comes with a lot of trust and safety, then it will just complete the thing for you. It's a virtual assistant.

Lenny Rachitsky (01:08:37):
It's interesting how this just sounds like obviously this should happen. Why is this not yet a thing? Which is also mind-blowing that we're just assuming this should exist. Just some AI doing things for you on a computer we just ask it to do. 

Karina Nguyen (01:08:37):
Yeah. 

Lenny Rachitsky (01:08:50):
It's absurd.

Karina Nguyen (01:08:51):
It's actually really hard. And I think you're still cracking this, but feel like... I don't know if you use Tuple like a pair programming product.

Lenny Rachitsky (01:09:03):
No.

Karina Nguyen (01:09:04):
But at Anthropic we loved pair programming, so if you used-

Lenny Rachitsky (01:09:09):
Oh yeah, Shopify uses this. I remember it came up on a podcast episode.

Karina Nguyen (01:09:10):
Oh, nice. Yeah, so it is a very cool product where you can just call anyone at any time and then share screen and the other person can have access to the screen or start literally operating your computer. And it's very realtime... The allegiance is very... it's very high quality. And it's just like I kind of want the same. I want to pair program with my model and the model should even talk to me. Draw very specific section in my code and just go to tell me... Obviously teach me and we can have different modes. It's like right, this is a product right here for you. I don't know. Some people should build that. 

Lenny Rachitsky (01:09:58):
It sounds like a startup just got birthed-

Karina Nguyen (01:09:59):
Yes.

Lenny Rachitsky (01:10:00):
... from someone listening to this. You mentioned that it's very hard to do this agent controlling a computer as you and helping out. What makes it so hard for whatever, however much you can explain briefly?

Karina Nguyen (01:10:11):
Much of it is because right now the model's operating on pixels instead of language or whatnot. Pixels is actually really, really hard. The models [inaudible 01:10:25] perception, or visual perception. I think there's still a lot of multimodal research that's going on, but I think language scaled so much easier compared to multimodal because of that.

(01:10:38):
Another thing that I guess my team is working that is how do you derive human intent very correctly? It's like sometimes does the model know enough information to ask a follow-up question or to complete the task? You don't want an agent to go off for 10 minutes and then come back with an answer that you didn't even want. That actually creates much more worse user experience. And this comes with teaching the model people skills. It's like, "What do people like? Kind of like creating the mental model of the user and care about the user in order to ask certain questions. Actually, that part is hard to do for the models.

Lenny Rachitsky (01:11:28):
That relates to what we talked about earlier where this kind of the soft skill, people skills piece is not where these models are strong yet.

Karina Nguyen (01:11:34):
Yeah. 

Lenny Rachitsky (01:11:35):
Okay. I'm going to skip the lightning round. I want to ask just one question from the lightning round, something fun. 

Karina Nguyen (01:11:41):
Yeah. 

Lenny Rachitsky (01:11:44):
Okay, so when AI replaces your job, Karina, I'm curious what you're... And it gives you a stipend, gives you a monthly stipend. Here's your salary for the month. What would you want to do? What do you want to spend your time on? What will you be doing in this future world?

Karina Nguyen (01:11:57):
I've been thinking about this a lot times. I feel like I have a lot of jobs options. I would love to be a writer, I think. I think that would be super cool. You should write short stories, sci-fi stories, novels. I really like art history, so you know those conservationists in the museums who just try to preserve art paintings, but just painting through a long day? 

Lenny Rachitsky (01:12:28):
Mm-hmm. 

Karina Nguyen (01:12:29):
I think that would be really cool to do. Yeah. 

Lenny Rachitsky (01:12:36):
That sounds beautiful.

Karina Nguyen (01:12:36):
I don't know.

Lenny Rachitsky (01:12:39):
What I'm hearing is you need to Nerf these models to not get very good at writing so that you can continue... Although at that point you don't need to do it from... You don't need people to buy it, you're just doing it for fun, so it doesn't even matter if they're incredibly good at writing or art conservation. Oh man, what an episode of our conversation. What a wild time we're living in. Karina, thank you so much for being here. Two final questions. Where can folks find you online if they want to reach out and follow up on anything? And how can listeners be useful to you?

Karina Nguyen (01:13:06):
You can find me, I'm on Twitter it's KarinaNguyen. You can also shoot me an email on my website. And my team is hiring and so I'm looking for research engineers, research scientists, as well as machine learning engineers, people who come from product engineers who want to learn model training. I'm actually hiring for my team. My team is called Frontier Product Research, and we train models, we develop new methods but for product oriented outcomes.

Lenny Rachitsky (01:13:38):
What a place to work. Holy moly. What's the best way for people to apply for these very lucrative roles?

Karina Nguyen (01:13:46):
I think you can shoot me a DM on Twitter.

Lenny Rachitsky (01:13:49):
Okay. 

Karina Nguyen (01:13:51):
Or I'm yet to create a job description for them.

Lenny Rachitsky (01:13:51):
Okay. This is the job description.

Karina Nguyen (01:13:58):
Or you can apply into post training team. Yeah.

Lenny Rachitsky (01:13:58):
Okay. You're going to get a flood of DMs. I hope you're prepared. Karina, thank you so much for being here. This was incredible.

Karina Nguyen (01:14:03):
Thank you so much, Lenny.

Lenny Rachitsky (01:14:05):
Bye, everyone. 

Karina Nguyen (01:14:05):
It was fun. 

Lenny Rachitsky (01:14:09):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at LennysPodcasts.com. See you in the next episode.

