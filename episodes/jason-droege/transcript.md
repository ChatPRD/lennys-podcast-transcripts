---
guest: Jason Droege
title: Scale AI CEO on Meta's $14B deal, scaling Uber Eats to $80B, & what frontier
  labs are building next
youtube_url: https://www.youtube.com/watch?v=W99jdYZOlN0
video_id: W99jdYZOlN0
description: Jason Droege is the CEO of Scale AI, a company that provides foundational
  training data to every major AI lab. He previously co-founded Scour with Travis
  Kalanick.
duration_seconds: 5042.0
duration: '1:24:02'
view_count: 17470
channel: Lenny's Podcast
keywords:
- growth
- onboarding
- churn
- roadmap
- iteration
- revenue
- hiring
- culture
- leadership
- management
- strategy
- vision
- mission
- positioning
- competition
---

# Scale AI CEO on Meta's $14B deal, scaling Uber Eats to $80B, & what frontier labs are building next

## Transcript

Lenny Rachitsky (00:00:00):
There's been a lot of talk these days about AI not delivering on the promise that we hear, especially at enterprises.

Jason Droege (00:00:06):
These things take 6 to 12 months to get them truly robust enough where an important process can be automated. Like with any of these major tech revolutions, headlines tell one story and then on the ground, laying broadband means you need to dig up every single road in America to lay it. Someone's got to dig up the road or someone's got to run the undersea cable.

Lenny Rachitsky (00:00:26):
Is there anything you think people don't truly grasp or understand about where AI models are going to be in the next two, three years?

Jason Droege (00:00:31):
The general trend right now is going from models knowing things to models doing things. The next question becomes, what can it do for me? How does the agent make decisions for you?

Lenny Rachitsky (00:00:39):
Let's talk about Scale and this whole world of AI that you're in, you essentially pioneered data labeling, trading data, creating evals for labs.

Jason Droege (00:00:46):
18 months ago, you would get a short story and it would say, "Is this short story better than this short story?" And now you're at a point where one task is building an entire website by one of the world's best web developers, or it is explaining some very nuanced topic on cancer to a model. These tasks now take hours of time and they require PhDs and professionals.

Lenny Rachitsky (00:01:07):
I've talked to a bunch of people that have worked with you over the years, and I heard a lot about just how high of a bar you set for new businesses.

Jason Droege (00:01:13):
From an entrepreneurship standpoint, it truly is about what insight do I have? Why am I so lucky to have this insight? Why in a world of a million entrepreneurs who are thinking, who are smart, who are trying everything, why am I in the position where I likely have an insight that others do not?

Lenny Rachitsky (00:01:31):
Today, my guest is Jason Droege. Jason is the new CEO of Scale AI. This is the first interview that he's done since taking over for Alex Wang after the Meta deal. Alex now leads the super intelligence team at Meta. Prior to Scale, Jason co-founded a company with Travis Kalanick. Before, he started Uber, worked at a couple startups. Most famously, Jason launched and led Uber Eats, which went from an idea that he and his team had to what is now a multi-billion dollar run rate business and one that basically saved Uber during the pandemic when nobody was taking rides. This interview is following a theme that I've been following through a bunch of interviews, which is the evolution of how AI models actually gets smarter. Along with scaling, compute and improving the actual model code, much of the improvements we're seeing in ChatGPT and Claude and every frontier AI model is these labs hiring experts to filling gaps in their knowledge and correcting their understanding of how things work, and basically showing them what good looks like in every domain that consumers are using models.

(00:02:35):
Scale was the pioneer in this space. They created the category, and in our conversation we talk about what is happening at Scale and just how this deal with Meta worked, what experts like doctors and software engineers are specifically doing to help models get smarter, how the whole market of data labeling and evals and data training has changed from when Scale entered the market to today, and also just how long will we need humans to keep helping AI get smarter. We also get into where Jason sees models going in the next few years because they have such a unique glimpse into the future. We also talk about a ton of really unique and really important product lessons from the course of Jason's career, including a bunch of advice on how to start a new business, both startups and within existing companies, and also a bunch of advice on hiring and leadership and so much more.

(00:03:21):
A huge thank you to Allen Penn and Stephen Chau for suggesting topics for this conversation. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It helps tremendously. And if you become an annual subscriber of my newsletter, you get a year free of 15 incredible products including Lovable, Replet, Bolt, n8n, Linear, Superhuman, Descript, Wispr Flow, Gamma, Perflexity, Warp, Granola, Magic Patterns, Raycast, ChatPRD, and Mobbin. Head on over to lennysnewsletter.com and click product pass. With that, I bring you Jason Droege.

(00:03:53):
This episode is brought to you by Merge. Product leaders hate building integrations. They're messy, they're slow to build, they're a huge drain on your roadmap, and they're definitely not why you got into product in the first place. Lucky for you, Merge is obsessed with integrations. With a single API, B2B SaaS companies embed merge into their product and ship 220 plus customer facing integrations in weeks, not quarters. Think of Merge like plaid, but for everything B2B SaaS. Companies like Mistral AI, Ramp and Dorada use Merge to connect their customers as accounting, HR, ticketing, CRM, and file storage systems to power everything from automatic onboarding to AI-ready data pipelines. Even better, Merge now supports the secure deployment of connectors to AI agents with a new product so that you can safely power AI workflows with real customer data. If your product needs customer data from dozens of systems, Merge is the fastest, safest way to get it. Book and attend a meeting at merge.dev/lenny and they'll send you a $50 Amazon gift card. That's merge.dev/lenny.

(00:04:59):
This episode is brought to you by Figma, makers of Figma Make. When I was a PM at Airbnb, I still remember when Figma came out and how much it improved how we operated as a team. Suddenly, I could involve my whole team in the design process, give feedback on design concepts really quickly, and it just made the whole product development process so much more fun. But Figma never felt like it was for me. It was great for giving feedback and designs, but as a builder, I wanted to make stuff.

(00:05:25):
That's why Figma built Figma Make. With just a few prompts, you can make any idea or design into a fully functional prototype or app that anyone can iterate on and validate with customers. Figma Make is a different kind of vibe coding tool. Because it's all in Figma, you can use your team's existing design building blocks, making it easy to create outputs that look good and feel real and are connected to how your team builds. Stop spending so much time telling people about your product vision and instead show it to them. Make code-backed prototypes and apps fast with Figma Make. Check it out at figma.com/lenny. Jason, thank you so much for being here and welcome to the podcast.

Jason Droege (00:06:08):
Yeah, thanks for having me. Excited to be here.

Lenny Rachitsky (00:06:10):
As I was researching your background and prepping for this podcast, I learned a really interesting fun fact about you that I don't think a lot of people know. So Travis Kalanick, he had a startup before Uber. It was called Scour. It was a peer-to-peer file sharing app, and then I think got shut down. You were his co-founder. This was the early part of your career. I'm guessing there are hours of stories we could talk about during this experience. So let me just ask you this one question. What's just a lesson that has stuck with you from that experience that you've taken with you to future places you've worked and built product at?

Jason Droege (00:06:44):
I mean, there's so many lessons. I like to pick one. I think that the main lesson is that in business and in startups, everything's negotiable. I think that's the main thing. Because we were 19 at the time, 19, 20 at the time, we built this search engine in a dorm room and we were running it out of the dorm room and our first URL was scour.cs.ucla.edu. These things were not necessarily in fractions at the time, but we were just being practical. It was basically a project that we had started, and so we built the search engine and people started using it and we thought we would get in trouble, but it turned out the computer science department was excited about it even though we had basically parked a domain on their servers and we were using our own computers in the dorms to serve up this website and product.

(00:07:46):
And then, when we got into financing, the financing process was fascinating, and this is where the everything is negotiable lesson came from, which is, it was Ron Burkle and Mike Ovitz, who are the initial investors in the business. We were in LA, so we were at UCLA, so we were not quite wired into the entire Sand Hill Road scene. And as we were doing the deal, the terms kept changing on us. We thought you went and raised money and it was like, "Oh, we'll get a few million dollars at a $5 million valuation." This is back when that was actually a series A valuation. And then over the course of the deal, it was like, "We're doing the deal. We're not doing the deal. Oh, you should give us 50% of the company. Oh, you should give us 75% of the company. Oh, if you want to sign the document today, this person's going to show up for breakfast and if you don't sign today and give us 80% of the company, the person's not going to show up."

(00:08:38):
It was just completely wild, the things that we saw from day one of what can happen in business, and we thought there was a way to do things, and at a very young age we realized there is no way to do things. There is just the way that you can negotiate your way through the world, which I actually think influenced Travis heavily and then me later heavily at Uber in terms of if you can imagine it and it makes sense and you can align incentives, then it can happen. But there is no way. And to learn that at 19 or 20 years old I think was highly imprinting.

Lenny Rachitsky (00:09:12):
That is an amazing lesson. What happened to Scour? It got shut down, I think. What happened there?

Jason Droege (00:09:16):
Well, yeah, so basically what Scour was was it was a multimedia search engine and then peer-to-peer file sharing network. But what it was used for was finding free content. And at the time, the laws were on this were pretty ambiguous because we weren't, mix tapes were legal, but this was like a hyperversion of that. But we were eventually sued for a quarter of a trillion dollars. So I guess if you're going to experience something that's potentially as life devastating as that, doing it when you're, I think we were 21 or 22 at the time is the time to do it, but it was just this very cold splash of water about how the real world really works, because the MBAA and the RAA were the ones who sued us, the entertainment industry sued us or the associations that represent the entertainment industry, and then they settled it for $1 million.

(00:10:08):
So we're like, "Wait, you wanted a quarter of a trillion dollars and then you settle for $1 million." And of course they were just trying to drive us in a bankruptcy, drive us out of the market, and these are established companies. So we're like, "If these guys don't have a playbook to follow, they just make up numbers, then wow, how should we navigate the rest of our lives?"

Lenny Rachitsky (00:10:28):
Let's talk about Scale and this whole world of AI that you're in. This is the first interview that you're doing since taking over CEO at Scale. I'm honored to have you here to talk through this stuff. This is also the first interview you're doing since the whole Meta deal, which is very complicated, confused a lot of people. So I'm just curious to hear the current state of Scale, what people should know. For example, what's your relationship with Meta? What's your relationship with Alex? What is the current state of Scale?

Jason Droege (00:10:55):
Yeah, so Scale is a fully independent company. The transaction was Meta invested a little bit over $14 billion to get 49% of the company, non-voting stock, didn't take a new board seat. Alex fills the board seat. So the board is the same, the governance is largely the same. There's no preferential access to anything that Meta has. There's no preferential relationship. I mean, we've had a longstanding relationship with Meta on the data side of the business for a long time and even on some business development related things to maybe working on things in government together, et cetera. And so, those might get bigger just as we're closer now, but there's nothing that prevents us from doing things with other parties and they have no access to anything that they wouldn't have had otherwise. All the privacy still in place, all the data security still in place that was there before.

(00:11:47):
And in fact, only about 15 people went over in the transaction. So Scale has about 1,100 employees or so now, and we have two major businesses. Each of those businesses, each of them has hundreds of millions of revenue. So we have two unicorns inside the company today that sustains. The business has grown every month since the deal happened, which I've read, the reporting is not consistently reported. We haven't talked about it, so this is part of getting the word out and we're excited to continue to build, deliver data, and do what we did before.

Lenny Rachitsky (00:12:20):
So the company today, independent, its own company. Alex, just to be clear, he works at Meta now. He's no longer at Scale.

Jason Droege (00:12:26):
Yeah, that's right. Excuse me, I should have talked about that more.

Lenny Rachitsky (00:12:30):
I think that's really interesting. So basically, it was an investment. Some people left to join Meta, the company continues, you're running the ship. Let's talk about this whole space that you guys essentially pioneered, I don't know best way to call it, data labeling, training data, creating evals for labs. You guys were at this before anyone even knew this was a thing. I know even Scale pivoted into this market from other things. I think there was a bunch of stuff they tried with self-driving cars and all these things, and then it's like, "Oh shit, AI labs need this data."

(00:12:57):
One of the main stories I've been hearing is, and I've had a bunch of CEOs from this space on the podcast, is that there's been this big shift from the way, from what Scale had pioneered and had been doing for a long time, which is generalists, low-cost labor training. From that to now, labs mostly need experts, lawyers, doctors, engineers doing training, writing evals, things like that. I'm curious just what you're seeing, how that's impacting you guys, where you think things are heading, what people should know about this whole market of data training data.

Jason Droege (00:13:27):
Yeah, totally. I think the current positioning out there from competitors is just bogus. So I'll start with that and then maybe talk a little bit about, I'll explain what I mean by that in a second. But I think it's important to just give 30 seconds on what the history of Scale is and what's the thread going back to 2016. So Alex had this insight in very early days that the important thing to models was data. And I think he was 19 or 20 years old at the time as well. And so, he's like, "Okay, well what business would I create around this?" And the business that he created around it was, okay, let's do labeling for autonomous vehicles, because if you label the data that they have, the cars do better. And then, that wave turned into the computer vision wave, which we have a relationship with the Department of Defense where we do labeling for them, and that was in 2020.

(00:14:21):
And then, you move forward and the models have gotten better over this period of time. And so, as models get better, they need different types of data. So we've constantly been adapting to the type of data that models need to be successful. And so, then the gen AI wave hit, and this went through the moon or to the moon. And so, as part of that, that industry is changing constantly too. So it is correct that when the models came out two or three years ago, I mean we remember using them, they would hallucinate all the time, they would get basic answers wrong, they didn't know which poem was better, this poem or that poem. And that was the state of labeling a couple years ago. And things have changed quickly and we've changed with it. And now the state for everyone, and we've been at the forefront of all of this, is expert data labeling, more sophisticated tasks.

(00:15:15):
So to give you a sense of what the task was 18 months ago, I've been here about 13 months. So I was interviewing and I remember seeing it. You would get a short story and it would say, "Is this short story better than this short story?" And then you would edit it and be like, "Yeah, it would be better if it was this," and you would give some preference ranking to it. It was pretty basic 18 months ago, and you had the rise of some experts, but the models were so far behind that they needed just even the basic stuff they needed. And now, you're at a point where a task is, one task is building an entire website by one of the world's best web developers, or it is explaining some very nuanced topic on cancer to a model. And these tasks now take hours of time and they require PhDs and professionals.

(00:16:01):
So to give you a stat to back this up, 80% of the people that we have on our expert network have a bachelor's degree or greater, which is very contrary to some of the positioning that's out there and some of the understanding of this industry. About 15% have a PhD that's greater, and we have PhDs on the network earning significant amounts of money doing labeling, contributing their expertise to these models. So we've been doing expert data labeling ever since the models need it. I mean, this game is keeping in touch with the researchers, knowing what they need, coming up with ideas internally. In some ways, we drove this because we were seeing that the models were not sufficient in more expert ways. And so, we would go to the model builders and say, "Hey, we noticed that this is a problem. If you would like to fix it, this cadre of experts can do that for you." So the counter positioning is out there, but I think that's just what competitors say sometimes. It has nothing to do with reality.

Lenny Rachitsky (00:17:02):
Okay. That was extremely interesting. So what I'm hearing is yes, there has been a big shift to labs need more expert folks involved in training, labeling, writing evals. You guys are very aware of that and have evolved with that. One of the, I don't know, allegations I guess in the market is that it's hard to find these experts. So all these companies have their proprietary network of experts and how they find them. Is there anything you could share about just how you guys go about that because that feels like the hardest part is finding these experts and keeping them from other companies?

Jason Droege (00:17:33):
They are hard to find. You have to have many, many tactics. So we get, as you would expect, there's not one way you do it. The largest way is that they refer each other because when you are enjoying what you're doing and you are using your expertise to contribute to AI, which is pretty cool. If you're a PhD on this pretty specific topic and you're using a model and you're frustrated that, oh, it doesn't interact with me in the way that I want, this is a paid way to have an outlet for that and to make hundreds or thousands of dollars doing that. And so, a lot of times they refer each other.

(00:18:13):
We also have campus programs where we will literally go onto the campus and talk to the professors, talk to the students, ask about who would like to do this type of work. And then, of course, there's the more traditional scaled ways of LinkedIn and places like that. But the best ones come from these grassroots and referral networks. And the only way you get that is providing a great experience to these people, because these people, they're doing it partly for money, but they're also doing it because they think that their contribution to the AI models is important and interesting, and in many times it solves a problem for them.

Lenny Rachitsky (00:18:48):
So something that I've been seeing on Twitter just this week as I was preparing for this is there's the information headline. This came out and this mirrored something that Brendan from Workhorse said that over time the entire economy is going to move towards just reinforcement learning and everyone's just training AI is basically the jobs that will be left. Thoughts on that? Is that where you think things are going? Is there another perspective?

Jason Droege (00:19:12):
Reinforcement learning is very important, and I think this is a broader comment about the move to environments. There's these things called RL environments that effectively are sandboxes for AI agents to play in to accomplish a goal so that they can learn how to accomplish that goal. We've been doing this for over a year. So for example, you have a Salesforce instance. How does an AI agent navigate that instance? That instance has data that it needs to recognize, it has configurations. Salesforce is a highly configurable product. It has configurations, it needs to understand how to navigate. You're asking the agent to do a business process that needs very high reliability, and then the agent needs to know, "Hey, if I can't accomplish what I'm going to accomplish, or I think if there's a low accuracy of what I'm about to accomplish, how do I pop it up to a human being for feedback so I can get guidance?"

(00:20:08):
All of those things need to be trained and there's no alchemy to it. You just have to put the AI agent in an environment that represents what a human being would be doing. And you can imagine the number of environments in the world and the number of goals within each environment is enormous. So the question is, and the research that we have done over the past year to try to be a good partner to our model builders, our model builder customers, is how generalizable is each individual task or each individual environment. So if you imagine the world of environments of software systems, configurations, data types, sizes, user counts, complexities, it's like the permutations are endless. So what you need is you need a strategy that allows a lab to collect data that is generalizable enough across a broad spectrum of use cases so that they don't have to collect 45 trillion combinations of what should the agent do in this particular situation.

(00:21:20):
So sometimes the work and the data is highly generalizable, and by generalizable I mean you have it accomplished in a simple way. The task might be find the meeting on my calendar for my interview with Lenny, and the agent goes and it looks through all my calendar and then it pops it out, very simple example. That needs to be generalizable to any calendar search potentially or potentially any calendar action. And the more generalizable it is, the more valuable the data is. So our job is to provide the most valuable data to model builders that accomplishes the goal of making agents as useful as possible for their end users.

Lenny Rachitsky (00:22:03):
I love that you've been sharing these examples of what this stuff is specifically that these people are doing, the data you're providing to labs. So just to mirror back a few of the examples you've shared, one is an engineer building a website, sharing the code essentially with the model. And here's how I would do it. And in that example, is it just like here's the code or is it a recording of them building it? What is the data?

Jason Droege (00:22:30):
It could be both. So in some cases, it's just the website and here's an example, and then they design it. In some cases, it needs to be annotated in such a way that's like, I made this decision for this reason or this decision for that reason, or here's how I would think about it. So it depends on what the model builders are trying to accomplish. And so, it can get quite nuanced in terms of what they're trying to train on.

Lenny Rachitsky (00:22:54):
Got it.

Jason Droege (00:22:54):
So it's not like here's a website and then it's created doing websites. It's like, here's a website, here's why I made this decision, here's why I didn't make this decision, or here's a broken website and here's why it's broken if they're trying to accomplish, I don't know, a debugging tool for a website builder or something like that.

Lenny Rachitsky (00:23:09):
And another example you shared is a short story where it's like, here's one short story, here's another I imagine generated by a model. And then it's like, which is better, and then how would you make it better? The other example you just shared is a Salesforce agent where it's like, Hey, book a meeting with a prospect and then teach it how that happens. I love just how concrete these are because it's like, okay, I get it. This is the stuff that these companies do. Is there another maybe one or two examples just to give people a sense of what this data looks like?

Jason Droege (00:23:33):
Absolutely. I can actually give you an example from, so we have two sides of our business. One, we supply data to model builders. We sell the data, and then the other is we actually do solutions. We sell applications and services to healthcare systems, insurance systems, et cetera. I actually think it would paint a more colorful picture if I gave you an example of one of those because it involves data, but it involves the use of data, the manipulation of data for a very, very specific goal. And so, one example there is we work with a healthcare system and health systems have lots of problems. This particular healthcare system has experts that see very rare cases on a regular basis. So you go there only if no one else can figure out your problem, and there's a huge backlog. So there's a productivity element to this implementation tier.

(00:24:27):
So there's a huge backlog. They want to be able to see more patients, they want to be able to provide better care, and they want to prevent the number of revisits because they want to give the accurate diagnosis day one and what the treatment should be. Well, to do this today without the help of AI, the doctor really needs to read 200 to 300 pages of documentation and it's rolled into one document, but in different formats. And so, if you're a doctor, how are you going to read 200 or 300 pages of everything? So what they do is they do the best they can. They scan it, they ask a nurse to look at it, they ask maybe a more junior doctor to take a look at this case. They want to treat the patient well, obviously this is why they became a doctor. And then, they go into the room and they talk to the person and then they make a diagnosis.

(00:25:14):
Well, we basically built a tool that will read that document for them and point out the top 5 to 10 things that they should take into consideration, either allergies that might not be obvious is one example where we actually, we picked up on an allergy that a patient had that would not have been obvious from reading the document and that allergy actually would've had a conflict with the medication that they were going to be prescribed. And so, the AI tool basically pulled out this correlation that would've even been hard for a human being to do. To make this tool better and better, you get to a certain limit with the models off the shelf, and actually the people inside of this healthcare system have to do their own labeling.

(00:25:54):
So we talk about labeling for model builders, but we are starting to see the labeling move into enterprises and into governments because you can only get so far with off the shelf plus rag plus some fine-tuning based on recorded data. One thing people often miss about these systems is we assume because you hear these numbers of like, "Oh, this bank in just 200 petabytes of data a year or whatever fantastical number." What we miss is is that the right data? Which of that data is useful to the models? And most of it is not useful. Some of it is, but a lot of what we do when we're talking about knowledge work, when we're talking about making judgment is human judgment based on synthesizing how would this doctor in this case or how would this banker in this case make this decision and how would they make decision in the context of their overall enterprise? And that might be different bank to bank, healthcare system to healthcare system, because of the culture, the objectives, the incentives, et cetera. And so, we're getting to the point now where we see that digitizing judgment, human judgment, true subject matter, deep expertise is becoming a bottleneck that we're unblocking for our customers.

Lenny Rachitsky (00:27:05):
That's really interesting. It's like the spectrum went from just low skill generous labor to experts to now the specific expert at this one company who needs to do this work, this labeling.

Jason Droege (00:27:16):
Absolutely. I mean understanding what, there's this broad narrative. We have two narratives. We have the AGI, everything is just going to become AGI, and then there's the skeptics, which is like, "Hey, this is all bunk, this is a bubble, et cetera." And of course, my view is most things are kind of like there's truth in between and some of the extreme parts of the extreme probably correct, but the reality is is that it's very hard to get machine critical use cases in agentic systems where agents are talking to agents to a level of accuracy that is necessary to accomplish a goal. And one of the main issues is that a one document, think about the problem of even understanding a document, a document that reads the exact same words in company A will have a different meaning and importance in company B. So how do you have a system that knows that? So this is all got to be built. So if you're going to make good decisions.

Lenny Rachitsky (00:28:18):
This is a good segue to this question that is always on people's minds when they look at companies like yours and the other folks in the space is just how long do we need people to be doing this? At what point will AI be smart enough to do it themselves? I know your incentives are to say we'll never run out of people because it's aligned with your growth, but just how should we think about just why do we need people, I don't know, in 10 years? How long do we need these experts telling AI things it doesn't know?

Jason Droege (00:28:42):
First off, the history of data labeling is a history of new beginnings. Autonomous vehicles do not need as much data labeling as they did in the past. I mean, Scale is a company that believes that data will always be important at the point at which you don't need external data, human data in models. I think we've gotten to a level of advancement in the world that is almost like unfathomable because you're effectively saying that no new human skill and no new human knowledge is important enough to put into these models. That feels like pretty far out there. And so, for a business like ours, we're constantly looking at how do you build operations that can constantly find the new needs and then work with the contributor network we call the experts contributors to unearth that data, to unearth that information. And sometimes it's new people, sometimes within our existing base we find that existing people have expertise that we didn't know about that maybe wasn't useful to a model a year ago, but now is useful.

(00:29:47):
So this is a constant progression of getting more and more data into these models. Yes, we are financially incentivized to believe that humans will always be in the loop, but that's not just a business belief, it is a personal belief. These systems need to work for us, and if these systems work for us, then we will need to be on the loop or in the loop on any of the decisions that these systems make. As to the broader point around labor, which I think comes up around white collar apocalypse and these things that come up, I'm definitely on the more maybe practical side of this, possibly just because of my nature, possibly because I see what's going on on the ground actually in these customers where supposedly this transformation is going to happen in the next one to two years. And I just think that it might happen. The space is moving super fast, but I don't think it's going to happen.

(00:30:39):
It is definitely not going to happen in the next year. The idea that it happens in the next two years I think is very far-fetched, but nothing's impossible here. And long-term, I think that if you go back through, I don't know, pessimist archive or whatever, these accounts that post, the radio was invented and then all of this will be eliminated. There will be change, but the change, I think humans are very good at adapting. So I think what we're underestimating in all of the doom and gloom is we believe in human adaptability. We as a company are highly adaptable and I think the history of technology has shown that people are adaptable.

Lenny Rachitsky (00:31:14):
I really like that takeaway. I'm an optimist as well, so I'm always looking for reasons to be optimistic. I want to follow that thread before I get there, something very tactical I want to ask about is evals seems to be coming up a lot, especially with companies in your space. I'm still learning a lot about just what this all is, especially in your market. How much of what you or experts are providing are evals versus other types of data?

Jason Droege (00:31:40):
A lot of it's evals, and within enterprise customers and government customers, it's mostly evals because somebody's got to establish the benchmark for what good looks like. That's the simple way to think about evals. What does good look like and do you have a comprehensive set of evals so that the system knows what good looks like? It's as simple as that.

Lenny Rachitsky (00:32:00):
So in the case maybe of the healthcare example you shared, essentially this doctor would be sitting there looking at all these reports, creating evals that are like, this is what this should be discovering in this report, in this record. Is that a way to think about it?

Jason Droege (00:32:15):
Yeah, that's a very big part of it, which is what does good look like?

Lenny Rachitsky (00:32:19):
Awesome, okay.

Jason Droege (00:32:20):
I have to reduce things down to simple terms.

Lenny Rachitsky (00:32:24):
It's interesting you say good versus correct. Is that a specific term you like to use good versus just this is the correct answer.

Jason Droege (00:32:31):
I didn't intentionally use that word, but these are probabilistic systems and so depending upon... Yeah, so I can get into some nuance here about the right types of problems that AI is good at solving. So if you have a human process that is 10 or 20% accurate or 10 or 20% liked, AI is awesome. Because if you get to 50, 60, 70, 80% accurate, you're in the money, you're in the green, everybody's happy. Now, the system then has to know, hey, for the remainder, how do I make sure that humans are involved for the remainder of the decision making? But from a net value add standpoint, the humans are pumped in that scenario.

(00:33:13):
If you have a human process, a workflow that is 98% accurate, and you expect an AI system to get you the remaining 2%, not totally there yet. And so, when I say what does good look like? A lot of the processes and a lot of the things that people are asking these systems to do and systems for us to build are making judgments on their behalf. And so, just like we would ask a human being, "Hey, what do you think we should do in this scenario?" What you're looking for is you're looking for the best recommendation or course of action given the current information.

Lenny Rachitsky (00:33:48):
To you, this is so obvious and to people in your market that I think a lot of people think about AI being trained on just here's a bunch of data, check it out, learn everything you can from all of human history and all of written record. But what's wild is basically people are sitting around teaching AI things it doesn't know, filling gaps. That's how AI is getting smarter now. There's no more real data for it to feed on. It's just like, here's what I don't know, or here's what an expert found you're wrong. I'm going to teach you this. And the fact that it scales and that's keeping models improving is so mind-boggling.

Jason Droege (00:34:21):
Yes. No, yeah, I agree. I mean, like with any of these major tech revolutions, the headlines tell one story and then on the ground, laying broadband means you need to dig up every single road in America to lay it. There is the, yeah, it's as simple as that. Someone's got to dig up the road or someone's got to run the undersea cable. There's always some operational chiseling that's going on in all of these industries. I mean, if you think about how magical these models are, they're remarkable that if you've been in technology long enough, it blows my mind even today that they get the punctuation right consistently. I mean, that sounds like almost daft to say at this point in the market, but if you were to go back three years and think about that from a technological standpoint, a lot of things that we think are trivial now are very sophisticated, and it's a combination of, I mean, the real answer is it's a combination of computational power, model improvement, and data, and all three are getting better at once.

Lenny Rachitsky (00:35:25):
Let's follow that thread. You've been at Scale for a long time, CEO for, you said, 13 months. I feel like you see a lot more about where things are heading because you work with labs on things they haven't even announced yet. You see more than most people, and I know there's only so much you can share about what companies are doing, but just is there anything you think people don't truly grasp or understand about where AI models are going to be in the next two, three years?

Jason Droege (00:35:47):
Look, there's so much talk. I think it depends on how much X or news you consume. So I think it's like what sort of our perspective. The general trend right now is going from models knowing things to models doing things. And we're pushing the boundaries of knowledge, like the benchmarks that we put out and that others put out are showing that the knowledge that these models have is getting, it's quite robust. And then, the next question becomes, well, what can it do for me? And as soon as you get into that world, that's where the environments we were talking about start to come into play. How do you navigate a Salesforce instance? How do you navigate a healthcare system? How do you navigate even a weather app on your phone, and how does the agent make decisions for you?

(00:36:36):
We're just getting into the beginning of that. It'll be very interesting to see how quickly that happens. And I think that's where a lot of the speculation has a wide variance because we're at the beginning of it. People take different trajectories on how that's going to improve. And so, if you take a trajectory of the most aggressive trajectory, which is like, oh, it's actually going to be quite easy to train on these things, and then it's just a change management exercise in the economy, which by the way, change management exercises are not to be underestimated.

(00:37:06):
There's still people in the world without an email address. And so, the adoption curve then becomes a human and policy issue, not a technological issue. We're not there from the technology standpoint, but I do think in the next two to three years, if I take the bait and have to make a guess is the technology will get to a point where it will push the change management and policy makers to say like, "Oh, what do we do with this because it's getting pretty close?" That's probably two or three years away.

Lenny Rachitsky (00:37:35):
There's been a lot of talk these days about AI not delivering on the promise that we hear, especially at enterprises. There's this MIT study that just showed that there's all these pilots that people are excited about and then they don't work and companies aren't adopting these tools. There's data showing engineers are not actually as productive with tools. It actually slows them down sometimes. You work with a ton of companies implementing all kinds of AI. What are you seeing on the ground? What kind of gains are you seeing? Do you feel like it's overhyped, underhyped?

Jason Droege (00:38:03):
There's a lot of hype out there, and our job is to actually build products that work, that deliver value for our customers and figure out where the rubber hits the road. And to get a sophisticated, my healthcare example is one, we do other sophisticated workflows, claims management for insurance companies. This is a financial decision that's happening, but it's an automatable process. But basically what happens is the POCs get to 60 or 70% of the way there, and the human mind goes, oh, the rest is no big deal. But it's like uptime in data centers where every nine is an order of magnitude investment in terms of reliability, backups, et cetera. One nine is basically a web server in a dorm room like we had at UCLA, and then five nines is this crazy high bar, but it just seems like a very small movement.

(00:38:55):
So you have a similar dynamic going on here where you have a bunch of people, one of the reasons why the POCs have failed, one, there's a denominator effect because it's so easy to do, "Hey, I spun up a project, I spun up a project, I spun up a project." So it's really easy for people to try. So I don't necessarily know that the 95% number, I think is a bit of clickbait in a way. It tells the right story, but it is a little bit hyperbolic because if you take the efforts that happen in the company where they actually get a quality partner like we are, or if you do it yourself, if you have engineers who've worked with models before and they put in the time, and I'm talking about months, not like minutes like you see in these videos to actually get legal approval, policy approval, regulatory approval, change managements like an accuracy that everybody's comfortable with. If you actually do that, these things take 6 to 12 months to get them truly robust enough where an important process can be automated.

(00:40:00):
So I think that's where the hype is right that when you do it, the impact is like, whoa, I never would've figured that out myself, and I'm one of the most educated doctors in the world as an example. But the time to get there is just longer than what people are selling.

Lenny Rachitsky (00:40:17):
It's such a good point that it's not only is it easy to try these things, it's just like everyone's doing it so everyone's feeling FOMO like, "I got to try these things. I got to try all these prototyping tools, Cursor, all these things." Just goes, "Everyone's doing it," and then you just rush into it and it doesn't actually work out.

Jason Droege (00:40:31):
Easy to learn, hard to master. That's my summary.

Lenny Rachitsky (00:40:36):
This episode is brought to you by Mercury. I've been banking with Mercury for years, and honestly, I can't imagine banking any other way at this point. I switched from Chase and holy moly, what a difference. Sending wires, tracking spend, giving people on my team access to move money around so freaking easy. Where most traditional banking websites and apps are clunky and hard to use, Mercury is meticulously designed to be an intuitive and simple experience. And Mercury brings all the ways that you use money into a single product, including credit cards, invoicing, bill pay, reimbursements for your teammates and capital.

(00:41:11):
Whether you're a funded tech startup looking for ways to pay contractors and earn yield on your idle cash, or an agency that needs to invoice customers and keep them current, or an e-commerce brand that needs to stay on top of cashflow and access capital, Mercury can be tailored to help your business perform at its highest level. See what over 200,000 entrepreneurs love about Mercury. Visit mercury.com to apply online in 10 minutes. Mercury is a FinTech, not a bank. Banking services provided through Mercury's FDIC-insured partner banks. For more details, check out the show notes.

(00:41:44):
Okay, let's move on from AI. This could be an endless discussion about AI, but you've got a lot more lessons to teach us. You've helped build Uber Eats, you've had a couple startups in the past. We talked about Scour for a bit. I've talked to a bunch of people that have worked with you over the years, and I got a lot of really interesting insights into the stuff that you're extremely good at. So I'm just going to go through a bunch of these. One is your obsession with being close to customers, talking to customers, and I love this topic because it's something everybody thinks they're great at, and they feel like they completely understand how this is important, why this is important. They all feel like I'm doing this, don't worry about... Everyone else is not doing this, but I am. Talk about just what you think maybe people miss about how this looks when you're doing it well, and just why this is so important.

Jason Droege (00:42:33):
I mean, I probably fall in the category of what you just described, which is maybe part of the hubris you need to start anything new. But I mean, I don't think it's a clean process. I think my process is I'm constantly questioning every single thing that I'm hearing at the beginning of anything. I don't take what a customer says literally. And there's been a lot talked about on this topic from a product management standpoint in terms of like, oh, don't do what they say, do what they mean, and look at the real problems and underlying things. I think the way that I look at it that might be additive to the discussion is I look at the underlying incentives of the customer. And the underlying incentives of customers are not always financial. Sometimes it's ego, sometimes it's career growth.

(00:43:24):
If you're selling enterprise software to someone, there's an executive sponsor as an example, that person needs to trust that you're going to do a good job for them. How do you get them to jump with you on this big project? Well, that's part of the journey of not just the product, but what do they need to hear from us? What do we need to supply them? What do we need to do to actually unlock the opportunity to implement the product? So I think there's an incentives alignment baseline. I'm a big believer that it's cliche, but show me the incentive and I'll show you the outcome. I think that's absolutely true. And even when customers will tell you things, I'll give you an example. I've been out of the game for a while so I can be open about it, Uber Eats.

(00:44:06):
So when we launched Uber Eats, I looked at the business in terms of being close to the customer. We actually couldn't get a restaurant tour. I knew nothing about this industry. So at Uber, my job was to figure out what other businesses we should get into. And so, we looked at a billion businesses and Uber Eats, food delivery was the one that we thought was most interesting, which turned out to be right so good for us.

Lenny Rachitsky (00:44:26):
Very right.

Jason Droege (00:44:28):
And we couldn't get a restaurant tour to help us understand their unit economics. And they'd say like, "Oh, it'd be this percentage or that percentage, or Why do you want to know?" And then we'd go to a different restaurant tour and they would explain it, but they were a little suspicious of why are these Uber guys talking to me about how much my ham costs? And so, what we did is we ordered just a bunch of food from these places, and then we got a restaurant supplier to give us a base catalog, and we just matched up how much does the ham weigh? How much does the cheese weigh? How much does the bread weigh? How many pieces of lettuce were on there? And we tried to actually just compose our own independent view of what's the ingredients cost versus what's the labor cost? And then, we triangulated what was our ground truth, and then what are we being told by restaurant tours, and then what is the site guys telling us about restaurant economics?

(00:45:16):
And if those things all overlapped, and we're like, okay, we have an insight about what to do here and how does this relate to Uber Eats? Well, what we found as part of this is that roughly a restaurant pays 20 to 30% of every meal to ingredients, and they pay roughly 20 or 30% to labor, and they pay roughly 10% to real estate and a bunch of other, anyway, so goes down the chain. But the important parts is what's the value of incrementality?

(00:45:41):
And so, we came in and we said, "We're going to charge you 30% of the bill." And they were like, "Oh my God, is this group on all over again? This is way too high. Oh my gosh." And we explained the economics to them and they were like, "Okay, we'll give it a try, but this is way too high." And they were right, the real number, the real clearing prices aren't 25%, but we weren't that far off. And so, when you go to find product market fit or be close to the customers, it's a combination of what's the most valuable thing. Well, in a restaurant tours case, give me incremental demand. Because if you were to take a restaurant location and triple demand based on the same labor but you're just scaling ingredients, you've got a 70, 80% incremental gross margin product.

(00:46:27):
Restaurant tours would hate when we would say this because it doesn't work out exactly like that in reality. But because we had that insight, we had confidence that we could go to market with, we need to charge you this so that the delivery fee can be that. And then, if the delivery fee is that and we charge you this, then we think the consumers will adopt, and that's what you need to get your incremental demand, and then we could pay the driver this. And so, you fit this whole puzzle together without totally satisfying, in the case of a marketplace, you're not totally satisfying any individuals 100% of their needs. What you're satisfying is is you're getting a clearing rate for them to participate in the market in the case of a marketplace. So that's one example.

Lenny Rachitsky (00:47:07):
Yeah. I love this example as you almost you figure out how to help them with something they don't even fully themselves know yet. So as you think through their goals for them as if you were them, break down the economics and then here's the solution versus, hey, what can we do for you guys?

Jason Droege (00:47:25):
Yeah. I mean, if you walked into a restaurant, they would tell you a bunch of things. They would say, "Oh, labor schedule is an issue." They would say, "My rent is an issue." They would say, "All these, my ingredients prices are an issue, that's 20 or 30%." If you could shave off 3% of that, that would be huge. You might then take that and go, "I'm going to go build a business. It's going to save you 10% of your ingredients costs."

(00:47:45):
Well, but that doesn't actually get into their head on what's truly important day-to-day. That might be important for them on an annual basis, but on a daily basis, what are they doing? They're looking at their numbers, they're looking do people show up. Did I make money yesterday? Am I going to make money tomorrow? So the urgency, I think the biggest thing people miss when they're building new products is the urgency of the buyer part of it. You can build something that provides a lot of value, but if it's not the top thing that the customer is thinking about in their busy days, then you're just going to have a long road to a small town.

Lenny Rachitsky (00:48:19):
This touches on just the theme I heard a lot about, this idea of independent thinking and how much you value that, and this feels like a really good example of that. Is there anything else along those lines of just why this way of thinking is so critical?

Jason Droege (00:48:30):
I think as a founder's job, and I mean I stretched that term because at Uber we had all of the benefits of Uber so I wasn't really a founder. I just started the business there. But there are some elements of founding there is you're looking for alpha in the market. When we started our first company in '97, it wasn't that cool. It might've been cool in Silicon Valley, but it was definitely not cool in LA. Now, it's super cool to start a business. So as a result, everyone's trying everything. So how do you get alpha on that market. If your research is highly influenced by what the world is saying around you, you're not going to have an independent insight. You have to go off and do your own thing.

(00:49:14):
And this is why from an entrepreneurship standpoint, I have very strong feelings about what the approach to founding a company should be and is probably very particular to me. But it truly is about what insight do I have, because why am I so lucky to have this insight? Why in a world of a million entrepreneurs who are thinking, who are smart, who are trying everything, why am I in the position where I likely have an insight that others do not? And then, why am I the one to do it?

(00:49:46):
And the answer might be I'm in this narrow, far-flung place. The other answer might be, I am inherently a contrarian personality type, so I'm just constantly looking for the thing that's true that people don't believe is true, which sometimes worked. But then, the second part of that's super important, which is why do I want to work on this problem for 5 to 10 years? And people get this wrong all the time. They go and talk to a customer and they go, "They have a problem. I'm going to go solve it." And it's just not a great way to start a business. You really have to have this burning desire to constantly be questioning yourself.

(00:50:20):
The other thing about independent thinking is is that you can't fall in love with your ideas. And I do not proclaim to be the world's greatest thinker for what it's worth, this is what you've been told, but is just part of that is basically throwing away who you are, who you've been, all your ideas for the mission that you're on, which is trying to accomplish something for our customer.

Lenny Rachitsky (00:50:43):
This is great. I'm glad you went here. This touches on the other theme I heard often about you is just how high of a bar you set for new businesses. And I think this advice is useful both for founders, as you said, and also people starting companies within companies, new business lines. So you've talked about this a bit already, but is there anything more there, just how high that bar needs to be for it to likely work out when you're starting something new?

Jason Droege (00:51:07):
Look, if you want to give yourself the best chance, and this isn't always how it works, but if you're in my position 25 plus years in their career, if you want to give yourself the best chance, I think there's two ways that companies end up working out. And the first way, which is probably the most important, quite frankly, is that the founder is just a force of nature over a long duration of time. Because you're going to have to pivot, you have to have that energy to pivot. You have to go years and years and years with it being hard, and that's probably the most important thing.

(00:51:36):
But the second most important thing is that you can easily educate yourself on what are good business models, what are bad business models, what are good markets, what are bad markets? And even if you're this force of nature, having the knowledge, if you're going to go into a bad market with all your energy, you should at least know, maybe ignorance is bliss because you just throw yourself into it and it just works out with time. But that's not how I would operate, which is marketplaces are good businesses. SaaS, at least historically, we'll see how this changes, but SaaS, historically, great businesses, recurring revenue businesses, sticky businesses, network effect businesses.

(00:52:12):
And if you look at what the top VCs invest in, yes, there is a lot of portfolio building, but there are similarities in terms of the types of business models that they believe could be worth tens of billions of dollars. And they have network effects, they have lock-in. They are more valuable at scale, a big scale than low scale. So if you just take a filter on a new business, this is what I did at Uber, which is like if you just have a filtering mechanism on a new business, it doesn't take that long to eliminate the bad ideas. And then, of what's left, you can pick, oh, I'm very passionate about this, even though it might have more problems than this other thing that on paper looks better. And then, you have to have passionate about it. But I think people just miss a basic understanding of what businesses even have a chance of being worth $100 billion.

Lenny Rachitsky (00:53:04):
So you launched Uber Eats, you figured out this is the place to go and bet. As an outsider, feels obvious, of course this is going to be a massive success. Of course, food delivery, such a good idea. I know you looked at a ton of ideas in that process. Can you just talk about what you explored and why you ended up picking Uber Eats?

Jason Droege (00:53:23):
I am definitely not the smartest person in the room when it comes to figuring these things out. And so, I keep a very, very wide aperture on ideas for as long as I can until I'm like, okay, everything is coalescing. And I think there's a bunch of reasons why you have to keep an open aperture on considering ideas that might seem bad at the start, but you just keep digging and see if you're right that they're bad or you're wrong. So just as a general philosophical principle, I'll start there. We looked at, we did some crazy stuff. I went walking around San Francisco one day and I looked down Market Street and there was a CVS, a 7-Eleven, a CVS, a Walgreens, a 7-Eleven, and I'm like, "How many SKUs could possibly be inside one of these things that people want and couldn't you just put that into a van and you hit the button on the van and the van comes around and you get whatever convenience items you have, and they're convenience items, so why would that be a problem?"

(00:54:14):
And we launched that in DC. We put 10 of these trucks on the road, we put 250 SKUs in them. And I mean, crickets is an understatement of how bad it was. I mean, we couldn't get an order to save our lives. And what we realized was that we hadn't really done the research on what convenience stores really were. It was if you didn't have cigarettes, you didn't have beer, you didn't have Slurpees, you didn't have these things, for example, you didn't bring people in to sell all the other things. So we didn't know anything about retail. We were clueless. So that's one idea. We looked at grocery, but honestly the unit economics just terrified me of all the pick packing and everything like that. I think Instacart did a remarkably good job at getting the unit economics to a good spot and probably the hardest operational problem you could tackle.

(00:54:56):
We did generalized delivery, point to point delivery, what's now, I forget what Uber's product is called, but Uber Direct I think it's called, where you have something that needs to go point to point in a city. That was a flop from the beginning because the truth is is how consumers don't really have this need, business sort of have this need, and in 2014 when we were doing this, no one had this need. But we tried 15 versions of all these things before we eventually just said, "Okay, the food delivery thing is just popping off on all signals and we can make the unit economics work. People seem to want it. It's a super cool problem because we can enable independent restaurants with all these tools and allow them to compete with the big guys. We can take the real estate out of the equation. So you can have a real estate location that's non-prime, but if you have prime food, then you get to compete." So we're like, "Oh, this is a very interesting problem and we can really help local economies."

Lenny Rachitsky (00:55:49):
And this ended up being, if I remember correctly, this basically saved Uber during COVID. Lyft didn't have something like this. And how big is this business at this point? Anything you share about just how important this turned out to be for Uber?

Jason Droege (00:56:02):
Yeah, of course. Well, we launched it in December of 2015 in Toronto and within two hours we had done $20,000 for the sales. It was crazy how quickly we saw that it was the right idea and the unit economics were good. And then, four and a half years later, I was at Uber for about six years, but it took us about a year and a half to figure this out. Four and a half years later, it was about $20 billion. So it was 0 to 20 billion in four and a half years, which is pretty good. Uber was very good at scaling things, but competitive market. Others did well. We beat a lot of people. Some people beat us. And then, now I think it's pushing 80 billion, and that's been for another four and a half years since I left. I think COVID turned it from 20, I left right before COVID, total coincidence, 20 to 50 in a year. So I mean, ride-sharing went this and food delivery just went to Pluto.

Lenny Rachitsky (00:56:52):
What luck. Well done.

Jason Droege (00:56:55):
Luck is part of the game. That's the other thing that's important to realize. Luck is part of the game, so do not begrudge people for luck. This industry is hard. All these things we're doing are really, really hard. Luck is just part of the game.

Lenny Rachitsky (00:57:08):
Maybe speaking that maybe not. One of your colleagues, Stephen Chau, who I am an investor in his new company, he worked with you at Uber Eats for a long time. He told me to ask you about the McDonald's story. I imagine that was just a big milestone, a big moment enough for you guys. So why'd you decide put McDonald's in Uber Eats and there's apparently a story of how you won that deal.

Jason Droege (00:57:27):
So it was interesting, and this just goes to maybe where sometimes ignorance leads you to accidentally the right answer. So we had launched Uber Eats and Uber had a global footprint and we were the only food delivery network with a global footprint excluding China. Everything at Uber needed to be launched globally. That was a very big part of the culture, et cetera, which is a lot of work and you can spread yourself too thin and cause other problems. But in this way it was good. My vision was, okay, let's help the little guy compete with all these chains. They have these systematized food systems and food is what makes a city amazing. And no one talks about the chain restaurant that they visited in Paris. They talk about the local place that they found and let's be part of that. That's who we want to be.

(00:58:17):
And so, McDonald's actually approached us and they said, "Hey, we'd love to do food delivery with you." And I said, "No." And they're like, "Hold on a second. We have 80 million consumers a day. You don't want to do this together?" I'm like, "It's not really our vibe right now." And so, I pushed them off for four or five months until my team is like, "You're insane. These people are going to put marketing behind it. They really want to do this. They want to lean in." So we actually had, because of that, I think it's hard to correlate these things, we ended up with this exclusive relationship with them, got an insane number of customers of... Chains at this point actually weren't really on food delivery networks because everybody was so worried about the unit economics, because they're so sensitive to the basket size.

(00:59:00):
And my approach was like, eh, figure it out, which is a very Uber culture thing. Okay, the basket's $17, it's our job to make that work, reduce the radius on the delivery, figure out the economics, maybe mark up some of the food someplace. There's always a way to figure it out. So we did it and then three months later the business just started hockey sticking again at a different level. And my team is just like, "Dude, you were so stubborn on this point," but I think it actually ended up being in net benefit because we got a great deal with them.

Lenny Rachitsky (00:59:34):
So the fact that you pushed him out helped you get a better deal is what I'm hearing. That's amazing.

Jason Droege (00:59:37):
Yeah, I think that's the story he would be referencing. And then, the onboarding of it was crazy because we basically went global with them in six months, and at this point the business was less than two years old. So activating this, I don't even know, an 80-year-old company that expects processes to be in place and we have two of our office managers in New York managing it. It's just mayhem.

Lenny Rachitsky (00:59:59):
I'm still sad In-N-Out is still not on any of these apps.

Jason Droege (01:00:04):
Yeah, me too.

Lenny Rachitsky (01:00:05):
I remember someone was hacking it. There's all these ways people found a way around and they're like, "No, no. Okay, you're Postmates. We know we're not going to give you any food."

Jason Droege (01:00:12):
Yes, love In-N-Out.

Lenny Rachitsky (01:00:13):
You've touched on this idea of gross margins and margins, how obsessed you are with this. I wanted to spend a little time on here. I've heard just you're obsessed with understanding gross margins before going in on anything. Most founders have no idea what they're doing here. What have you learned about just what people should be paying attention to, what they might be forgetting when they think about just the feasibility of a business?

Jason Droege (01:00:33):
Yeah, look, it's one filter like many filters. There are certainly businesses that have low gross margins that are great businesses. Costco, Walmart, et cetera. Amazon talks about this all the time of there's companies that increase prices and there's companies at lower prices. But I would say that by and large, high gross margins combined with healthy churn curves are a very healthy sign for the business. I mean, think about it. If I were to sell you something and I can't mark it up a lot, how much value am I adding beyond what's in my hand? And if I'm not adding that much value, then what am I in the business of doing? And I'm in business of adding value. And it's not quite that simple. This is just a litmus test of when someone comes to me and they go, especially in a new business, and we deal with this. I dealt with this at Uber, I've dealt with it everywhere.

(01:01:26):
Someone comes up with an idea and they go, "We can get into this business and I think we can charge this and it'll get us to a 40% gross margin." And then, my next question is start at a 60% gross margin. Why does that not work? And they go, "Oh, well, the customer..." And immediately, you short circuit to what the real problem is. Oh, the customer has an alternative. Oh, okay, well who's the alternative? Oh, it's some offshoring company. Well, what's their gross margin? Oh, we don't know. You go find out. It's like 20% and they've been around for a long time and they have scaled operations. And you're like, okay, so your gross margin is going to go from 40 to 20 quicker than you think, and you're going to be in a world of hurt unless you do something to differentiate.

(01:02:06):
So I take gross margin is just a very coarse instrument, not a perfect instrument to think about, am I adding enough value? Am I differentiated? It's not perfect, but it's a very quick short circuit filter to even to see if someone's pitching you an idea, have they thought through this dynamic? Because if the response is gross margin is super low right now, but here's the dynamic I'm going after. And then you're like, "Oh, okay." And sometimes it's like, we'll just make it up with volume and then the gross margin will go negative for a while and you're like, "Wait, this doesn't work."

Lenny Rachitsky (01:02:35):
So what I love about this is just a lens into is my idea good enough if studying, can I keep a high gross margin? Is there a reason why people in this space haven't been able to have a higher margin?

Jason Droege (01:02:48):
Yeah, exactly. And like I said, it's meant to disqualify just you're doing these large for larger companies and everybody has ideas. And so, it's a way to cut through. Do you understand the machine that is going to need to be in place in two or three years? You might have a 70% gross margin now because the next question is why can't someone else do this? And if you have an answer of like, "Well, they can now, but they can't in two years, if we run really fast." Okay, we might have something. If they can now and they will be able to in two years, you're going to have margin compression.

Lenny Rachitsky (01:03:29):
Along these lines I was just listening to, I think it was the a16z podcast. Alex Rampell I think was sharing this story about Costco, how as you said, their strategy is actually to keep margins very, very low because all their revenue comes from their membership. So they have something like 50 million members paying 100 bucks a month and that's their entire business. And so, they don't plan and they don't want to make money off the products.

Jason Droege (01:03:55):
Yeah, that's right. I mean, they're playing a slightly different game, not an expert on Costco, have spent some time with the company, but they use price as a way to get to scale. And so, they're basically saying if we discount, same with Walmart, we will get so much volume that we will just take the air out of the room for all of our competition. And so, then the question of, okay, so if you have a low gross margin today, in two or three years, once you land one of these centers in a market, why won't your margins to get eroded? The answer is because we will have already absorbed all of the demand. You try to go to 8% versus 10% gross margin, which I roughly think is what their gross margin is. That's going to be a really hard business. If you already have a habit with a customer, they have already built their weekly trips around you, you already have relationships with suppliers, you already have general managers that know how to stock inventory, that's not a straightforward exercise. So they're first to scale and then good luck competing with them.

Lenny Rachitsky (01:04:49):
Okay. Just a couple more questions. One is there's this term that I've heard that you often say and believe in is this idea of not losing is a precursor to winning.

Jason Droege (01:05:00):
Yes, yes.

Lenny Rachitsky (01:05:01):
Talk about that.

Jason Droege (01:05:03):
Tech is a culture where portfolios are built by investors, and a lot of the narrative is controlled by investors frankly. Founders obviously participate, but this idea that you should just go for it is consensus. Just go for it. Who cares? Well, I don't know, if it's my life and I only have one moment to take a shot, I might want to just not just go for it. I might want to think for a little bit, and I think the best entrepreneurs, I have no data to back this up, but just these are my friend, this is my friend group. I think the best entrepreneurs and the best business owners look at the risk profile of the decisions that they're making and they try to make asymmetrically positive decisions all along the way.

(01:05:51):
And so, oftentimes I feel like we forget about the risk of a decision, and there's more to unpack there because I actually think taking highly risky decisions and then having it work out is a weird cultural thing too, because then how do you train people to do that? Because it's a very hard thing to take high risk decisions and be right enough because it creates a lot of volatility. But it goes back to my comment about the most important thing in founders, which is just this ability to persevere through. Survival is just part of the game, and most people just give up before they get their timing right, before they get the right insight with the customer before they get the right product in the market. And life can change quickly in tech. You can go from being a dog to being a hero in a very short period of time, but you're on this very, very long journey, but you have to survive for that condition to be met.

(01:06:38):
And so, then the question is is when you're in a hype cycle, I would argue that we are right now, everyone wants to go for it and then go for it more and then go for it more and go for it more and you don't realize, guys, all of our customers are going to be around in five years. They just want us to solve their problems. We have to be around to solve their problem for them. And so, survival is a precursor to that. So let's not put ourselves in position that could potentially compromise the enterprise along the way. It doesn't mean don't take risks, but think about how you calculate it.

Lenny Rachitsky (01:07:10):
I love how clear it is that this lesson and many of the lessons along these lines have come from just failure and things not working out and things breaking, which is the best outcome.

Jason Droege (01:07:19):
If you ever get on the other side of a high reward, high risk decision, it is so painful because you are just cooked. You are done, and often there's no way out.

Lenny Rachitsky (01:07:32):
Is there a story along those lines that comes to mind or an example of that?

Jason Droege (01:07:35):
Well, this is where it is together on why I try to be so I think you can spend a little bit of time thinking upfront to save yourself a lot of pain downstream. I had this business not worth detailing it, but after the bubble burst in 2001, I'm like, "I'm going to self-fund a business. I'm going to build a profitable business. I want to prove that I can do this." And we had started Scour, which had all the things we talked about. And so, what I did is I'm like, I was a golfer and frankly, there was nothing to do in tech.

(01:08:03):
So I started selling golf clubs on the internet and I was making real money and I might've learned more from this business than any other because I started on eBay and I was 22, and I didn't really understand that my margins would come down because anyone can do this, but I was one of the first ones to do it, so I was making a ton of money and then I built this business and then I just failed to recognize I had a lot of hubris. I was like, "Oh, if I could just buy all the used golf clubs in America, I can be the market maker for prices," and don't people do that?

Lenny Rachitsky (01:08:34):
I love this ambition. That's great.

Jason Droege (01:08:36):
And it's just like it's madness to actually think about the practicality of that. And so, I just didn't spend the time thinking and then I ended up in this business. The business was profitable, it got to a couple million of revenue, whatever, paid me a dividend for a while, but it was painful the entire way.

Lenny Rachitsky (01:08:51):
I love the spectrum of experiences you've had. You've sold golf clubs, you're helping achieve AGI, you could say. There's also a whole part of your career. We haven't talked about where you built tasers and body cams and drones and all these things. Also, peer-to-peer file sharing before anyone else. Final topic I just want to spend a little time on based on this experience is hiring and building teams, something that I know you have a really strong take on. That I've been hearing a lot on this podcast recently is this idea of it's more important to build the right team than find the most optimal top talent. Talk about that, why that's so interesting and important.

Jason Droege (01:09:31):
As of late, I've developed a more nuanced view of this, which is for certain roles, you absolutely need the right experience in this current market. You see this with researchers, because the market's moving so fast, you don't have time to train up some people, so you actually have to go find people either who have the right relationships with customers that you want to get or you have to, who might not check other boxes but are awesome at that, might not check the classic boxes that I think you're referencing of they're a problem solver, they can grow with the company, they have a high trajectory, et cetera. I would say that's 5% of the roles in the company, but very important whenever speed to market is important.

(01:10:09):
And then, for interviewing, I just interview for three things and I have to interview across all kinds of expertises, which is hard. I can't be an expert in everything. And so, I reduce it down to just three things, which is like, are you a curious problem solver and can you articulate that verbally? Can you work across people? Are you humble enough to work across and are you a good leader? And if you just do those three things, I think you have a pretty high chance of success, at least in an organization that I'm running, because the world's changing. So you do need people that are adaptable. So all the experience is not necessarily one-to-one relevant.

(01:10:53):
And then, the working across to your team point, this actually came up at Uber Eats. So when I was building the Uber Eats management team, I'm not sure if this was mentioned to you from that group, but whenever I would hire people, I was trying to compose almost like an organism of strengths and then minimize the conflicts. That management team for the most part outside of some of the operations side, but for the most part, that management team was the same management team from day one when we had nothing to $20 billion. And I just believed that the team, knowing each other's strengths and weaknesses and being able to compensate for each other was more important than the classic advice you get around, "Well, that person hasn't seen this much scale." And you're like, "Well, yeah, but can they learn it?" I learned it. So you do have to kind of believe in people a little bit, which is my job, not necessarily their job. And so, I mean, these are people systems. They're not straightforward rules-based things you can apply.

Lenny Rachitsky (01:11:49):
And I especially love this advice because there's all this talk about what skills will matter in this world of AI doing all our jobs, and it feels like these three buckets are maybe the same thing, just are they good at solving problems? Are they good leaders? Can they collaborate well with other people?

Jason Droege (01:12:02):
Yeah, I don't think that the core rise of humanity, it will change, and I think that these things are pretty core to how humans have been successful for a long time.

Lenny Rachitsky (01:12:11):
Speaking of that, I'm going to take us to a recurring segment of this podcast that I call AI Corner, where I ask folks this question, what's some way that you've found a use for AI in your day-to-day life in your work that makes you more effective, get more done, get better stuff done?

Jason Droege (01:12:28):
Honestly, when I came into Scale, so my history was in consumer and I've done some application level stuff with government, and this space is moving so quickly. AI is my, I use it as a tutor. As these new concepts come up, I have a lot of people in the company who can educate me on the nuances of the technicals of all of, excuse me, the technical nature of the data and the products, but they only have so much time. And honestly, there's new concepts coming up all the time and I need to stay on top of it.

(01:13:01):
So it might sound crazy, but a large percentage of my job is not dealing with the engineering issues related to AI. I'm managing an organization, but I love understanding it. It's one of the most enjoyable, rewarding parts of my job is to learn from all these AI researchers, but they don't always have the time to do it, so I use it as a tutor. I turn on voice mode and talk to it on my way into work. So I think that's probably the most impactful thing that I use it for that's also relevant to this topic.

Lenny Rachitsky (01:13:32):
I do exactly the same thing, especially when I'm prepping for this podcast. What exactly is this? I think about when you say this, I did an interview with the founders of Perplexity a few years ago asking about how they work at Perplexity, and the founders said that before, they were ruled, before they ask a question of anyone on the team, they have to ask AI first. And I was just like, "That's crazy." Now, it's so obvious. But back then, I was like, "That's an insane way of working. I've never heard of this before." Just a sign of how ahead of the curve they were.

Jason Droege (01:14:04):
Yeah, I think number two would be I'll take internal documents and I'll ask, what's the most important thing in this document? And I'm shocked, and then I'll read it and just double check, but I'm shocked at how good it is at just pulling out. There's so much in organizations that is like, I don't know what you want me to say and I don't know what I need to know, but we each have our own agendas, and so this matching of, and so then there's this huge broadcast problem where it's like, of all of the information you might want to receive, what's actually important to you? And so, I use it a lot for that too.

Lenny Rachitsky (01:14:39):
Amazing. That's a really good tip. I use it for legal documents, just like what do they know about what they're trying to do here for me or against me? Jason, is there anything else you wanted to share or leave listeners with, maybe double down on a point before we get to a very exciting lightning round?

Jason Droege (01:14:54):
Yeah, absolutely. I mean, I think the really important, the reason why I'm doing this, the reason why want to spend time here outside of wanting to be on the show for a while and being a long-term listener is, our long-time listener, excuse me, is there's a lot of amazing work going on at Scale. The teams are working super hard, we're delivering a ton of value for our customers. The public narrative has not represented the work that the people here are doing and the work that our customers are doing with what we're doing for them. And I just think that deserves the respect and reward that all those people are putting in, and we'd like people to know that.

Lenny Rachitsky (01:15:34):
I appreciate you saying all that. With that, we've reached our very exciting lightning round. We've got five questions for you. You ready?

Jason Droege (01:15:38):
Yeah, let's go for it.

Lenny Rachitsky (01:15:39):
What are two or three books that you find yourself recommending most to other people?

Jason Droege (01:15:44):
Some of this is going to sound interesting. The Selfish Gene is one of my favorite books.

Lenny Rachitsky (01:15:48):
Love that book. I don't know if anyone's ever mentioned, it was one of the most influential books for me too. So sorry, keep going.

Jason Droege (01:15:54):
Yes. I think Selfish Gene. Road Less Traveled, I've read more than once. I mean, it's just one of the classic human psychology book. And then, I think in business, I think Good to Great. It's not the read that you're going to be most excited to enjoy on a vacation, but it's pretty much right, and I think we should take advice from people who have analyzed these business problems before because not a lot's changed, but we keep acting like everything's changed.

Lenny Rachitsky (01:16:24):
What's crazy about that book, you look at all the companies they talk about, I haven't read in a while, but just the whole book is about companies that last, I believe, or maybe that's the other book, I don't know. But anyway, all the companies that they talk about, I don't know if they're still around. It's so hard for a business to last a long, long time.

Jason Droege (01:16:38):
I would also recommend Thinking Slow and Fast, that's the... Yes.

Lenny Rachitsky (01:16:38):
Thinking, Fast and Slow.

Jason Droege (01:16:43):
Thinking, Fast and Slow. Excuse me, sorry. It's been like a decade since I read it, but just in terms of point there being human biases are very important to understand.

Lenny Rachitsky (01:16:51):
What's really crazy to me about that book and Kahneman in general, someone asked them just, how's your life been impacted by learning all these biases humans have? He's like, "Not much. I have the same biases. Knowing them doesn't really help me avoid them."

Jason Droege (01:17:05):
See, I find myself checking myself. Whenever I get super convicted on something now I will be like, okay, what is the list of things that I'm inclined to do to try to catch myself? Because I think we're most inclined to have these bad decisions impulsively, which is what I think the book is largely about. I mean, it's a long book.

Lenny Rachitsky (01:17:28):
So long. Oh, my God. It feels like that's where AI can help us in the future. Just like, "Hey, Jason, are you sure this isn't framing a fact or whatever?"

Jason Droege (01:17:38):
Yes.

Lenny Rachitsky (01:17:38):
Okay. Next question. Do you have a favorite recent movie or TV show that you've really enjoyed?

Jason Droege (01:17:43):
Most of the movies I watch are with my kids, so I wish I had something deep and profound.

Lenny Rachitsky (01:17:50):
No, kids content also is a very acceptable-

Jason Droege (01:17:52):
The Formula 1 movie I thought was really good. I mean, it's a classic action movie. I don't think it informs anything in AI or business, but it's good to check out from the craziness of tech once in a while.

Lenny Rachitsky (01:18:04):
Is there a product you recently discovered that you really love? Could be an app, could be clothing, could be a kitchen gadget, anything along those lines?

Jason Droege (01:18:13):
VO3. Not totally new, but when I was in high school, I wanted to be a screenwriter. I actually grew up in the Bay Area and everybody was an engineer, but I wanted be a screenwriter. And so, I went back and I got the first page of one of my old scripts, which not good scripts, but I got the first page. I took a picture of the script and I fed it to VO3, and I said, "Make this scene," and it got it right.

Lenny Rachitsky (01:18:38):
Wow.

Jason Droege (01:18:39):
I was shocked. I was just absolutely shocked that you could just take a picture of a script. And so, now I'm thinking about that for how do I use these tools for family videos? Some of the grad tools now with making live images more active, I think are really interesting. I think they need one more step of iteration, but I think those are going to be really emotionally life-changing for people because just a little bit of movement in an image from a grandparent or a relative or whatever you haven't seen in a while, it really does make a big emotional impact on you.

Lenny Rachitsky (01:19:20):
I love that when you play with these tools, you probably can think about, oh, here's the people that help train this thing. Here's the people that helped on the problem that it had.

Jason Droege (01:19:26):
I was actually talking to someone who was working on VO3, and I told him the script thing and he goes, "Oh, actually scripts. Yeah, no, the way the data is formatted in a script, that would actually be very good." Because they start with set looks dark interior, this character says it in this raspy voice, and so it gives you all the instructions in the script.

Lenny Rachitsky (01:19:45):
Oh, man, just unlocked a whole new business unit right there. Two more questions. One is do you have a favorite life motto that you often think about, find useful in work or in life?

Jason Droege (01:19:57):
Yeah. The end is never the end. That's my favorite internal saying, and it goes to the comments before about survival being a precursor, surviving being a precursor to thriving. You got to survive before you thrive, which is your brain tells you, and along these entrepreneurial journeys, I think this is most applicable. I mean, this is the hardest journey anyone can go on. If you go on this journey for five years, you are mentally harder than 99.9% of the population. People don't understand the Chinese water torture of having self-doubt and having things go wrong, et cetera.

(01:20:31):
And so, more tactically, you get this when you're working out like in a day like, "Oh, I'm too tired. I need to stop." But the truth is is you can keep going and the world's going to keep spinning. So I find in the moments where it's just the hardest or you have this hard decision that seems impassable and your body, you're having this visceral reaction to this is impassable, just to remind yourself that I'm going to wake up tomorrow. This isn't the end. There's another end somewhere. I just find that to unlock me to be like, okay, there might not be a perfect solution, there might be an imperfect solution, but it's a solution so let's just keep going.

Lenny Rachitsky (01:21:06):
Final question. You helped create Uber Eats. I imagine you're still a power user of Uber Eats. You have a favorite restaurant on Uber Eats that maybe people should know about, maybe that you order most from?

Jason Droege (01:21:16):
I order a shocking amount of McDonald's actually. Despite my original story, it's the family treat in the house. I would say that that's probably the top thing that we order.

Lenny Rachitsky (01:21:31):
Oh, man, I'm worried for your health, but I love, I haven't had McDonald's so long. This is like, maybe I should give it another-

Jason Droege (01:21:37):
I mean, more practically we will order mixed greens or tender greens or something like that on a day-to-day basis, but I think that the more notable, surprising thing is is that despite my initial aversion to working with a global chain, it's a good treat once in a while. You just shouldn't have it all the time.

Lenny Rachitsky (01:21:57):
Jason, this was incredible. I really appreciate you making time for this. I'm really honored to be the first chat you've had since taking over at Scale. Where can folks find you online if they want to maybe reach out, learn more about what you're, I don't know, maybe join Scale. Where do you want to point people to and how can listeners be useful to you?

Jason Droege (01:22:14):
Yeah, absolutely. I'm @jdroege, J-D-R-O-E-G-E on X. That's probably the easiest way to follow me, keep up with things and you can shoot me a DM if you like. And so, I think that's how you would keep in touch and, sorry, what was your other question? Sorry.

Lenny Rachitsky (01:22:31):
If you're hiring, I don't know, where should people go check it out if you are, and then also just-

Jason Droege (01:22:34):
Absolutely. Just go to scale.com, go to our careers page, and we have 250 open roles. To the point about we're in business and we're growing, we're hiring a ton of people. Our data business is growing, our applications and services business is growing like crazy, and so we're going to need a lot of people to help us on that journey.

Lenny Rachitsky (01:22:54):
You guys just signed some insanely large contracts with the government I was reading.

Jason Droege (01:22:58):
Two $100 million contracts.

Lenny Rachitsky (01:23:01):
$100 million contracts.

Jason Droege (01:23:02):
100, yeah. We didn't sign just one. We signed two in one month, so yes, no, our federal business is doing well. Our enterprise business is doing well. Our international government's business is doing well. There's a lot of demand out there.

Lenny Rachitsky (01:23:16):
Some salespeople are getting some great commissions. Good job. Jason, thank you so much for being here.

Jason Droege (01:23:21):
Yeah, thank you. Honor to be a guest here. Super excited to be with you, especially so early in the journey, or at least my journey here leading Scale.

Lenny Rachitsky (01:23:32):
Appreciate it. Thanks for coming. Thanks for joining us. Bye, everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

