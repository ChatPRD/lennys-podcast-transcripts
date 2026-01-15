---
guest: Garrett Lord
title: Inside the expert network training every frontier AI model | Garrett Lord
youtube_url: https://www.youtube.com/watch?v=0qdR-XwHJ9o
video_id: 0qdR-XwHJ9o
description: 'Garrett Lord is co-founder and CEO of Handshake, which started as a
  career network for college students and new grads but recently discovered something
  extraordinary: they were sitting on the...

  '
duration_seconds: 4191.0
duration: '1:09:51'
view_count: 15322
channel: Lenny's Podcast
keywords:
- growth
- retention
- acquisition
- onboarding
- metrics
- kpis
- user research
- iteration
- analytics
- conversion
- revenue
- hiring
- culture
- management
- strategy
---

# Inside the expert network training every frontier AI model | Garrett Lord

## Transcript

Garrett Lord (00:00:00):
There will never be a time like this. I've never seen anything like it. I doubt I'll ever feel anything like this in business again where there's unlimited demand. How do you make sure that three months from now, six months, you have no regrets? Get on the plane to go talk to a customer, make the late night push, check the data six times over again.

Lenny Rachitsky (00:00:15):
Your company creates new data to continue advancing the intelligence of models. This is a business that you built on top of a business you've already had. 

Garrett Lord (00:00:24):
We're the largest expert network in the world. We have this massive strategic advantage, which is like no customer acquisition costs. The only moat in human data is access to an audience. 

Lenny Rachitsky (00:00:33):
You guys come in after the model's trained to tweak the weights based on additional data that you you've created. 

Garrett Lord (00:00:38):
The models have gotten so good that the generalists are no longer needed. What they really need is experts. 

Lenny Rachitsky (00:00:44):
There's this tension between all these students training models to become smarter, and then there's that they will have harder time potentially finding jobs. 

Garrett Lord (00:00:52):
That's not what we're hearing from our employers, this is just enabling human beings to be even more productive. You used to put a Google Search on a skill on your resume because you grew up with Google. Being AI native, young people are at a huge advantage.

Lenny Rachitsky (00:01:05):
Today my guest is Garrett Lord. Garrett is the co-founder and CEO of Handshake, which is one of the most interesting and incredible AI success stories that you probably haven't heard of. Handshake has been around for over 10 years, they're essentially LinkedIn for college students, it's a place for students to connect with companies to find a job. They are the platform of choice for every single Fortune 500 company. Over 1,500 colleges, over 20 million students and alumni, and over 1 million companies use them to hire graduates. At the start of this year, Garrett and his team realized that their huge proprietary network of students, including tens of thousands of PhDs and master's students, is extremely valuable to AI labs to help them create and label high quality training data. So, they launched a new business from zero to one in January. Four months later, they hit 50 million ARR. They're now on pace to blow past 100 million ARR within just 12 months. They'll exceed the revenue that they're making with their decade old business in under two years. 

(00:02:04):
This is a truly incredible and rare story, and one that I think a lot of teams can learn from because AI is creating a lot of opportunity but also a lot of potential disruption, and this is an amazing story where the company basically disrupted themselves. This episode is packed with insights, including a primer on what the heck are people actually doing when they're labeling and creating data to train models? A huge thank you to Garrett for making time for this, his wife just had a baby this week. He's also in the middle of scaling this insane new business. So thank you, Garrett. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. 

(00:02:39):
Also, if you become an annual subscriber of my newsletter, you get a year free of a bunch of incredible products, including Lovable, Replit, Bolt, n8n, Linear, Superhuman, Descript, Wispr Flow, Gamma, Perplexity, Warp, Granola, Magic Patterns, Raycast, ChatPRD, and Mobbin. Check it out at lenny'snewsletter.com and click bundle. With that, I bring you Garrett Lord. 

(00:03:01):
This episode is brought to you by CodeRabbit, the AI code review platform transforming how engineering teams ship faster with AI without sacrificing code quality. Code reviews are critical, but time-consuming. CodeRabbit acts as your AI co-pilot, providing instant code review comments and potential impacts of every pull request. Beyond just flagging issues, CodeRabbit provides one click fix suggestions and lets you define custom code quality rules using AST GREP patterns, catching subtle issues that traditional static analysis tools might miss. CodeRabbit also provides free AI code reviews directly in the IDE. It's available in VS Code, Cursor and Windsurf. CodeRabbit has so far reviewed more than 10 million PRs installed on 1 million repositories, and is used by over 70,000 open source projects. Get CodeRabbit for free for an entire year at coderabbit.ai using code Lenny. That's coderabbit.ai. 

(00:03:58):
This episode is brought to you by Orkes, the company behind Open Source Conductor, the orchestration platform powering modern enterprise apps and agentic workflows. Legacy automation tools can't keep pace, siloed low-code platforms, outdated process management and disconnected API tooling fall short in today's event-driven AI-powered agentic landscape. Orkes changes this. With Orkes Conductor, you gain an agentic orchestration layer that seamlessly connects humans, AI agents, APIs, microservices, and data pipelines in real time at enterprise scale. Visual and code-first development, built-in compliance, observability and rock solid reliability ensure workflows evolve dynamically with your needs. It's not just about automating tasks, it's orchestrating autonomous agents and complex workflows to deliver smarter outcomes faster. Whether modernizing legacy systems or scaling next-gen AI-driven apps, Orkes accelerates your journey from idea to production. Learn more and start building at orkes.io/Lenny. That's O-R-K-E-S.io/Lenny.

(00:05:04):
Garrett, thank you so much for being here. Welcome to the podcast. 

Garrett Lord (00:05:07):
Yeah, thanks for having me. A long-time subscriber.

Lenny Rachitsky (00:05:09):
I appreciate that. Okay, so before we get into the insane trajectory that your data labeling business is on, which is just an amazing story that I think a lot of founders and product teams that are trying to navigate this AI disruption that's happening will have a lot to learn from. I want to first help people understand what the hell data labeling actually is. Just like, what are people actually doing? Why is this so valuable? Some of the most, I don't know, fastest-growing companies in the world today, including you guys are just, this is what you do. Clearly there's something really important here. I sort of understand it, probably not really. I think a lot of listeners feel the same way. So let me just ask you this, what is data labeling actually? What are people actually doing? And then, just why is this so valuable to frontier AI labs?

Garrett Lord (00:05:55):
Yeah. So, I think it's helpful to take a step back of what does training a model look like? So, there's really two primary functions. There's a pre-training and a post-training process in training a model, and for a long time these AI providers, or LLMs, or Frontier Labs we're focused on basically sucking up more and more information on the pre-training side of the house. And that's basically the entire corpus of written human knowledge. So, that's not just written, but every YouTube video, every book, basically the pursuit of sucking up everything that was on the internet, and that was the pre-training side. And there was a lot of gains from pre-training, like models continue to get better. And about 18 months ago, 24 months ago, we started to really see an asymptoting of gains coming from, because they had essentially sucked up all of the knowledge on the internet. And so, labs really shifted towards most of the gains now coming from the post-training side of the house. 

(00:06:50):
And what post-training is, is it's augmenting and improving the data they have across every discipline or capability area that they care about. So take coding, or mathematics, or law or finance, they are focused on collecting high quality data that really improves the state of our capabilities, their models, and you can see a lot of these popular benchmarks on what are called model parts. When Llama IV is released, you'll see the benchmarks across various domains, and each one of the research teams inside of the labs have different use cases. Basically they're running experiments, almost think like the scientific process. They have a hypothesis around how to improve the model. They're trying to collect small pieces of data to see if that hypothesis works out. If that hypothesis is proving true, then they expand the overall collection of the data in that advert. And it could look like reinforcement learning environments, it could look like trajectories, it could be audio and multimodal, it can be text-based like prompt-response pairs. 

(00:07:58):
It can also be reinforcement learning with human feedback, which is like preference ranking data. And so, that's the state of the art of models. And most of the gains that are happening from models right now are coming from the post-training side of the house. And there's just an incredible amount of demand to stay at the absolute frontier of where models are going.

Lenny Rachitsky (00:08:20):
So training, pre-training is feeding it, say the entire internet. Here's like all the data that the humans have ever created, figure out knowledge and facts, and how to reason and all these things. Post-training, is it correct to say there's essentially two buckets of things to do? There's reinforcement learning, human feedback RLHF, and then there's kind of this bucket of fine-tuning?

Garrett Lord (00:08:41):
I mean, yes and no because take for example trajectories, or you want to be able to do, people use flight search or an accounting end-to-end process, or you want to be able to conduct biological experiments, you need actual trajectory data. There's still very much, a lot of the labs are still, they have points of view on what data collect. It's evolving very quickly. But I think reinforcement learning is really preference ranking, like which question do you like more, question A or question B? SFT data is a prompt and a response, and obviously the labs are very focused on these thinking or reasoning models. So, in order to improve a reasoning model you need to actually have the step-by-step instructions, of which when you interact with a lot of these frontier models they struggle in very advanced domains. And so, I think there's a variety of data that they're working with to improve capabilities in their models.

Lenny Rachitsky (00:09:39):
What I'm hearing is there's other ways to post-train. Which of these are you guys focused on? Where do you help models most of these three-ish buckets?

Garrett Lord (00:09:48):
Our real unique proposition as a business is the fact that we have an engaged audience. We have 18 million professionals across, we have 500,000 PhDs, we have 3 million master students, we're a global platform. And so, depending on what you're looking for across any area, academic knowledge, what is the definition of a PhD? How do you get your PhD? You defend your thesis. Defending your thesis means, generally speaking, you have proven that you have extended the world's knowledge in a particular domain. And so, the ability to hyper-target this audience into chemistry, math, physics, biology, coding and really touch parts of human knowledge that have never before made it to the internet is really where we excel. And I would say that when you talk about the labeling market, something to make it more abstract is like it used to be generalists' work. 

(00:10:52):
A lot of the market before the model started to get better was leveraging talented international lower cost labor to do basic generalist tasks. But really what's happened is the models have gotten so good that the generalists are no longer needed. What they really need is experts, experts across every area that the models are focused on. And really, you could think about these model builders as they're focused on the most economically valuable capability areas in the economy. And so that, generally speaking, right now is focused on advanced STEM domains, advanced science and math domains, and then the derivative functions of accounting, law, medicine, finance, where they want to make the models more capable. And then the work that we're doing, I think to come full circle to your question, we're doing work across so many domains. I mean, we have millions of bachelor students that are being used for work in audio, work in customizing a model depending on the voice and tone, where you are geographically in the country, what do women versus men prefer? All the way to the most advanced PhD STEM domains out there.

Lenny Rachitsky (00:12:08):
Okay. So, is it fair to say essentially all the data that is available has been trained on, and your company creates new data, new knowledge to continue advancing the intelligence of models?

Garrett Lord (00:12:22):
Yep. And I also say we help point out where the models are weak. So, in order to break a model, it's pretty tough for the average person to break a model and get an incorrect response. But if you are a PhD in physics, you can go in multiple subdomains of physics and prove where the model's actually breaking, either breaking in its reasoning steps or it's where it's broken in its ground truth right answer, or we start throwing tools in there or needing to follow some step-by-step process. And I wouldn't say it's easy for them, but the average person cannot break the models and that's where we really come in.

Lenny Rachitsky (00:13:03):
So, essentially it's just catching mistakes that the model has made. Okay. So, what are these people actually doing? I know there's all kinds of different types, you described all the ways that data's generated, what kind of data is useful? So, maybe just the most common examples. Let's say a PhD person is sitting there doing stuff, what are they actually doing?

Garrett Lord (00:13:22):
A great example is a public paper called GPQA. So, for the engineers out there that want to read about it, essentially the crux of the paper is you break the model, you provide a ground truth, the right answer to the question, you provide the step-by-step a reasoning steps. So, you might imagine because models are non-deterministic, the model can get the answer right once, but it might not get the answer right three out of five times. So, you actually prove where the model's failing. You actually break down into where is it failing? Maybe it can get, it knows the question, it can get the right answer, but the actual steps to get there are wrong and they really focus on the steps to get there. Say there's 10 steps in a math problem, step 6 through 10 is wrong. So, how do you fix the actual steps? 

(00:14:11):
And what are they doing? So they're going in, we're really focused on calling this branding the experience and treating people like experts. PhD students expect to be treated different than a lower cost international labor with a different work expectation. And so, these PhDs come into a community, we have a instructional design team and an assessments team that's going through and basically iteratively helping them understand how to use the tools that we built, and how to interact with the latest models. Then they go in and start actually creating data. And that process is, on our side the model builders, they want to know that the data we're producing is high quality. Som we have our own research team, our own post-training team. 

(00:14:53):
I hired a gentleman from Meta that went along on the post-training over there, and I-

Lenny Rachitsky (00:14:57):
Hope you paid him well. 

Garrett Lord (00:14:59):
Yeah. So, war for AI talent is very expensive, but super, super privileged and proud to be working with him. And so, each unit of data, we have to build it an environment for them to actually create the data. Then we have to understand in a unit level we're trying to approximate the actual gain from that piece of data and whether it can improve in a particular capability area. And then, we're also focused on evolving the use cases to also follow what the model builders want, which is they want more more real world tool use and trajectory based data as well.

Lenny Rachitsky (00:15:33):
Okay. There's so much here, and we could go infinitely down here but I think that this is really interesting because just like people hear so much about all of this and they barely understand what the hell it actually is. So, this is for me really interesting. I think it's going to help a lot of people. So essentially a PhD, say a biologist, biology PhD is just their job is find flaws in what, say ChatGPT is producing, and then come up with here's the correct answer. And that is used to fine tune the mode, here's something you are doing incorrectly, here's the correct answer and that improves the model.

Garrett Lord (00:15:33):
Yep. 

Lenny Rachitsky (00:16:03):
Is that a simple way to think about it? And please correct anything I'm saying that is incorrect because I don't want people to misunderstand it.

Garrett Lord (00:16:08):
Yeah. I mean, a great example, let's take a non-verifiable domain like education. So there's a PhD student, Rachel on the network, she got her PhD from the University of Miami, spent two decades as a teacher teaching students in the eighth grade. And she was an adjunct professor at a local community college in the field of education. And so, she is interacting with the state-of-the-art models in educational design. So, actually trying to understand what is the best way to teach people, and how do you spot incorrect issues in a model in the way that they're training people, and help the models understand the forefront of educational design with the hands-on experience of being an eighth grade teacher for 10 plus years and having a PhD in education? So, that's an example of you can have that all the way down to a verifiable engineering problem that you're seeing the latest models fail on.

(00:17:12):
Yeah, I think that gives you the gamut. You also have, we talk about professional domains like these reinforcement learning environments, there's a bunch of papers out there that basically speak to people narrating over their step-by-step tool use. So, as they go to solve a problem from start to finish, interact with multiple different service areas, interact with multiple different tools, they're like, there's papers that talk about this, talking over what they're doing, actually following and screen recording where their mouse is going, how they're problem solving. When they run into a roadblock, what do they do? So, they really want to understand how humans think.

Lenny Rachitsky (00:17:50):
You mentioned this term trajectory. Can you just explain what that actually means? Because it feels like you've mentioned that a few times and that feels important to all this.

Garrett Lord (00:17:56):
Yeah. A trajectory is basically just like the entire environment that is collecting what you're doing. So it's your screen, it's your mouse-

Lenny Rachitsky (00:18:04):
Oh, I see. Oh, wow. 

Garrett Lord (00:18:05):
Yeah. 

Lenny Rachitsky (00:18:06):
Including this voiceover, okay. And then, this might be too technical, but what is the output of all this work? This, say teacher, is it just like a JSON file, an XML file, like a text file?

Garrett Lord (00:18:15):
Yeah, it can be managed JSON data.

Lenny Rachitsky (00:18:17):
JSON data? Okay. 

Garrett Lord (00:18:18):
And then, we also have multimodal work like audio, like classifying music and understanding ... We're engaging thousands, or not thousands, probably hundreds of top music students at the music schools in the country who are improving models of understanding of music. And you also have the thing called, which we haven't talked about here, a rubrics, and rubric models are, you can put a model in as a judge. What is a good educational design, or what's a good MRI result? In some of these domains, you actually don't have a guaranteed correct right answer. And so, models can sit in the middle as a judge and actually understand what is ... Think back on your school days. How do you get A on your 5,000 word paper? Well, there's a great introductory statement and there's scientific proof. So, you can build a rubric that allows a model to sit in the middle and actually auto-evaluate responses. We're seeing a lot of rubrics work as well. 

Lenny Rachitsky (00:19:28):
And you would think, why would you trust this one teacher's opinion that this is the right way to do it? But what's cool is the market speaks for itself. If these models are being used more and more, and people love them and value them, I imagine steps in between to verify this is good and other people think this is a good idea. It feels like the market dynamics will tell you if the data you're providing is correct at what people want. Is there something more there?

Garrett Lord (00:19:52):
I didn't get a PhD in AI, or math, or physics, and I haven't trained myself, we have frontier models, but there is a lot to each unit of data whether it's improving. There's a ton of science and research out right now around how do you make sure that the data that you're producing is improving the model? And it's very hard for model builders to understand. They really care about, to zoom out, they care about three things. They care about quality first and foremost. You have to have high quality data. And if you imagine you're training a model, like teaching a student and you're giving it the wrong data, it's extremely challenging to overcome that. So, quality is first and foremost. And then, the other huge problems you have is volume. How do you generate thousands of pieces of data in the most advanced domains of chemistry, and mathematics, and physics, and how do you ensure that it's high quality?

(00:20:48):
Well for us, say in physics, we just reach out to students at Stanford, and Berkeley, and MIT, and they're at the top GPA at the best physics schools in the country. And so, our ability to get to scale or volumes of data, to produce very high quality data, is something they care deeply about. And then, the other thing I would say model builders care about is speed, because they have all these hypotheses and they're constantly testing different pipelines. And so, you might have three or four bets going at once, and then as soon as one is actually showing a gain, imagine you're a researcher or you're assigned to the processes, once you're running a gain then you're trying to grow that pipeline and grow that piece of data that's actually improving it, and you're maybe ditching two or three other projects you had that weren't showing improvement. 

(00:21:31):
So, your ability to quickly turn around for them in a period of days, and then get to high volumes of data that are high quality is the number one thing they care about. And so, there's quite a bit of technology we built on our side to assess each unit of data. We have our own post-training teams, we're renting our own GPUs, and we're trying to make sure that we can sit directly with these researchers and help share what we're seeing with the data that we're creating and how it could improve their model, how they could best train with it. So, hopefully that helps.

Lenny Rachitsky (00:22:03):
Going back to the types of post-training, just because I think this might be helpful, at least for me the mental model of there's pre-training, there's post-training, within post-training there's reinforcement learning, human feedback, there's this concept of fine-tuning. There's also evals and stuff like-

Garrett Lord (00:22:03):
There's SFT, yeah. 

Lenny Rachitsky (00:22:19):
SFT, which is supervised fine-tuning? Is that-

Garrett Lord (00:22:22):
Yeah.

Lenny Rachitsky (00:22:22):
Yeah. So, the stuff you've been describing, would you mostly describe that as supervised fine-tuning?

Garrett Lord (00:22:29):
Yes, and we're doing all of the above. We don't do the auto eval, we produce rubrics which are used auto evals. But yeah. 

Lenny Rachitsky (00:22:39):
Okay, awesome. So essentially there's a model, it's trained on all this amazing data. You guys come in after the model's trained to tweak the weights based on additional data that you create. What's interesting is that this is a scalable system. I want to talk about just the supply of amazing people that you have producing this, but it's amazing that humans can do this. You would think it needs to be this infinitely scalable thing, but humans sitting there creating data is working and improving the intelligence of models significantly.

Garrett Lord (00:23:13):
Oh, yeah. I mean, I think maybe a funny joke is all the MBAs think this is all just going to go away. And I think for as long as models are improving, humans will be needed in this process. And when you talk to the lead scientists and researchers at these labs, it's like the data types will evolve and what they're trying to capture and collect, but there will be humans needed in the space for the next decade until we reach full ASI. So yeah, I mean, you think about in a lot of them will struggle to do basic trajectories right now. So, right now people are very focused on academic domains, and I think they'll continue to be focused on academic domains, but there will also be far, far more demand for professional domains as well across basically every trajectory or step-by-step problem that a knowledge worker solves in the workplace, it's the pursuit of these labs to make sure that they're trying to collect the data to help add as much value in that process for humans as possible. 

Lenny Rachitsky (00:24:17):
So, let me ask you about this. There's this tension, I imagine, people might feel between all these students training models to become smarter, and smarter, and smarter, and then there's that they will have harder time potentially finding jobs if models are so smart that people at entry level aren't being hired as much. How do you think about just that tension? Do you think this is a real problem or not, or do you think this goes-

Garrett Lord (00:24:42):
I'm probably in the camp of like GDP growth over universal basic income. I very much believe that this is going to improve and accelerate every human's ability to create an impact in the economy in the world, and that we're hearing from, there's like a million companies that use Handshake. 100% of the Fortune 500 uses Handshake, so we basically power the vast majority of how young people find jobs, and a lot of people are hyperbolic at saying that all young people won't have jobs, and that's not what we're hearing from our employers. What we're hearing is pick social media marketing, before you needed somebody that could do Photoshop, and take pictures, and create the videos. Then you needed somebody that understood marketing analytics platforms to track your posting on different social media forms. It's like now one person, one young, talented, AI native, Iron Man suit enabled young person can get on and they can build their own videos, produce their own creative assets, post across multiple social media platforms, run all of their own analytics. They don't need a data science degree to be able to do that.

(00:25:47):
Or take an intern in our company, he had his first PR up I think the afternoon he started. You were a PM, you realize how challenging that would've been historically to get your dev environment set up and figure out where to add value. You just took a bug and squashed it. And so, I'm really a believer this is just enabling human beings to be even more productive and create more impact. And yeah, of course, hundreds of millions of jobs, the jobs will evolve. People will become displaced, they'll have to upscale and rescale, and I think Handshake has a huge role to play in helping knowledge workers evolve.

Lenny Rachitsky (00:26:24):
This has come up a couple of times this point that I think is really good, that younger people coming out of school are actually going to be much more likely to be successful because they're growing up with these tools, and are much more native to all these advanced tools and so they just come in as beasts just doing so much more.

Garrett Lord (00:26:42):
Well, do you remember when, this a little bit predates me, but you used to put Google search on as a skill on your resume. You were person, you were good at Googling, because you grew up with Google. It's like I think being AI native and having your Iron Man suit on, and understanding how to leverage these tools is like young people are at a huge advantage.

Lenny Rachitsky (00:27:03):
Yeah. And especially if they're involved in training these models, I imagine there's some other cool advantage there. 

Garrett Lord (00:27:08):
Yeah. Well I mean, just to hit on that, what we're hearing from our thousands of fellows is they're in the classroom, they're actually producing research. We're talking about PhDs at the top institutions in the country. They can make 100, 150, $200 an hour in their area, in their field of expertise. It's pretty sweet. You can make 25 bucks an hour being a teacher's assistant, or you can actually make $150 an hour breaking the latest models, and what we're hearing from our fellows is they're bringing a lot of those insights into the classroom to help them be more effective at teaching. More importantly, they're starting to learn how to leverage these tools to actually advance their area of research. So, they believe that these tools can help them advance their area of research by helping them be more effective with their time. And so, it is quite cool to get paid to learn a skill.

Lenny Rachitsky (00:27:58):
Before I get to the story of how this all emerged, because that is an incredible story, is there anything else about this whole field of labeling, of reinforcement learning that you think people just don't fully understand or you think that is really important? There's just so much happening. Like I said, some of the fastest growing companies in the world are in the space, Scale was just acquired for 30, sort of acquired for $30 billion. Just what else is there, if there's anything, that you think people need to understand?

Garrett Lord (00:28:26):
Generally speaking, anytime that you're interacting with a model and you're asking it to do really advanced things, and it's not performing your expectations, like somewhere there's probably an expert that is the top mind in that domain working directly for the best researchers in the world at the Frontier Labs trying to understand and go through the scientific iteration process of how to make that better. And that the assumption there is that they already have the entirety of human knowledge that's written and recorded. And so, for as long as there are problems in solving any problem with AI, any human problem, there will need to be humans in the loop helping advance that. And models don't generalize. I mean, obviously the field will advance a lot and the type of data they'll collect will evolve a lot, but it's pretty exciting at the frontier. 

Lenny Rachitsky (00:29:20):
Kevin Wheel was on the podcast, the CBO at OpenAI, and he made this point that really stuck with me that the model of today is the worst model you will ever use. 

Garrett Lord (00:29:29):
I love that line. 

Lenny Rachitsky (00:29:30):
Will only get better, just boggles the mind, and now we know why things are getting better because all the work you guys are doing. Just one quick question on this whole scale thing, I guess they were, I don't know, the main company doing this, now they're swallowed up and Alex is running superintelligence in Meta. Are they still a big player in this labeling space or are they out of it and that's a big opportunity?

Garrett Lord (00:29:50):
Yeah. I mean, kudos to the whole Scale team, a lot of respect for what they built, just many great companies operating the space. I think to the core of your question, I think if you viewed your research team and your model building team, and the experiments they're running to be really the cornerstone of how you're improving, you probably wouldn't want the latest research of what you're trying to work on being invested in by a peer. I mean, that's just generally what we hear in this space. And so, we have seen an incredible search and demand, and are I think extraordinarily well positioned. We like to say the only moat in human data is access to an audience. Basically, there are many, many small players in this space, some midsize players in the space, and they're basically running TikTok ads, running Instagram ads, paying money for Google Search display ads, YouTube ads, and they will be like, "Can you get me 200 physics PhDs?"

(00:30:58):
What do they do? They only can do one thing. They have 100 recruiters on staff, they all get on LinkedIn, they all send messages, they spend a couple million bucks on performance advertising campaigns. Somebody's scrolling their Instagram feed that's a physics PhD of which you can't target them that well and they like see, "Come train a model." It's like, "I've never heard of this brand before." The huge advantage that we've had and why we've resonated so fast in the marketplace is we built a decade of trust with 18 million people, and they trust us, and we built a ton of brand affinity, and they use Handshake, and they have an active profile, and we have a ton of information around their academic performance and what they've done in school. And so, we're able to really target people really effectively, and get to scale and volume of high quality data faster than anyone else. And I think that competitive advantage of access to an audience is really resonating in the marketplace. 

Lenny Rachitsky (00:31:49):
Today's episode is brought to you by Anthropic, the team behind Claude. I use Claude at least 10 times a day. I use it for researching my podcast guests, for brainstorming title ideas for both my podcast and my newsletter, for getting feedback on my writing and all kinds of stuff. Just last week I was preparing for an interview with a very fancy guest, and I had Claude tell me what are all the questions that other podcast hosts have asked this guest so that I don't ask them these questions? How much time do you spend every week trying to synthesize all of your user research insights, support tickets, sales calls, experiment results and competitive intel? Claude can handle incredibly complex multistep work. You can throw a 100-page strategy document at it and ask it for insights, or you can dump all your user research and ask it to find patterns. With Claude 4 and the new integrations including Claude 4 Opus, the world's best coding model, you get voice conversations, advanced research capabilities, direct Google Workspace integration, and now MCP connections to your custom tools and data sources. Claude just becomes part of your workflow. 

(00:32:53):
If you want to try it out, get started at Claude.ai/Lenny, and using this link you get an incredible 50% off your first three months of the pro plan. That's Claude.ai/Lenny. 

(00:33:06):
Okay, this is an awesome segue to where I wanted to go, which is just how this business emerged. This is a business that you built on top of a business you've already had. From what I understand, you were at like $150 million in revenue, you've been at this for a long time. You found this opportunity, and now that looking back it's like obviously this is an amazing idea, labs need data, you guys have the supply of incredible experts. What an opportunity. Talk about just how you first realized this was something that you could be doing, and should be doing, and then how you started to execute down this path.

Garrett Lord (00:33:40):
Yeah, I think it's been a pretty natural extension from helping people jumpstart, restart or start their career. Monetizing your skills and this new employment ecosystem is going to look very different in the future, and to zoom into how we discovered it, it's like because we have such a large access to this audience, and as the world shifted from generalists to experts, we're the largest expert network in the world. We have more PhDs, 500,000 of them use Handshake than any other platform. We have three million master students who are in school or alumni. And so, we started to see all what I would call middleman companies reaching out to us saying, "Can we recruit your PhDs and master's students?" And like any great marketplace we started sending them to these different platforms, and started to really realize that from hearing from our users that the experience was really frustrating. 

(00:34:38):
Training was very transactional, it was very amorphous how you could get paid. There was immense amount of drop-off in the process to actual project like completion on these other platforms. So, we started to think the company was making tens of millions of dollars from helping these other platforms, and we started to realize what really kicked it off was hearing also from the Frontier Labs, they started to reach out to us and started to go direct and trying to almost cut out the middleman. And we started to realize, well, we could really serve our fellows, our PhDs, our experts, we could treat them. We just believe there will need to be a platform, an experts first platform in the pursuit of ASI and advancing AI, and there will need to be a place that everyone in the world could go to, to monetize their skills and their knowledge as these labs are focused on improving in all these multidisciplinary. And yeah, we entered the business in, really I started doing it over Christmas and New Year's. That's when I started flying around.

(00:35:48):
My family thought it was a little wild that I was on planes trying to chase different leaders, but we built an incredible team of people that came from the human data world, and really started building out our platform in January, and then started really monetizing the relationships about five months ago. Fast-forward to today, we're working with seven of the Frontier Labs, basically every lab that's doing work and building the best large language models, and the team has exploded and revenue's exploded, and it's been really a incredible ride running back new company inside of a company for the second time over again. 

Lenny Rachitsky (00:36:28):
And just to share some numbers, tell me if this is correct or if you're sharing these, but I heard that you hit 50 million in revenue just four months into this? Today we're at eight months in and you're on track to hit $100 million in revenue in the first year.

Garrett Lord (00:36:43):
I think we'll blow through that number, but yeah. 

Lenny Rachitsky (00:36:44):
Okay. Incredible. And I didn't even know there were seven Frontier Labs, that's-

Garrett Lord (00:36:49):
Zero to 50 is pretty good in four months, I think. 

Lenny Rachitsky (00:36:51):
Think zero to 50 million in four months, that's something. It's like the bar has been shifting constantly. A year ago that'd be legendary. Now it's like, all right, well another one of these. 50 million in four months, no big deal. It's truly insane. Just to zoom out one second, for people that don't know a ton about Handshake, the original business, what was that? What was actually this network that you had, that you sat on top of?

Garrett Lord (00:37:18):
Yeah, that network does about 200 million. This will do about [inaudible 00:37:21]

Lenny Rachitsky (00:37:18):
200 million.

Garrett Lord (00:37:18):
Yeah. 

Lenny Rachitsky (00:37:18):
Okay. 

Garrett Lord (00:37:20):
So, we have 600-ish super passionate teammates that work on the core business, which I would separate those. These aren't two businesses, I think it's one business, but what is that business? If you're a young person in America that's graduated in the last five, six, seven, eight years, you probably have Handshake on your phone. You definitely know what Handshake is. It's a verb with young people in America, it's a verb with people that are in college in their PhD or master's program, and it is, I call it an unconnected graph, meaning you don't need to ... LinkedIn is very focused on who you know and what your experience is. The first question on LinkedIn is what's your job? And a lot of young people start off, they've never had a job before. They don't have 500 connections to add to their graph. 

(00:38:13):
Whereas on Handshake, you start off trying to discover, and explore, and figure out how to navigate through school and figure out, "Oh, I'm an engineer. Maybe I want to be a PM, maybe I want to work at a startup, maybe I want to go to a larger company." What are the pros and cons you want to learn from your peers and young alumni? And so, Handshake's this I call a very social platform with groups, and messaging, and profiles, and short-form video and feed, all focused on your interests and helping really build your confidence in your early career to find your first job, your second job, and to manage 18 to 30, I would say.

Lenny Rachitsky (00:38:49):
And how long has that business been around? 

Garrett Lord (00:38:51):
It's been around 10 years.

Lenny Rachitsky (00:38:51):
10 years, okay. So it's just again, it just feels like such a holy shit, you guys are in the right place in the right time with the right network that is extremely valuable now. What an interesting story. I feel like it's just another interesting example of you've been doing something for a long time and then all of a sudden AI is just, opens up a whole new way of leveraging something that you have been doing for a long time. It makes me think a little better about Bolt, and StackBlitz, which was building for seven years this browser based OS where you could run an OS in the browser. And they're like, "I don't know, no one needs this. What are we doing?" And then, all of a sudden AI and they're like, "Oh, what if we build AI apps in the browser and just generate products for you with AI?" And now it's, I don't know, one of the fastest growing companies in the world. 

Garrett Lord (00:39:36):
Yeah. 

Lenny Rachitsky (00:39:37):
So interesting. And so, I think this is just an interesting time for our people to think about what have we done that may give us a new opportunity to build something huge based on this unfair advantage that we have?

Garrett Lord (00:39:49):
I think also as your company grows in size and headcount, and maturity, it's also hard to incubate something new inside of a business. It's hard in so many ways. The way that you build zero to one, and find product market fit, and scale a team very quickly and is very different than the way that you run a more mature business that has been around for 10 years with hundreds, and hundreds, and hundreds of people. So, I've really had a ton of fun and found a ton of passion in running it back again for the second time inside the business. And then yeah, we have this massive strategic advantage, which is no cost or acquisition costs, and we have much higher conversion rates and retention than any of the other platforms by a large margin because we have such consumer affinity. 

Lenny Rachitsky (00:40:43):
There's actually two threads here I want to follow, I'm going to follow the second one first, this idea of where this data labeling work can come from. This isn't a really clear, simple, understandable one, which is just experts sitting there creating data. Another one that I know a lot of other companies in this space use Scale, I know especially with just like low-cost labor internationally. Are there other methods for doing this that isn't one of those two? How are other companies doing this?

Garrett Lord (00:41:10):
I think if you care about building a really high quality business, and having good gross margin and high quality growth, the ecosystem here is, one of the leading players, they have 200 recruiters. It's unsustainable. There are like 200 people on LinkedIn sending individual messages to acquire these people, because there's no brand, there's no trust. They're spending tens of millions of dollars a month on performance advertising, Google Ads-

Lenny Rachitsky (00:41:39):
To find experts and to find folks. 

Garrett Lord (00:41:41):
Find experts. 

Lenny Rachitsky (00:41:42):
And it's experts mostly at this point. 

Garrett Lord (00:41:43):
Yeah. And then they put them onto an experience that is treating them like they're drawing boundary boxes around stop signs in the Philippines. The frontier tax accountants don't want to be treated like low cost international labor, and I don't think anyone enjoys that process. And so, the ability to build a experience that's rooted in community, that's rooted in high quality training. If you're getting your PhD at MIT, chances are you're just not being taught well enough on how to use the tools.

(00:42:15):
It's not you can't break the models, it's just like the other platforms, they're spending thousands of hours to acquire an individual user and they're put right into a project with no training. So, we just started from day one at building this expert ... We believe there'd be a deep network effect here that's very connected to our core business of starting, jumpstarting or restarting your career. And you come in, you build a profile, you see the community, there's groups and a feed of here's how people are learning. You come into actual individual cohort with peers that look like you and have your similar background. You're being taught on how to interact, and there's a trial and error, and we have an instructional design piece so you can't do it. Then you're put on the projects where building ... There's certain swim lanes where we're actually pre-building data and selling that data to all the labs. 

(00:43:03):
So, we can do this thing where we produce one unit of data ourselves. We pay for it, almost like a movie production. We pay for a unit of data, and then we make sure it's very high quality. We run our own post-training on it, and then we produce a bunch of specifications of the data, and we actually sell that individual package of data to many different labs. And so, you get put on a project like that. Once you're doing a really, really good job on our projects, oftentimes then we'll put you on customer projects where they only want the best of the best people in machine learning. And then they go from our projects to their projects. And so, there's a huge customer acquisition. You love going deep on your podcast, so just to talk about it, it's like you really have a couple of things that matter.

(00:43:46):
You have a cost to customer acquisition, your CAC, and then you have your LTV, like the lifetime value of a user. And an LTV is calculated pretty simply in this business. It is based on the retention of a person, and how many projects they can participate in. So, if you treat people really well, you train them really well, well, A, we have no customer acquisition costs because we partner with 1,600 universities, power 92% of the top 500 schools in the country. We power almost every institution and community college in the country. We have no customer acquisition cost to acquire the people. We have a ton of brand and trust with them built up, so they convert at really, really high rates. And then, if you treat them really well, because what they expect from us, they know Handshake, their school buys Handshake, we care about treating these people well but the universities would not tolerate our partnership with these fellows unless we treated them well. 

(00:44:41):
So, you put them into this process where our LTVs and repeat engagement rate and retention rate on different projects is really high. And so, these structural advantages are quite significant when you contrast a leading provider that has 200 individual contributing recruiters, and are spending tens of millions of dollars a month on performance marketing. So, that's I think why we've seen so much success.

Lenny Rachitsky (00:45:07):
That's extremely interesting. And it feels like, as you said, there used to be a big focus on generalists, which is people anywhere in the world for low-cost can do the work, like draw bounding boxes around things. And essentially the market has shifted from low-cost generalists to experts. And a lot of these companies like Scale, we're optimizing for general work model training data, and you guys are set up to be extremely good at expert based data. And so, you're in the right place at the right time, at the right supply. What a business.

Garrett Lord (00:45:43):
Yeah.

Lenny Rachitsky (00:45:43):
Nice work.

Garrett Lord (00:45:44):
I would say it's not been easy building business two inside of business one, but-

Lenny Rachitsky (00:45:48):
Yeah. So, let me follow that thread. That's where I wanted to go. What was just that like? So, you started noticing that model companies were coming to your people, that people were having hard times with some of these other companies in this space and you're like, "Oh, maybe we should be doing this sort of thing"? How did that just initial inception start, and how did you start to explore that idea and to see if it was a real thing?

Garrett Lord (00:46:09):
Tactically we were working with many of the middleman companies doing work. We started to see the demand, as I talked about earlier. We started to see direct outreach from the Frontier Labs reaching out to us, trying to cut out the middleman in their pursuit of getting higher-quality data. When we started to put together the dots on we could build a way better experience for our fellows, we could serve them directly to the labs and build a direct customer relationship with the labs, and basically cut out the middleman. And provide a better experience to the labs, provide a better experience to our fellows and provide a better experience to our million companies in the network.

(00:46:48):
And you might think about just upskilling and reskilling, what's going to happen there. So, we walked into this space. We started in really December, exploring and learning more about it, like on expert calls and hammering down. I hired three expert firms, AlphaSights and GLG, and started doing a bunch of calls with the latest researchers, because we had resources. One of the cool things about being a larger company is our core business is $200 million ARR, so it's like we had resources to be able to accelerate the learning curve here. And then, we started working with arguably the number one lab about five months ago. 

Lenny Rachitsky (00:47:34):
I wonder who that is. 

Garrett Lord (00:47:35):
Yeah. 

Lenny Rachitsky (00:47:35):
Yeah, wonder who it is. 

Garrett Lord (00:47:39):
[inaudible 00:47:39] different answers working with the number one lab, and have just now we're working with Devin on the Frontier Labs and the number one thing we're trying to do is just focus on scaling up. And we've gone from four or five people working on this to 75 plus people working on it. I think we had 12 people start last Monday. It's like we are so bottlenecked on just meeting this opportunity, because in this market there's essentially unlimited demand. If you can produce high quality volumes of data, you most likely will be able to sell whatever you produce. And so on our side, it's like we're really focused on making sure that we pick the right longer term strategy, making sure that we don't grow too fast as to erode the trust that we've built up with these Frontier labs. Yeah, but it's been fun.

Lenny Rachitsky (00:48:38):
You said it's also been really hard to start those business within an existing business. What's been hard? What's been hardest? You touched on a couple of these elements already, but what else? 

Garrett Lord (00:48:50):
I think I just followed a lot more of my intuition around this, doing this. The story of Handshake was we had to sign up 1,600 universities, so I had to learn how to be the best ... We are the fastest growing higher education company in history. So, we signed up six 1,600 schools. Then we had to build an employer business, where we had to figure out how to sell the 100% ... All these Fortune 500 companies use it and 70% of it pay for it, so I had to learn about upmarket sales to Goldman Sachs, and General Motors, and Google and the biggest companies in the world, which is totally different than selling universities. And then we had to learn how to build an incredible student social network. What does the best feed look like? What does group messaging look like? So, I felt a little bit of familiarity in those zero to ones. 

(00:49:39):
Oftentimes marketplaces are like many zero to ones. Sometimes I dream that we just, I actually don't dream, but I make a joke that I just wish we were a cybersecurity company and we had one buyer and just one product, and it was just like we had to ... In a marketplace, you have to serve three different sides, you know from your time at Airbnb. And so, one of my learnings in spinning up these three different businesses in starting Handshake was I was pretty hands-on. So, everyone reported directly to me. I really said in a lot of meetings, "I'm not trying to be the boss, I'm just trying to get another smart guy in the room." We've hired an incredible team of people that have spent a lot of time in the space and have been big leaders at a lot of the human data companies in the space.

(00:50:27):
And so, everyone saw very clearly the structural advantages that we had, and a lot of the focus was on making sure that we could deliver high-quality data to one customer before we expand to anyone else. You had to say no to a lot of things. And then, you also had a lot of people in the core part of the business that, rightfully so, there's just checks and balances that there's a lot of people that try to get involved. Everyone wants to say, not everyone, this is a stretch, but it's easy to say no. It's easy to be like, "I can't prioritize that this week or this month. I have an existing set of priorities." So essentially, with the exception of a few things, everyone just came straight into this new org that I built, everyone did not have any responsibilities in the existing part of the business. It was extremely clear who was the directly responsible individual across each area of the new co. And now we've got deeper coupling and integration points across the rest of the business, but we sat in a separate part of the office. 

(00:51:35):
Everyone's in the office five days a week, a lot of weekends. There's a totally different expectation in hiring talent too, where it's like, "Hey, this is a 24/7 job. This is an early-stage company." The compensation was also different too, and based on hurdles in this new business so people felt owners creating the new co. And yeah, it's still extremely nimble, very, very flat. Just because you run one function doesn't mean you're the directly responsible individual on a project. We pick the best person who's most capable of driving an initiative forward, regardless of the function to be the DRI. We're a lot more metrics-oriented. When I built Handshake, we resisted this operating cadence for a long time, this weekly, monthly, quarterly operating cadence. With Handshake AI, we've been way more focused on operating with data, and metrics, and rigor from an early stage. There's a gentleman named Sahil on our team who's been doing an incredible job with that. Shout out Sahil, shout out young, shout out Paco. Yeah.

Lenny Rachitsky (00:52:42):
Okay, this is incredible. So, a few elements of what allowed this to succeed within a decade-old company. And by the way, so you're at 200 million a year in revenue with the traditional business. You're going to, as you said, blow past 100 million in the first year of this new business. So, it's wild that in the first couple years, if things continue to go this way, you'll exceed the run rate of a business that took you 10 years to build. Incredible. To make this successful, a few of the things I noted as you were talking, one is clearly you were just in founder mode. You're the lead of this new business. You weren't delegating it to someone, "Hey, go start this thing." You dedicated people, "Here, we're going to pick people. You have nothing else going on, this is your new job. You're going to work on this stuff." 

(00:53:28):
You worked in different part of the office. There's a metrics-based cadence. It's just like, let's stay really diligent about here's how it's going, here's where we're going, here's our track, here's our KPIs, things like that. Anything else there that you felt really important to making this work? Because a lot of companies are going to try to do this, I imagine, and so I'm curious what else you found important to make this work.

Garrett Lord (00:53:50):
Yeah. I mean, I just really believe in separate and everything. Separate engineering team, separate design team, separate accounts and operations team, separate finance team. Early on, everything was separate. People only had one job and one job only, and that was making Handshake AI successful. We had a couple integration points more, and I had an incredible executive team and a core part of business, and now there's becoming more and more involvement. But our executives that have built Handshake for a long time ran the core business, and I focused 80 plus percent of my time and attention on just this. And we hired an incredible engineering leader like Avery, who ... We have a lot of entrepreneurs, people that have started companies inside the company. Or pardon me, people that started companies before. That was huge. A lot of familiarity with hiring talent that have only worked at early stage companies so [inaudible 00:54:44] that feels super comfortable with ambiguity. 

(00:54:46):
We were also way more upfront around this is going to be chaotic. Just owning that narrative in front of all hands at the core company, owning it directly with the team. We have a separate all hands, we have separate onboarding, we have a separate recruiting team. I had some connection points, but mostly separate. And I think that was absolutely critical. We took some of the top people, I mean, we have great people in the core business, we took some great people from the core businesses and basically said, "Sorry, I know you love your old team. I know you love what you're doing. Will you join us in Handshake AI?" And they completely forego their historical responsibilities and came over. That became really critical with engineering when things started to scale and topple, and we're growing so quickly we took some of our top senior engineers, who were very entrepreneurial, and principal engineers, staff of engineers, parachute them in. It's been awesome to ask some of the most talented people in the core business like, "Hey, do you want to come over here and do this?"

(00:55:49):
And sometimes they say no. They're like, "I don't want to work most of the weekends." The number of 2:00 AM, 3:00 AM nights we done in this business, I mean, it's quite regular. People sometimes don't want to commit to that, but we've been up front, like here are the expectations for this team. It's an insane pace. If you want to be a part of one of the fastest growing businesses in Silicon Valley, you can join it. The ownership too has also been huge, like owning this outcome, and we have this motto to leave nothing to chance. For a while there we drew the number of days in the year on the whiteboard and it was like, there will never be a time like this. I've never seen anything like it, I doubt I'll ever feel anything like this in business again where there's unlimited demand and it's just our ability to execute against it.

(00:56:39):
And so, we had this motto like leave nothing to chance. How do you make sure that three months are not six months? You have no regrets. Get on the plane to go talk to a customer, make the late night push, check the data six times over again, ship the extra feature that helps. And really, a huge celebratory culture too. It's very flat so there really isn't this principle of ... There's so many people putting up points, directly calling out the people that are putting up points and creating a really fun environment around impact I think has been awesome.

Lenny Rachitsky (00:57:14):
The leave nothing to chance piece I imagine speaks partly to the value of trust in what you're doing. You win if they can trust that your data's awesome, and great, and consistent, and I could see why that ends up being such an important part of what you're building. And just listening to you describe this, I understand it's obviously a massive opportunity, obviously a massive advantage you guys have, and just the stress that comes with that burden also imagine is very high of just like we can't screw this up.

Garrett Lord (00:57:44):
No. Yes, Handshake should be a ... Business does billions dollars revenue as a public company, we should be able to continue to ... I mean, and it also helps our core business. The longer term opportunity that we see is it's connecting, it's building the best job mashing marketplace on the internet. It's probably one of the largest problems in the world like labor supply mashing. It's where people spend most of their time and energy, just hours of their life they spend it at work. The process of searching for a job, applying to a job is going to be completely reinvented with AI. We've been leading the charge there. An AI interviewer that's collecting skills and actually asking about your experiences, doing work simulation experiences that help employers find the best candidates. I mean, I don't know the last time you've done this, but the hiring manager process, reviewing 200 resumes, are you kidding me? 

(00:58:49):
I'm going to sit there and review 200 resumes? Not a chance five years from now. Students manually making cover ... Not a chance. So, there will need to be a marketplace that wins in connecting supply and demand, and talent with opportunity, and we think and get psyched about the opportunity for impact here. That's my story, I went to community college, I paid my way through school. I went to a no name school in Upper Peninsula of Michigan. I worked at Palantir as an intern, it totally changed my life, and I started Handshake because I wanted to make it easier for anyone regardless of who you knew, what your parents did, what school you went to, to find a great opportunity. And I think AI, totally step function improvement in matching. And I think that our human data business is really serving as the foundation for improving matching. 

(00:59:44):
A lot of things that we're doing in the human data business are being integrated to our core business. I think that's going to improve outcomes for employers, save them in the aggregate like billions of dollars over time. And I think it makes the experience way better for students. So, it's just like we have to meet the moment. We still have the stamina, and the excitement, and the passion internally in our core and in the new business to go charge after this. And that's a lot of the message we've been sharing internally is it's time to amp it up. This is a once in a lifetime opportunity to be positioned as well, and we are going to make the moment as a team.

Lenny Rachitsky (01:00:19):
It really is. This very much feels like a once in a lifetime opportunity. Let me ask a few other questions along these lines that are something I've been thinking about, something that a lot of people think about, just while I have you, there's always this question of will we run out of data? Will model stop advancing? Are we going to hit some plateau and there's not actually going to be some AGI moment, SGI moment? So first of all, do you think we'll run out of data? There's a point at which we just can't produce more knowledge and data to feed these models? And along those lines, what do you think is the biggest bottleneck to advancing models faster and further?

Garrett Lord (01:00:50):
Yeah, I mean, it's just the type of data we're going to need is going to evolve. It's going to be CAD files, it's going to be scientific tool use data as they try to automate scientific discoveries and drug discovery. It's going to be esoteric operating systems that exist on scientific tools. So, I love this trajectory and stitching together step-by-step instruction following. The type of data we're going to need is going to evolve a lot. And we haven't even talked about multimodal, and video, and text and audio. There's a huge demand for audio data right now. So, the type of data's going to evolve.

Lenny Rachitsky (01:01:38):
Yeah, I use voice mode all the time. That's on my default ChatGPT experience, just talking to-

Garrett Lord (01:01:42):
It's amazing. It's amazing. I just had a baby on, or my wife had a baby on Sunday, and voice mode's been incredible. I mean, every night, every two hours it's like I have more questions. Voice mode's been huge. So, shot out voice mode. Yeah, so the type of data is going to collect a lot, or change a lot. I think synthetic data has a role to play and in verifiable domains, but what we consistently hear from companies it's like synthetic data is not going to dominate. There's billions, and billions, and billions of dollars of value to extract as a company over the next decade and following the frontier of AI development.

Lenny Rachitsky (01:02:24):
Let me first say just huge kudos to you for just having a kid, your wife just having a kid a few days ago, and building this business that is growing bananas and doing this podcast conversation. I really appreciate you. 

Garrett Lord (01:02:35):
Thank you.

Lenny Rachitsky (01:02:36):
Of course. Is there anything else that we haven't covered that you think might be helpful for folks to hear, or a part of your story that you think might be helpful for folks to learn from, or something you may want to just double down on that we've talked about before we get to a very exciting lightning round? 

Garrett Lord (01:02:52):
I mean, the thing I always love talking, I'm really passionate about people starting companies and helping them do so. I just think in this moment right now with AI, for young entrepreneurs that listen, that read this podcast, because I've been a reader since 2020. We looked. 

Lenny Rachitsky (01:03:07):
Yeah, we did check. That's incredible. 

Garrett Lord (01:03:08):
Yeah, been a long-term reader. I'm just so curious and love sucking up-

Lenny Rachitsky (01:03:08):
Appreciate it. 

Garrett Lord (01:03:11):
... your interviews. But it's like you just focus on doing something of meaning that really helps people. And I think with AI, there's going to be so many opportunities to improve the way people learn. I'm just really passionate about trying to make Handshake a platform that is not only an incredible business, but is also something that really helps solve a societal problem that matters. And yeah, that's be my one shout out here. If anyone wants advice on how to do that or wants to reach out, I'm happy to chat.

Lenny Rachitsky (01:03:43):
Okay, so this is an offer to share advice on starting companies within AI. Is that the offer here? Just so folks-

Garrett Lord (01:03:50):
Yeah, that'd be great. 

Lenny Rachitsky (01:03:50):
Okay. I don't know how much time you'll have for the hundreds of thousands of people coming your way, but I appreciate the offer. That's very cool. Anything else before we get to a very exciting lightning round?

Garrett Lord (01:04:00):
No. 

Lenny Rachitsky (01:04:02):
Well, with that Garrett, we reached our very exciting lightning round. We've got five questions for you. Are you ready?

Garrett Lord (01:04:06):
Ready.

Lenny Rachitsky (01:04:07):
What are two or three books that you find yourself recommending most to other people?

Garrett Lord (01:04:11):
I'm a sucker for Peter Thiel's Zero to One. I read it when I started the company, and watched Peter Thiel's startup school class at Stanford he taught back in the days where there wasn't everything written on the internet about how to start companies, and just think he was the coolest. Love Shoe Dog. I think it's the epitome of starting a company. Hard Things About Hard Things obviously, but these are all quite common books.

Lenny Rachitsky (01:04:38):
But also classics. Ben Horowitz is coming on the podcast, talk about Hard Things About Hard Things. 

Garrett Lord (01:04:42):
Super cool. 

Lenny Rachitsky (01:04:43):
The Hard Thing About Hard Things. Yeah. Okay, have you seen a recent movie or TV show you really enjoy it? I imagine you don't have much time for this, but-

Garrett Lord (01:04:49):
I'm going to get blasted for this, but I did start Game of Thrones with my wife, and I cannot-

Lenny Rachitsky (01:04:55):
For the first time. 

Garrett Lord (01:04:56):
Yeah. 

Lenny Rachitsky (01:04:56):
Okay, cool. 

Garrett Lord (01:04:57):
So, I got a lot of catching up to do.

Lenny Rachitsky (01:04:59):
Why would you get ... No, this is great. It's like people that have watched it-

Garrett Lord (01:04:59):
I've loved it so far. 

Lenny Rachitsky (01:05:02):
You've loved it so far? Okay. It's quite gruesome, that's the only downside of that show. Don't watch it before you go to bed, I don't know how many gruesome scenes you've seen already. Do you have a favorite product you've recently discovered that you really love? 

Garrett Lord (01:05:14):
The SNOO. The baby automated SNOO has really helped us a lot. So love the, shout-out SNOO team. 

Lenny Rachitsky (01:05:24):
Amazing. I had a SNOO as well. We never actually turned it on, we just ended up using it as a basinet the whole time. 

Garrett Lord (01:05:28):
Yeah, most of the time it's not turned on, but a couple of cries it's been turned on, it's been very helpful. 

Lenny Rachitsky (01:05:33):
Do you have favorite life motto that you find yourself coming back to, sharing with other people?

Garrett Lord (01:05:37):
I love that leave nothing to chance, leave it all out on the field. Grew up in a really hardworking family, and dad worked really hard to provide, make it happen for us and it's like just give it your all. Leave nothing a chance.

Lenny Rachitsky (01:05:51):
Okay. So the last question, I was researching you in prep for this podcast and there's a story that I love about your hustle early on is when you were going from campus to campus pitching schools to join Handshake, and there's a story where you had to shower in the Princeton's pool to save money because you just didn't have a place to stay. Is there something there? Is there a story there you could share?

Garrett Lord (01:06:13):
Yeah, so it was a tough one. I mean, I almost got arrested at Princeton, because I mean, I guess for entrepreneurs that are traveling around all the time, we were sleeping out of our car. We had this Ford focus, we would put 20, 30,000 miles on it, sleep in the back of like McDonald's parking lots because they're well lit and had good wifi back in the day. And instead of staying in a hotel, a way to freshen up ahead of your meeting is every university has a pool and the pool's almost always, it is always open. We never had a situation where it's always open for people to swim in the morning, like fitness. Faculty, students. And every pool, what do they have? They have a shower. 

(01:06:49):
So, you could go to any pool at any university in the country, and you can get a free shower and freshen up. So, the Princeton campus security did not appreciate me showering as a non-student, but I think it meaningfully helped us because the Princeton campus security called the career service center director we were selling to, being like, "Who's Garrett Lord? Is he really here to pitch you software for your career center?" And it made the start of the meeting with the career center really stimulating and exciting, because they were like, "You showered in our pool, you drove here?" "Yeah, we drove here from Michigan." And so, I think that showed a level of commitment that was exciting for them.

Lenny Rachitsky (01:07:29):
Fast-forward to all these founders now starting to use this growth lever of getting in trouble with the campus police to get better meetings with the school leaders. Incredible. Garrett, this is such an insane, amazing, inspiring story, just like what you're building and the opportunity here, and just how it's fast, it's going, and all the advantages you have. If I was an investor in Handshake, I'd be like, "All right, 10 years, it's going great." And now it's like, "Whoa, holy shit. Where did this come from?" Incredible. And it's just also really meaningful. So, I'm really happy that you made time for this in spite of the madness you are in right now. Two final questions, where can folks find you if they want to maybe reach out or maybe if you're hiring, let us know. And then, how can listeners be useful to you?

Garrett Lord (01:08:12):
I mean, sign up for Handshake. If you want to message me on there, it's the easiest way to reach me. Just find me at garrettlord@Handshake, and you find me on Twitter. Love X, huge X guy. You can email me at garrett@joinhandshake.com and double R, double T. And how can you be helpful? We are trying to hire so many people. We have offices in New York and in San Francisco, and London and Berlin. If you have friends that are maybe passionate about this, you let them know, or you're interested in the learning more, please reach out. We'd love to talk to you. Hiring is like the number one problem we have right now to meet the demand. So, if you're talented and interested in learning more about Handshake, if you want to work on our consumer product, if you want to work on our employer products, cool PLG issues or the state-of-the-art consumer social experience, like reach out, or you want to work on the AI business we'd love to talk to you.

Lenny Rachitsky (01:09:06):
To make it even more clear for folks, what roles are you most hiring for? Is it every role? Is it engineering? 

Garrett Lord (01:09:11):
Engineers.

Lenny Rachitsky (01:09:12):
Engineering, all right. If you're an engineer and want to join one of the fastest growing AI companies in the world right now, here we go. We'll link to your careers page in the show notes. 

Garrett Lord (01:09:18):
Thank you. 

Lenny Rachitsky (01:09:19):
Yeah, of course. Garrett, thank you so much for being here. This was incredible.

Garrett Lord (01:09:22):
Of course. 

Lenny Rachitsky (01:09:24):
Bye everyone. 

(01:09:26):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review, as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at Lennyspodcast.com. See you in the next episode.

