---
guest: Inbal S
title: The future of AI in software development | Inbal Shani (CPO of GitHub)
youtube_url: https://www.youtube.com/watch?v=f10s3rxKaJw
video_id: f10s3rxKaJw
description: 'Inbal Shani is the chief product officer at GitHub, where she leads
  core product management, along with product strategy, marketing, open source, and
  communities, including the development...

  '
duration_seconds: 3004.0
duration: '50:04'
view_count: 9980
channel: Lenny's Podcast
keywords:
- growth
- acquisition
- churn
- metrics
- roadmap
- prioritization
- revenue
- culture
- leadership
- management
- strategy
- vision
- mission
- market
- persona
---

# The future of AI in software development | Inbal Shani (CPO of GitHub)

## Transcript

Inbal Shani (00:00):
The user of the AI tools to develop software needs to form a different thinking. You need to start figuring out how are you using these AI tools to help you be successful. And it's no longer just the actual code writing, it's really evolving your thinking to the big picture, to the connected experience, to connected systems, which today we just find it more in the world of more senior developers and less and less in the junior developers.

(00:24):
The junior developers, when they start, usually we expect them to be able to write simple code. But if now there is an AI system that is helping them writing code, they can spend more time from the get-go understanding the system, understanding the environment that they're building, or understanding that product that they're building, which today they don't have time because they're still learning how to code.

Lenny (00:46):
Today, my guest is Inbal Shani. Inal is Chief Product Officer at GitHub, formerly a general manager at AWS and at Microsoft, and also a senior software developer on Amazon Robotics.

(00:58):
In our conversation, we explore the end state of Copilot and AI-based tooling for software engineers, what the future of software development looks like with AI, what's underhyped and overhyped in AI and software development, what metrics the teams look at to understand if Copilot is doing its job, what mistakes teams and companies make jumping into AI, the design philosophy of Copilot, plus what's helped Inbal most become the leader she is today, and also where GitHub is heading as a product and an organization.

(01:27):
With that, I bring you Inbal Shani after a short word from our sponsors. You fell in love with building products for a reason, but sometimes the day-to-day reality is a little different than you imagined. Instead of dreaming of big ideas, talking to customers, and crafting a strategy, you're drowning in spreadsheets and roadmap updates, and you're spending your days basically putting out fires. A better way is possible. Introducing Jira Product Discovery, the new prioritization and roadmapping tool built for product teams by Atlassian.

(01:59):
With Jira Product Discovery, you can gather all your product ideas and insights in one place and prioritize confidently, finally replacing those endless spreadsheets, create and share custom product roadmaps with any stakeholder in seconds, and it's all built on Jira where your engineering team's already working. So true collaboration is finally possible. Great products are built by great teams, not just engineers. Sales, support, leadership, even Greg from finance, anyone that you want can contribute ideas, feedback, and insights in Jira Product Discovery for free.

(02:32):
No catch. And it's only $10 a month for you. Say goodbye to your spreadsheets and the never ending alignment efforts. The old way of doing product management is over. Rediscover what's possible with Jira Product Discovery. Try for free at atlassian.com/lenny. That's atlassian.com/lenny. This episode is brought to you by Sanity. Your website is the heart of your growth engine. For that engine to drive big results, you need to be able to move superfast, ship new content, experiment, learn, and iterate.

(03:06):
But most content management systems just aren't built for this. Your content teams wrestle with rigid interfaces as they build new pages. You spend endless time copying and pasting across pages and recreating content for other channels and applications. And their ideas for new experiments are squashed when developers can't build them within the constraints of outdated tech. Forward-thinking companies like Figma, Amplitude, Loom, Rightgames, Linear, and more use Sanity to build content growth engines that scale, drive innovation, and accelerate customer acquisition.

(03:36):
With Sanity, your team can dream bigger and move faster. As the most powerful headless CMS on the market, you can tailor editorial workflows to match your business, reuse content seamlessly across any pager channel and bring your ideas to market without developer friction. Sanity makes life better for your whole team. It's fast for developers to build with, intuitive for content managers, and it integrates seamlessly with the rest of your tech stack. Get started with Sanity's generous free plan.

(04:02):
And as a Lenny's Podcast listener, you can get a boosted plan with double the monthly usage. Head over to sanity.io/lenny to get started for free. That's sanity.io/lenny. Inbal, thank you so much for being here and welcome to the podcast.

Inbal Shani (04:22):
Awesome. Thank you for having me. I'm excited to be here.

Lenny (04:25):
I want to start with just a broad question about where software development is going. It feels like you're at the center of the storm of what is changing in software development. It almost feels like GitHub kicked off the storm with the launch of Copilot. So let me ask, what do you think is overhyped in terms of what is changing in software development and then what do you think is underhyped?

Inbal Shani (04:46):
So I joined GitHub as a CPO basically a year ago. Two days ago, I celebrated my first year. And for me, the initial approach is let's look at the platform, let's look at the software development lifecycle, and draw some conviction. And for me, the biggest conviction is that developer happiness and productivity strongly depends on their environment and dev tooling. And as such, AI is really critical to that mission.

(05:11):
When we're looking into what's happening right now with AI, it really became table stakes on expectations among developers, and it's really central and critical for them to be able to do their job. We know that something like 92% of developers are already using AI tools. But in that landscape, some of the things that are overhyped is that generative AI will replace humans. I don't see that happening in the near future. The way I think about it, you always need that human in the loop because AI cannot replace innovation.

(05:45):
That creative spark, that creative thinking that is the center of humanity, this will not be replaced by AI, at least not in the near future. If we think about what does that mean having an AI tool that is successful, you need data. In order to generate data, you need humans using tools, acting with tools, doing something, something. So I think the overhype that is happening right now is that generative AI will replace humanity. It's going to be the solution for everything, and I think it's a tool.

(06:15):
If I'm drilling down to the things that are underhyped right now in the world of software development, I'm starting hearing a little bit more on AI driven testing, but there's not lots of mention on it. And if we're thinking about the world of AI where we're going to generate much code, much more productive, much more efficient, more lines of code, more application, then testing is becoming such a critical part of that journey of developing software.

(06:43):
And I would like to hear more about that and what companies are thinking about how do they use AI to generate a larger suite of testing to be able to validate the work.

Lenny (06:53):
And by testing you mean like unit testing, integration testing, things like that?

Inbal Shani (06:57):
All of them, load testing, load testing, infrastructure testing, security testing, penetration testing. When you need a human to write all these testing capabilities, you need a lot of humans that needs to form different thinking. Can we leverage AI to really generate that testing suite that test everything that you need from unit testing and functional testing to load testing, to performance testing?

(07:23):
There's a lot of testing that we do that we don't even consider them as testing, so we don't necessarily spend a lot of time in doing them. But if we're now saying software is in the center of everything, all companies will become a software company in some form or another, there is more code being generated. Hence, the importance of testing is becoming much more critical.

Lenny (07:43):
Let's follow that thread. You talked about how you don't see software engineers completely disappearing. What's your just general sense of how software development will be different in three to five years? What do you think is going to be different? And then also just how do you see the end state of all of this of Copilot and tools like this getting better and better and better? What do you think this ends?

Inbal Shani (08:02):
For me, and I keep on saying that again and again, Copilot is a copilot. It's not a pilot. You still need the human in the loop. But that means that now the software developer or the user of the AI tools to develop software needs to form a different thinking. One, you need to start thinking more systems, more architecture. You need to start figuring out how are you using these AI tools to help you be successful? And it's no longer just the actual code writing, it's really evolving your thinking to the big picture, to the connected experience, to connected systems.

(08:36):
And what we will see in the fullness of time that developers, one, will adopt much more of that mindset, which today we find it in software development, don't get me wrong, we just find it more in the world of more senior developers and less and less in the junior developers. The junior developers, when they start, usually we expect them to be able to write simple code.

(08:57):
But if now there is an AI assistant that is helping them writing code, they can spend more time from the get-go understanding the system and understanding the environment that they're building or understanding the product that they're building, which today they don't have time because they are still learning how to code. So I think that's one element. The second element that I expect to see changes is in the world of hardware development, because we know that AI has a big footprint and requires a lot of resources.

(09:24):
And in order to be able to meet the scale, to meet the demand, we need to be able to improve our hardware, our CPUs, our GPUs, our compute and optimization of code. And that's another area that today it's a niche of people that are spending time and I think it'll become much more aligned across the software development lifecycle.

(09:44):
Integration with AI is something that will definitely become something that is more normal for every developer, is today something that we start seeing that revolution, that acceptance, that AI tools, I need to figure out how to integrate with AI, I need to know how to use AI. It will become something that is more custom, and we will start seeing that shifts from very early on. When developers are start shaping their thinking, they will start understanding all these components.

Lenny (10:14):
I saw a stat that at Shopify over a million lines of code and their code base was written by Copilot, which I don't know if I can do the math, but I imagine that's more than one person would've written in their lifetime and probably many engineers write in their lifetime. And I think that number reminds us just how fast things are moving and how much is actually changing.

(10:35):
You also mentioned 92% of engineers are using AI tools already. Is there any other stats that you can share that might surprise people about the usage of Copilot, growth of Copilot, things along those lines?

Inbal Shani (10:46):
Yeah. Well, we have over 37,000 organization and more than 1.5 million developers that are using Copilot.

Lenny (10:54):
Wow.

Inbal Shani (10:54):
And they're writing code based on our surveys 55% faster. Imagine that you can give a software developer even few minutes, half an hour back in every given day, how much more productive they're becoming, and also as a result, how much happier they're becoming. So we know that in a survey that we have run through our users is 85% of that participants felt more confident in their code quality and also code reviews were completed 15% faster without Copilot. And we know that usually no one likes to do code reviews.

(11:32):
So if we can help accelerate and make developers take their time in doing code reviews, and also if we think about removing frustration, then 88% felt less frustrated and more focused on their ability for coding. And that is just the beginning. We have different examples from our customers. I think Accenture is a recent one that we got where they had 88% of suggested code was retained. So we have a lot of these stats that are coming together to showcase the size and the impact of using Copilot and AI tools for software development.

Lenny (12:07):
Say companies hear these stats of like, oh, we're going to be 25% more efficient. Some people may think we need 25% less engineers. We're going to do all the same things. I imagine what you're actually finding is your engineers can do more. So it's not like you need to cut your people, it's that people can be faster and better.

Inbal Shani (12:23):
No, let me be very clear, you cannot cut your people. You have to have a human in the loop. Copilot is a copilot, it is not a pilot. And I keep on saying that sentence again and again. I think the second thing that what companies need to realize, and that's another developer experience survey that we have run recently, that throughout the years we have added so much tasks on a single software developer from writing code, writing testing, interacting with people, collaborating with 21 people on every given week, going to meetings, waiting on builds, digging into legacy code, all of that is added to the fact that they need to write code, which is their basic work.

(13:03):
So most developers span less than 25, some say less than 20% of their time writing in code. So if we're able to give them half an hour back, one, they can write more code. Second, they can have a break and take a breath so we don't burn them out and they're more happy. Third, we give them more time for collaboration and creative thinking, so that sparks innovation. That is not something you want to cut back.

(13:28):
This is something you want to be able to give as a gift to your developers so they're happy with you and you can retain them. They can do their job. They're productive. Hence, they're happy.

Lenny (13:38):
I've talked to a bunch of engineers that use Copilot. One thing that surprised me is the most amazing engineers love Copilot. You think this would be for junior engineers learning to code better and faster, but 10X engineers say that... Someone told me it made them 50% better and faster too, which is incredible. What mistakes do you see product teams and engineering teams make when they rush to start adopting AI, integrate AI into their workflows?

Inbal Shani (14:07):
I think there are a couple things. The first one is companies expect a change to happen magically. Here's a tool, go use it. And it's not always flying the same way across all companies. So investing time in really taking the company through a change management process. The second thing that I'm seeing is that since AI is so hyped right now, there is often the questions of, oh, what should we do with AI? So there is that sense that I have to do something with AI.

(14:38):
Because if not, I'm not doing the right thing. Versus the question that for me is a big focus for my product team is, what is that problem that we're trying to solve and how can we leverage AI better to help solve the problem versus what do we do with AI? So it's really working backwards from the customer problem from what we're trying to solve, and then realize what are the best tools that we have in order to do that work better and think through that landscape versus, oh, AI is here, we have to use it. Because if not, we're not doing something right.

Lenny (15:11):
Is there an example of that that comes to mind of someone that did that incorrectly or wasted a lot of time?

Inbal Shani (15:17):
It's not necessarily examples, but I've been talking to some of our customers and they're coming to us. "We heard about AI. What do you think we should do with AI? And how should we adopt AI? And can we learn from your experience?" And I'm sharing our experience. When we started thinking about AI, it was with the idea to make developers much more productive. And what are some of the things that we've seen? That developers have multiple tasks on them and they don't have enough time to spend on coding.

(15:45):
So how can we give them time to spend more on coding and what are some of the coding element that we can automate? And from that comes the need to, okay, let's incorporate OpenAI, let's incorporate ChatGPT, let's connect all of them to help create that tool that helps developer be more productive and is AI based. So I'm sharing how we went through that journey to think about how to use AI. I see a lot of the times light bulbs with the customers like, "Oh, we didn't think about it like that."

(16:15):
It's more about we wanted to plaster AI on a lot of things versus I have this workflow and it requires a lot of manual work, or it requires a lot of configuration. Maybe I can think how to incorporate AI into that and really shorten the time or make it seamless or make it less friction for developers to adopt that tool and so on and so forth. So it's really sharing more how we are thinking about it and helping our customers to understand the same.

Lenny (16:42):
Along the same lines, you're talking about how you think about it with your teams. It feels like your product teams are probably living in the future of how other product teams will operate because you have access to stuff everyone else doesn't necessarily have access to. They probably adopt these tools a lot faster than the other teams would. What are some ways that your product teams operate that other teams may not yet be operating?

Inbal Shani (17:04):
In GitHub in general, it's not just the product team. GitHub is GitHub. I'll say we eat our own dog food, and that means that we are the first to try every feature, every capability that we're developing. And it's not just our engineering team, it spans across GitHub. So for example, GitHub is running on GitHub. There are several blog posts and talks. Even in the recent Universe, we had a specific talk in terms of how GitHub is using GitHub and adopting AI across software development lifecycle.

(17:32):
And the biggest focus for us is if we're saying that GitHub is a developer platform and it's more than that, it's a software development platform, how are we making sure that all the persona that are taking part in the development of GitHub are also using GitHub? So for example, our finance team is using discussions and posts and PRs and reposts to communicate our AR numbers and so on and so forth. We have our legal team using, we have our HR team. If they like it or not, it's a different question.

(18:02):
But the idea is that we're using GitHub to run GitHub, and the product team is one of the first early adopters along with our engineering team. So for example, when we've tested chat and we wanted to see the quantity or the recommendation, the search, this is something that the product team was one of the first users to go and figure it out. Is it giving me the right thing that I need to do that? Is it summarizing the PR the way I want to summarize? And so on and so forth.

(18:27):
But we are really strong in advocating that we have to be the one testing our tools. If we cannot use them, our customers cannot use them for sure. So nothing is shipped before it spends enough months cooking inside GitHub, so we have to say this is working for us or not before we put it at the end of our customers.

Lenny (18:47):
One of the magical elements of Copilot is how it just fades into the background. You don't have to chat with it. You don't have to tell it anything. It just infers, here's what you're doing, here's the answer for you. If you want to use, it's cool. If you don't, it's fine. Is there anything you could share about just the design philosophy of Copilot?

Inbal Shani (19:05):
Yeah. The design philosophy for Copilot is very much aligned with the working backwards concept that I just mentioned. It's really putting yourself in the shoes of your customers and figuring out what is it that they need, how is that experience going to work for them? If it's an extra tool and if you need to ask for it and if you need to ask for it or if you need to wait for it, then developers will not adopt it.

(19:27):
So because we developed it for ourselves first and we wanted to experiment with that, the design philosophy was put yourself in the shoes of a developer, how would you like that experience to be? In 2020, we had a group of GitHub engineers that were working with the design team and with OpenAI GPT to really figure out how we're going to build that and how it can work to help developers to do their job more efficiently, more productively, improve their collaboration and happiness, and so on and so forth.

(19:57):
But the grounding principle was the developer needs to want to use this tool. And the more you add friction, the more you add churn, the more you add complexity, the developers will not want to use their tool. We just talked about all the things that the developer needs to do in every given day. Now add to that mix, I need to learn how to adopt AI, we knew that it will not fly. So it has to be a seamlessly integration. It needs to be something that is very intuitive for developer to use to be successful.

Lenny (20:24):
What are the success metrics for Copilot? It's such an interesting problem of measuring efficiency gains and productivity gains for engineers. What metrics do you focus on to tell you this is doing what we want it to be doing?

Inbal Shani (20:35):
We are in a world that there are no right metrics. There is no one metric to rule them all. It's a combination of the things that you're looking to measure out of adopting AI. You can think about measuring code quality using AI. Can you improve the code quality? Can you improve the security of your code by introducing, for example, our GitHub Advanced Security using AI?

(21:00):
So there's a lot of different metrics that if you combine them together are providing you with that developer productivity, and then there's developer productivity, developer collaboration, time gain, that if you're bringing them together are yielding the developer happiness. The biggest area of focus for us right now is the definition of productivity because we have so many users that are coming to GitHub and they're looking for that productivity gain.

(21:27):
But one of the things we're very conscious of as we continue evolving Copilot and AI across the software development lifecycle across all the tools, productivity is not the right metrics against each one of these components. When we're implementing AI to GitHub Advanced Security, writing more secure code is the right element. It's like how many secrets were we able to prevent from leaking? How many issues in the code we're able to detect and find and fix before you ship that?

(21:51):
So I think that the world of the metrics for AI is really a big one. We are working a lot with our customers as they're asking the same questions and they're running their own experiments within their companies to figure out what is it that they want to measure. The most easiest one is time, but time is, it's funny what I'm going to say, but time is not quantifiable as a success metrics because you can write really bad code really fast.

(22:18):
So it's really about how are we taking time and translating it to efficiency, to productivity, to something that are harder to measure, and then how does that lead to develop core happiness, which is another harder metrics to measure. So the combination of all these input metrics leading to eventually developer happiness is what we're focusing on.

Lenny (22:40):
Yeah, it's so interesting because engineers could end up spending more time coding because they're enjoying it more. They're getting more done. Also, more lines of code isn't a good metric because you don't want to know if those are good lines of code. That's a classic way to not measure engineers well. So to me, it feels like developer happiness is the ultimate metric. We had Nicole on the podcast who came up with this framework, DORA, that's an interesting way of just measuring developer experience, developer happiness.

Inbal Shani (23:05):
Right. I think one of the things that we're talking to customers and we're trying to figure out how we're articulate is instead of time, can we talk about time to value? So from the moment you put a developer on a task, how long did it take you until you realize the full potential or the full value of that, if it's generating revenue, if it's in adoption, if it's time to market? You can define your time to value in different ways.

(23:28):
But eventually you're investing in AI tools to help your developer to be more productive, to be more efficient, to be more happy, and then is it impacting your time to value, which is something that's the business side that they're looking to measure.

Lenny (23:44):
This episode is brought to you by HelpBar by Chameleon, the free in-app Universal Search Solution built for SaaS. Your help content lives outside your app and is scattered in many places, forcing users to waste time hunting for answers HelpBar solves this. It delivers answers directly inside your app and eliminates context switching. Users can search or ask questions to get AI generated answers and lists of the most relevant documentation from all of your help sources, including your knowledge base, docs, blog, and video libraries.

(24:15):
You can also use HelpBar to navigate your app and launch actions such as scheduling a meeting or viewing an interactive demo. The best products today use Command-K for in-app search and navigation. HelpBar makes that readily available within your app without engineering or new code, give users a faster and more delightful self-serve experience that reduces friction and increases in app engagement. Upgrade your user experience with this modern component and supercharge your product-led motion.

(24:43):
Sign up for HelpBar today. It's free and easy to set up in minutes. Check it out at helpbar.ai/lenny. That's helpbar.ai/lenny. Coming back to where this all goes, imagine you've seen all these demos of people like sketching a website, taking a picture, sending it to ChatGPT, and it builds the website for you?

Inbal Shani (25:04):
Yeah.

Lenny (25:05):
How do you see all of that sort of thing playing into this? Do you see CEOs being like, "Here's the iPad app I want," I'm going to sketch it for you, and then just run it through Copilot version 10 and it writes it for you? I know that you're saying engineers won't be cut and only increase and become more efficient, but I guess where do you see that version of it going of just like, here's a sketch, build it for me?

Inbal Shani (25:27):
I'm thinking about that as a better collaboration tool versus a production tool. Because right now, a lot of the time where we see challenges in articulating ideas is the communication. It's the clarity of thoughts. So if we can leverage AI to improve collaboration, and you basically put a drawing in front of Copilot and it helps tell the story of what is it that you're asking your developers to do, it shortened a lot of cycles and the back and forth. So what did you mean?

(25:53):
Did you mean the button here, or did you wanted it pink, or did you want that application, or did you want that operating system? So if Copilot can help refine communication, and it's becoming likely the best collaboration tool that exists in the market, especially in the global world where we are where we see communication is ongoing challenges between different personas that are taking part in coming up with an idea and basically we see AI and in our view is Copilot becoming that next natural language conversation.

(26:26):
It's that translator that helps bring everyone on the same page because it's creating that universal conversation language, the same that math used to be.

Lenny (26:37):
Reminds me, there's another conversation I was having with an engineer and he was saying how he loves writing those simple functions that Copilot is now doing for him and he's sad that it's doing it for him, but he doesn't turn that off. But he kind of is like, "That's what I really enjoy. These little things that I could just crack like sort function of some sort." I guess, is there anything you think we lose with so much of our code being written for us?

Inbal Shani (27:01):
I think each developer has their own part that they enjoy doing. And you don't have to use Copilot to write your simple code. You can use Copilot through a chat experience and use them as an AI assistant and brainstorm. We're giving you a set of tools, and we have a scenario in mind how you should use them. But what we're seeing is developers are using them very differently. Everyone is choosing their own flavor on how to use the tools. There is no right and wrong way to use it.

(27:32):
It's a tool. It's a language. When I was learning how to code, I used to code in C, and then Java became a thing. I'm like, oh, but this is taking away my job because I used to write all these functions and all these libraries and now Java has it all. And then Python came, which is another abstraction layer. It's like, okay, so now I don't even need to think about that because Python can do all of that. So it's a matter of how you use the tools and what you use them to do what. There are areas that I will still go and write in C, even today.

(28:04):
I don't trust someone inventing metrics for me in an efficient way if it needs to run on a very small CPU. So I'll do that myself. On the other hand, there is going to be an element that I'm going to delegate to a higher obstruction tool, and that's exactly the way I think about AI. You pick and choose how you want to use it. There is no global way that is the absolute truth that everyone has to follow. You need to think how you use your tools to do your job in a way that you're still keeping the things that make you happy.

(28:34):
On the other hand, use AI to do the things that you less enjoy. Maybe you like writing functions, but you don't like writing, testing, so generate unit testing and so on and let AI do its job for you and you still focus on the things you enjoy.

Lenny (28:48):
Are you actually still finding time to code? Are you still writing some C on the side?

Inbal Shani (28:52):
A little bit now. Now I'm mainly playing with my older son, so he has more time to cook, but sometimes I enjoy spending time with him and brainstorming and talking about things and architecture. I think recently a few months back, he did a project on sensors and sensors integration, and he came across common filter, which was the thing that I used to do many, many years back.

(29:16):
And he's like, okay, what is it and how is it done? And then we went through that and I helped him think about the structure and the sensors fusion and all of that. And then sometimes I'm like, "Okay, move aside, here you go. This is how you..."

Lenny (29:29):
Turn on Copilot. Just kidding.

Inbal Shani (29:29):
Mommy's Copilot.

Lenny (29:33):
That's so funny. That reminds me, I was watching a talk of yours and you were training tuning models and LMS way back in the day, before it was very cool. And so you've been in this space for a long time. Looking back, is there something that you see now of where things were going that you didn't see at the time?

Inbal Shani (29:51):
I grew up in a world of niche AI where you have to be an expert and you need to be trained for years understanding how to tune a model, what is the right output, and you needed to understand how to build a simulation to test it, how to ingest data, focus on optimization. I've seen the evolution of AI throughout the year with all the talking devices and conversational AI, and then it started as a single term. It came up as a multi-term.

(30:22):
So I've started seeing that trend of more democratizing AI, but I didn't expect that boom of generative AI. Everyone that even doesn't even know what AI is, that they need to use AI. I think that was the thing that caught me by surprise because I was so trained that you have to be an expert to use AI. So for me that was aha moments, like hmm, this is interesting. So what's next?

Lenny (30:47):
Do you have an opinion on whether large language models are the end all and be all of where all this goes and just continue to add in compute and data? Or do you think there's another, I don't know, something on the horizon that's going to again completely transform the transformer model of AI?

Inbal Shani (31:06):
I think we've pivoted very hard towards a generative AI and generalized AI can solve everything. I believe that the future is going back to scale back a bit to the niche AI. So we will live in a hybrid world where you still have specific AI models that are solving very specific problem where the generative AI will have its limitation. It's a general purpose tool, so it can be as good as the data sets, but it also try to find some statistical recommendation. Is it good? Is it not good? So it's limited by the training set that it has and it's trying to be everything for everyone.

(31:43):
There are going to be areas where you still need to train models. For example, I spend my time in the aerospace industry and in the automotive industry. I don't see self-driving car models that requires so much delicate, specific models, tuning, high safety regulation, all of that being developed on the ChatGPT. I might be wrong, but I think that eventually we will find ourself in the world of hybrid models and multi-models where there will be several LLM models coming together because each one of them will have their own benefit.

(32:19):
And then there's going to be a niche AI or a more configurable customized model for specific use cases. So that's my prediction of the future. But in 10 years from now, we'll all be smarter.

Lenny (32:32):
Yeah, the future hard to predict.

Inbal Shani (32:34):
Yes.

Lenny (32:35):
I wanted to ask, so GitHub came up with this whole Copilot idea. We had Ryan on the podcast talking about how there's a researcher just experimenting with what can we do with a bunch of data. And then that essentially turned into, wow, this is actually working. Let's quickly scale this and launch it.

(32:54):
I guess is there anything you learned from that huge success within GitHub and Microsoft to find other big opportunities? Is there something you do about how you structure product teams or create space for people to experiment with things like this to find the next Copilot?

Inbal Shani (33:10):
It's a lot about that. It's a lot about creating that bandwidth for the team to innovate and experiment and carving that time out, but also being okay that not every experiment is going to be successful. So the shift to learn or to fail forward, these are the philosophies that I believe in. If you don't try, if you don't experiment, you will never innovate. And if you don't fail, you will never learn from your mistakes, you'll never learn from your experience, so you will not progress forward.

(33:36):
So really creating that ability to experiment, the same that we've done with Copilot or we've done in GitHub Advanced Security or even the way GitHub was created, it's all that innovative thinking that the teams have that are thinking about what is that next generation use case? What is the future developer will need to be happy, to be more productive, to do their job? In a world that software development is changing so fast, you have to create that bandwidth for the next generation, the next innovation.

(34:08):
And if you didn't have a chance to see that the two-day keynote in Universe, I highly recommend because we basically shared our next vision for Copilot with Copilot Workspace. We also had Satya Nadella on stage and he was very excited. He's like, "Oh my god, GitHub, if you build that, this is amazing." So you see that we keep on putting this vision forward again and again at least six months to a year before we even have something in the market because we're already thinking, we're already innovating, we're already on the next thing.

Lenny (34:38):
Is there something that you do to allow for that other than just these principles of ship to learn and it's okay to fail? Is there a way you structured teams or resource teams? Is it like you have a percentage of time to think about other ideas, or is it just generally we're okay failing, find time to work on other things?

Inbal Shani (34:55):
It's a couple things. One, it's spend time with customers and learn from your customers, because a lot of the innovative ideas are coming basically from conversation with customers because they're sharing with you their frustration, they're sharing with you what they would like to have, they're sharing with you what will be an amazing invention for them. So that's the first thing is creating that mechanisms. And we spend a lot of time talking to our customers and also talking to our community.

(35:21):
We're fortunate to be the home for all developers and home for all open source. Large open source foundation and small open source foundation are running on top of GitHub. So that's another feedback cycle that we have to really gather those ideas and those asks to help us shape the future. And then the second thing is really about the teams pitching idea. It's like, "I have this idea. I've been doing some research. Here's a paper that describes what is it that I want to do," and then we figure out, okay, when can we fund it?

(35:49):
How can we fund it? Can we allocate a specific bandwidth? Can we do a POC? Do we do that in that team? Do we do it as a V team? So we keep it flexible. And we also have a research team, which are GitHub vNext, that basically that's our day job is to think about the next big innovation. But in GitHub, innovation is coming from everywhere. It's coming from our field team that are talking to customers and are implementing different variations of GitHub for customers. And they'll come back with some feedback or an idea.

(36:18):
It's coming from the product team. It's coming from the design team, from the engineering team. It comes from everywhere. So if you try to structure innovation, you're losing that organic spark that is humanity. Imagine that someone say you have 15 minutes a day to be creative. I don't think it's the pull. So it's encouraging that thinking more than structured.

Lenny (36:50):
Can you talk more about that team that you mentioned? What is it called? The vNext team?

Inbal Shani (36:50):
The GitHub Next. Yes.

Lenny (36:51):
Next team. Can you talk a bit more about what that team is and how that works?

Inbal Shani (36:53):
They're basically applied scientists, research scientists that are working together, and they're really thinking about three, five years horizon. They're not thinking about the right now. They're thinking about what is the future for software development is going to look like. They're writing papers. They're running experiments. They're doing POCs. Their job is to invent the future.

(37:16):
 But again, it's really a synergy because they're talking to the product, to their engineering, so they're getting ideas from that. They're talking to customers, or we're sharing feedback. So that's our GitHub Next. It's basically our research team.

Lenny (37:28):
And that's where Copilot emerged out of, is that right?

Inbal Shani (37:28):
Right.

Lenny (37:32):
It's so interesting because, I think I talked about this with Ryan, there's so many companies with a team like that. Like Facebook had a famous one, New Product Experience team. Google had Google... Forget what it was called. But none of them have really been successful is my understanding and this one was. Is there anything you think you're doing differently? Is it more science-based and research versus just product managers trying a bunch of different apps? I don't know, is there anything you think is key to this team being successful?

Inbal Shani (37:59):
I think there are two elements for that. One is having the right people with the right mindset on the team, allowing them and giving them the bandwidth and freedom to innovate. And the second thing is that we're focusing on making things real. So we're not keeping them far or in disconnect from the product and engineering.

(38:15):
There's a lot of synergy, there is a lot of discussion, because what happens in teams that are not successful, at least from what I've seen, one, that the team is becoming basically an university, they write papers, but nothing is coming out of that, so nothing finds its well to production. So if you don't introduce that, how do we take it to production from day zero when you're thinking about a new idea? It's rarely that it'll go through that hump cycle and itself in production. And the second thing that companies tend to use these teams is too much tactical.

(38:47):
Here is that, "We need something in six month. Go invent it right now," and then they're basically creating another engineering or producting to think about the things that are now in horizon one. So I think in GitHub we found the right balance between having the right people, having the right mindset, but also creating that synergy between the future thinking to how we make it real, so we have a strong relationship, especially between the product team and GitHub Next, to make sure that this relationship are ongoing and ideas are flowing both ways.

Lenny (39:20):
Today, you're chief product officer at GitHub, which is I think a dream job for a lot of people. Early product managers, senior product managers want to figure out how to get to a place that you're at today. And I'm curious what you found most helped you build the skills that were necessary to be successful in this role? Was it mentors, exec coaches, just doing the job for a long time? Anything else along those lines?

Inbal Shani (39:47):
Combination. It's never one thing, because the role of the chief product officer is so broad. You're not just the head of products. And that's the mindset that is now evolving in the industry is that a chief product officer is more than just the head of product. They need to have a business thinking. They need to understand their go-to market strategy. They need to understand the sales play. They need to understand how engineering are building products. It's not just about let me write a set of requirements or think about the vision and the future.

(40:16):
It's how all these components in the company are operating together to build that product. And some of that you learned from looking into the leaders that you work for and see how they're thinking. From my first boss in the aerospace industry, I learned how to think system. Not to think just on the problem that I'm solving right now, but how the problem that I'm in charge in solving that filter that I'm responsible in tuning is connected to their control system and the ignition system and all of that and how is it eventually being displayed.

(40:47):
So that requires me to think from the get-go on the bigger solution, not just my component. So I think that's one. The second thing is really thinking about the people and change management and how you take people with you, because a product manager role is a very influential role and a lot of the things you do is influencing other people. Although everyone thinks that as a product manager you get to do things, you get to write papers, but you need to influence the engineering team to build a product that you want them to build.

(41:17):
You need to influence the revenue team to go with a go to market and sell the product the way you envision it. So there's a lot of influencing happening. You need to understand how to do that and building that skillset as a product manager from the get-go is very critical. So for me, it was the fact that I was fortunate enough to do different roles in the industry and learn from different people, but also looking up, looking across, and looking down into the people that I manage and what are the things I could learn from them?

(41:47):
What are some of the skills that they have that are not necessarily in my toolbox and how can I adopt them? What does success look like and what are some of the things that make people unhappy? And you don't necessarily want to have these tools in your toolbox. So it's a lot of what's yes and what's no in a combination.

Lenny (42:04):
Yeah, it's exactly like you said, it's all the things combined. I really like that last point of just identifying people that are good at something that you want to get better at and just learning from them, watching them, maybe asking them questions about how they're operating. I am trying a new segment of this podcast called Failure Corner, and my question to you is, what's the biggest career or product failure of your career and what did you learn from that experience?

Inbal Shani (42:30):
I'll call it the biggest learning because I'm not a believer in failure. I'm a believer in learnings. And every time you fail, it's a big learning and I prefer to look at that as opportunities. I think biggest one was likely early on when I started being a leader and the manager of a team, I'm a very go, go, go person and I have a lot of energy. And when I'm coming to something and I see all the issues that need to be fixed, it's like, okay, let's take the toolbox out. Let's go fix everything. And that includes driving change.

(43:03):
And I've seen that when I started doing that without building that understanding of why we need to do a change or why this is a problem that we need to go and fix it, then you don't take people with you through that journey. So really analyzing that not everyone appreciate change the way you are, not everyone has that mindset of the go, go, go, let's go do it. And really figuring out, taking a step back and assessing what is happening so you can take the team with you on that journey of changing.

(43:35):
That was for me, the biggest learning and likely a lot of the not supportive feedback I got from the team at that time was, "You're moving too fast. Slow down. Explain the why. Why are we doing that? How should we move forward?"

Lenny (43:52):
Where did this actually happen? Which company? Which role?

Inbal Shani (43:55):
In TomTom when I was leading the location-based services team. And I think for me it was one, it was the first time I was working in international company, so really figure out that my character not always fly with every culture that exists. So how am I adjusting to that? And the second thing is that they were very accustomed in working in a specific environment in a specific way. And yes, I was hired to drive change, but one, the team doesn't have to accept. That's your job to drive change.

(44:31):
And also they're not necessarily on board with the fact that you're here to drive change. So how you take them with you through that journey was a big learning and being able to communicate in a general way of communicating to drive clarity, that was a big learning.

Lenny (44:48):
That's actually a recurring theme on Failure Corner of the failure stories I'm thinking about is just somebody starting at a company and trying to change too much too quickly.

Inbal Shani (44:55):
Right. It's very common because we are human beings. We think that if we're coming, we have our experience, we're coming to a new space, and you immediately see all the things that are not working or all the things that needs to be fixed. If you're working in the same space for a long time in the same team, you often don't see these gaps anymore because you got used to living with them.

(45:15):
So as someone new, you're coming in, you immediately see all these holes and cracks. And it's like, okay, here's all the things I need to fix. But you have a team that has been there for what? So how you find that bridge to communicate between the things you see and the things that they think is fine. Like, "Why are you driving these changes? It's be working. Don't fix it."

Lenny (45:35):
Inbal, is there anything else you'd like to share before we get to our very exciting lightning round?

Inbal Shani (45:40):
For me, it's an exciting moment in time. I've been celebrating my first year in GitHub and my first GitHub Universe on stage last week. It was amazing experience for me to meet our customers, our partners and talk a lot about the importance of developer experience, our AI power platform, and how we're shaping the future. So I'm in a very exciting part of my journey with GitHub.

(46:05):
You don't get here if you don't make some mistakes and you do some learnings and you have some successes and then you take the right turn and sometimes you take the wrong turn, but you find your way to a place that makes you happy and feel fulfilled as a product leader.

Lenny (46:19):
Awesome. We're going to link to that talk in the show notes that people want to watch it. With that, we've reached a very exciting lightning round. Are you ready?

Inbal Shani (46:26):
I'm ready.

Lenny (46:28):
What are two or three books that you've recommended most to other people?

Inbal Shani (46:32):
Failing Forward by John Maxwell, The Flywheel from Good to Great by Jim Collins, and a recent book that I read that is called Dare to Lead Like a Girl by Dalia Feldheim.

Lenny (46:45):
That's a new mention on the show. Awesome. What is a favorite recent movie or TV show that you really enjoyed?

Inbal Shani (46:51):
I like a lot of fantasy and I like a lot of history based movies and theories. There is a recent one that came up on Netflix, All the Light We Cannot See. Amazing. So well produced. Really tells an interesting part of the history of World War II.

Lenny (47:06):
Have you seen Wheel of Time on Amazon Prime if you like fantasy?

Inbal Shani (47:09):
Yeah. Yes., I love that. It's done. It's a good one.

Lenny (47:13):
Yeah, especially season two is like wow. It's a lot better. Next question, do you have a favorite interview question you like to ask candidates when you're interviewing them?

Inbal Shani (47:22):
I think the first question that I really like to ask is, what is the most innovative thing you have done and why do you think it's innovative? And it's really interesting that there are some people that think they need to answer about the biggest invention that they've done, and there are some people that are very vulnerable and they talk about something very personal that they have innovated.

(47:41):
It shows a lot of their character. And I think the second question that I like to ask a lot is give me an example in a time where you had a disagreement with your manager, you're in the line with your manager, and then what did you do about it and how did you go? Because it showcase a lot about your character and are you willing to stand your ground and push up when you need to? And then what is that communication skills that you have, your influential skill that you have?

Lenny (48:09):
Do you have a favorite life motto that you like to share with people, often come back to either in work or in life that you find useful?

Inbal Shani (48:15):
I think it's, if you don't take risks, you cannot create a future. I forgot who said it. I think it's from one of the animation Monkey Luffy if I remember. But it basically summarized the life motto that you have to take risks, you have to experiment. If you feel comfortable, it's not a good thing. You always need to feel uncomfortable to stretch yourself to go to the next thing. So that's something that I've done. You just heard about my career story from applied scientist to chief product officer. Who knew?

Lenny (48:46):
I love that motto. lnbal, thank you so much for being here. Two final questions. Where can folks find you online if they want to reach out and follow up on anything? And then how can listeners be useful to you?

Inbal Shani (48:57):
Lots of interesting sessions and talks from Universe. So if people want to learn more about what is it that we're doing, how we're thinking about AI, LinkedIn is likely the best social media platform to find me where I have a chance to talk to a lot of people. These are the best places.

Lenny (49:12):
And then how can listeners be useful to you?

Inbal Shani (49:16):
If you can share a similar experience or a story that you think will be helpful for me as I'm thinking about, what does that mean being chief product officer for GitHub, any tips and tricks on how you use GitHub, so maybe I can learn, or share your experience and story so I can learn from your experience as well.

Lenny (49:31):
Amazing. lnbal, thank you so much for being here.

Inbal Shani (49:35):
Thank you so much for having me.

Lenny (49:36):
Bye, everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

