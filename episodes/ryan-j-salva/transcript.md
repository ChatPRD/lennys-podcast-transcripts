---
guest: Ryan J. Salva
title: The role of AI in new product development | Ryan J. Salva (VP of Product at
  GitHub)
youtube_url: https://www.youtube.com/watch?v=awcd3P1DnX4
video_id: awcd3P1DnX4
description: 'Ryan J. Salva is the VP of Product at GitHub, where he led the incubation
  and launch of Copilot, which uses OpenAI to suggest code and entire functions in
  real time, right from your editor,...

  '
duration_seconds: 3900.0
duration: '1:05:00'
view_count: 3798
channel: Lenny's Podcast
keywords:
- growth
- acquisition
- metrics
- roadmap
- iteration
- experimentation
- analytics
- conversion
- revenue
- hiring
- leadership
- management
- vision
- market
- persona
---

# The role of AI in new product development | Ryan J. Salva (VP of Product at GitHub)

## Transcript

Ryan J. Salva (00:00:00):
We had actually created a snapshot of GitHub's public code for what we call the Arctic Code Vault, right? Essentially, this is up in like way in the Northlands of Finland, there's a seed vault. We were like, you know what? Seed vaults are really there to preserve the diversity of the world's flora in seeds in case of some crazy either natural or manmade disaster. But another really important asset to the world is our code, our open source. This represents actually a lot of the collective, well, certainly software, if not intelligence of kind of the modern world, right?

Ryan J. Salva (00:00:44):
We had put this snapshot of public repositories on this silver film that would be preserved for thousands of years in this Arctic Code Vault. Well, we took that same data snapshot and we brought it to our friends over at OpenAI to see like, okay, what can we do with these large language models built on public code? Well, it turns out we can do some pretty cool things.

Lenny (00:01:13):
Ryan Salva is VP of product at GitHub, where, amongst other projects, he incubated and launched GitHub Copilot, which in my opinion is one of the most magical products that you'll come across. If you haven't heard of it, it uses OpenAI's machine learning engine to autocomplete code for engineers in real time as they're coding. I think it's one of the biggest advances in product development and productivity that we've seen in a while. I'm always really curious how a big product like this starts, gets buy in, build momentum, and then launches, especially at a big company like Microsoft and especially a product like Copilot that has surprising ethics challenges, scaling challenges, business model questions.

Lenny (00:01:55):
Also, this came out of a small R&D team that GitHub has, and it's so interesting to hear what Ryan has learned about incubating big bets within a large company, and then taking them from prototype to Microsoft scale. Ryan is also just super interesting as a human. He's got a very non-traditional background. I am excited for you to hear this conversation. With that, I bring you Ryan Salva. If you're setting up your analytics stack, but you're not using Amplitude, what are you doing? Amplitude is the number one most popular analytics solution in the world used by both big companies like Shopify, Instacart, and Atlassian, and also most tech startups.

Lenny (00:02:38):
Amplitude has everything you need, including a powerful and fully self-service analytics product, an experimentation platform, and even an integrated customer data platform to help you understand your users like never before. Give your teams self-service product data to understand your users, drive conversions, and increase engagement, growth, and revenue. Ditch your vanity metrics, trust your data, work smarter, and grow your business. Try Amplitude for free. Just visit Amplitude.com to get started. This episode is brought to you by Athletic Greens. I've been hearing about AG1 on basically every podcast that I listen to, like Tim Ferriss and Lex Fridman.

Lenny (00:03:20):
I finally gave it a shot earlier this year, and it has quickly become a core part of my morning routine, especially on days that I need to go deep on writing or record a podcast like this. Here's three things that I love about AG1. One, with a small scoop that dissolves in water, you are absorbing 75 vitamins, minerals, probiotics, and adaptogens. I kind of like to think of it as little safety net for my nutrition in case I've missed something in my diet. Two, they treat AG1 like a software product. Apparently they're on their 52nd iteration and they're constantly evolving it based on the latest science, research studies, and internal testing that they do.

Lenny (00:03:59):
And three, it's just one easy thing that I can do every single day to take care of myself. Right now, it's time to reclaim your health and arm your immune system with convenient daily nutrition. It's just one scoop and a cup of water every day. And that's it. There's no need for a million different pills and supplements to look out for your health. Make it easy. Athletic Greens is going to give you a free one year supply of immune supporting vitamin D and five free travel packs for your first purchase. All you have to do is visit AthleticGreens.com/lenny. Again, that's AthleticGreens.com/lenny to take ownership over your health and pick up the ultimate daily nutritional insurance. Ryan, welcome to the podcast.

Ryan J. Salva (00:04:42):
Thank you, my friend. I am genuinely very excited to be here. Lovely to geek out with you for a little while.

Lenny (00:04:48):
I'm excited as well. We were chatting briefly before we started recording and you mentioned a little bit about your background, which is really unique for someone that is leading product at GitHub. Could you just share what you studied in school, and then briefly just how that led to your career in product management?

Ryan J. Salva (00:05:07):
Oh wow! You're going to make me remember all the way back to school. Okay. Back in school, I was not a classic software engineering, CS major. The kind of esoteric answer is philosophy of aesthetics and 20th century critical theory. The easier access answer is philosophy and English. But primarily it was really about how do we, as people, communicate with each other, how do we express ourselves through creativity. As humans since the dawn of time have been painting on cave walls and dancing around the fire and writing stories and novels and singing to each other. I was just really interested in how we convey our experience of the world to others.

Ryan J. Salva (00:05:58):
I got started in software development and product management because I wanted to be in the business of creativity. We're at a really, really unique time in human history where we actually get to witness the advent of a brand new medium. Software development and the worlds that it creates wasn't possible, I don't know, maybe 50, 60 years ago now. If I'd been born in the 1700s, I probably would've been the guy making, I don't know, new colors of paint and paint brushes, but I wasn't. I was born kind of at the turn of the 21st century, and so I work in engineering.

Ryan J. Salva (00:06:39):
That's what I've been doing for the last about a little bit more than 20 years now, working sometimes in startups, some of them other people, some of them my own, about 10 years at Microsoft and now three years at GitHub.

Lenny (00:06:51):
Amazing. I didn't know that was a job to make new paint colors for paint brushes. Is there a color you would come up with?

Ryan J. Salva (00:06:59):
Oh man! It so happens that yellow... I think I would do a really vibrant gold sunshine yellow if I was in that business.

Lenny (00:07:13):
Very positive, happy. I love it. That could be a new GitHub brand color. Today, you're VP of product at GitHub. Before that, you were a super senior product leader at Microsoft, and I'm always curious how that transition happens when you move from just a longtime senior product leader at a larger company to taking on something like this that was an acquisition. I'm curious what made you decide to take this leap, and then just was there anything interesting about the machination that went into just making that transition and figuring that out?

Ryan J. Salva (00:07:45):
Yeah, it's a good question. Like I said, I was working on development tools and developer services when I was there at Microsoft. Specifically, I was leading product for what they call One Engineering System. It's essentially the shared developer infrastructure for all Microsoft products like Windows and Office and Azure and things like that, as well as Microsoft's DevOps solution called Azure DevOps. When the acquisition happened, it was clear that so much of the energy, so much of the focus and the innovation that was going to be happening around developer tools and services was going to be happening around GitHub. I mean, that's where the community is creating.

Ryan J. Salva (00:08:34):
That's where people are learning, that's where so much of the mind share of just the development community is focused. Like I said, I'm motivated. What I care about is helping people create. It was very clear to me that there was no place that I could have a larger impact than working at GitHub. I really took that opportunity to make the transition out of a little bit more enterprise focused internal role at Microsoft to going where I could work on everything from, I don't know, AI technology like Copilot to a cloud hosted development environments like Codespaces, repos, which literally every single developer on the planet is participating in some way GitHub repos in a typical year.

Ryan J. Salva (00:09:28):
That was what I wanted to accomplish, is just like, how do I get more connected to the community, especially the community outside of what Microsoft could reach on its own. The decision to move as well, I think, was really focused not just on what GitHub was and maybe is at the time, but what GitHub also can be. I mean, GitHub has more than a decade, nearly a decade and a half of history of bringing developers together to collaborate on code through repositories. But in the last few years, we've really expanded that portfolio to include so many different parts of the developer life cycle.

Ryan J. Salva (00:10:13):
Again, I talked there about Codespaces and Copilot, but it's also actions for CI/CD and advanced security. As developers, we are so much more than just where we put our code. There's a whole part of the tool chain there. And to get to an opportunity to work on so many V1 products, like that is creation itself, to be able to build an entirely new product, get it out to market, test it, iterate on it, and really feed on the energy that's coming back from the community.

Lenny (00:10:46):
Awesome. There's definitely a lot of energy coming out of GitHub. What I want to spend most of our time chatting about is a product that your team helped launch and incubate, which is GitHub Copilot, which just from my outsider perspective feels like one of the biggest advances in software development in, I don't know, a decade, maybe more. It's definitely one of the most magical products out there and your team and you kind of led the incubation and launch of the Copilot.

Lenny (00:11:15):
I'd love to spend most of our time chatting through that. The first question... Okay, cool. My first question just for folks that don't know a lot about Copilot is just like, what is it? Can you just kind of briefly describe what Copilot is?

Ryan J. Salva (00:11:26):
Yeah, sure. Developers for the last 20 years or more have had essentially simple, intelligent autocomplete. You hit the period and you get the next variable that might come up. It's helpful for moving a little bit faster through your code, helpful sometimes for remembering what the particular syntax might look like for a method or a function. Copilot is essentially that magnified by many lines of code. It is multi-line autocomplete that is fundamentally powered by an AI model called CodeX, which is a derivative of another one that you might be familiar with, GPT-3.

Ryan J. Salva (00:12:15):
When you are in the editor, it could be VS Code, it could be IntelliJ, it could be them, essentially, as you are typing, Copilot will provide suggestions usually in kind of this italicized gray text that is really, to your point, kind of magical what it's able to infer. Based upon the variables around it, the class names, the method names around it, your comments, Copilot infers what you intend to create, and then hopefully does a pretty good job at nailing it by providing scaffolding code template that you can then riff on. Now, what we tend to find is that developers love it. They really enjoy it. They kind of find themselves getting a little addicted to it because it helps them stay in the flow.

Ryan J. Salva (00:13:08):
As developers, we love to be in that place. I love to be in that place where I'm creating things, where I'm focusing on some product, some piece of software that I'm going to give to my customers, my users. The labor of remembering what's the order of parameters that need to come into a particular API, or hey, what's the particular syntax of this thing I'm supposed to do, or oh, I've got to create a bunch of dummy data that is days of the week or months in the year. That's just labor. It's not creating. It's just typing.

Ryan J. Salva (00:13:47):
Copilot helps developers stay in the flow by bringing all of that information into the editor, preventing them from having to go check out documentation or watch tutorial or go to Stack Overflow and either find an answer or worse, have to ask a question and wait for an answer. It just brings all of that into the editor and gives the developer often multiple suggestions that they can choose from and just pick and choose what is the right solution to solve the problem for the thing they're trying to create.

Lenny (00:14:21):
Awesome. What I'm most curious about, and we're going to spend time on this, is just how a product like this comes to be at a larger company. But before we get into that, what's the craziest story of someone using Copilot to write code? And I'll share one real quick. I was watching some YouTube videos to prepare for this chat and one guy, maybe this is the Turing Test of AI writing code, is he used Copilot to center divs. He's like, "Wow! This did it right." And then another guy, he's an instructor of code.

Lenny (00:14:51):
He makes YouTube videos teaching people how to code and he's like, "Copilot just gives you the answer immediately, and so I can't make these videos as easily. I have to turn it off so that doesn't just give it away." I'm curious, what have you seen?

Ryan J. Salva (00:15:03):
There are so many of those. I'll just kind of give a couple of recent ones that I've heard. I was talking to one developer who was... He's actually an educator and he's teaching kids how to code, usually like kind of high school age, so 16, 15, that kind of thing. His experience matches my own, which is that many of us, we learn to code best not by arbitrary exercises, but by actually building something that's going to be useful solving problems.

Ryan J. Salva (00:15:41):
What he does is he matches small businesses and medium size businesses who need to build internal tools with essentially classes of students, like a group of maybe six or eight students, and then gives those students Copilot and says, "Here, small business, medium size business. Group of students, go build this internal tool for this business."

Ryan J. Salva (00:16:08):
Copilot is essentially kind of whispering in the student's ear, metaphorically speaking, "Hey, here's how you solve this problem. Here's how you do this," and students build not only the tool, the software that the business needs and then get to put that on their resume and their application for college and university, but they also get to learn by using the tools that likely are going to be part of the core DNA of the developer tool chain two, three, four years from now, as AI starts to permeate our entire stack. That was a pretty cool recent one that I talked to.

Lenny (00:16:48):
That is very cool. I didn't think about just the education lever here of just making it so much easier to learn to code, not even just building code.

Ryan J. Salva (00:16:56):
And that's the thing, Copilot is particularly good not just at taking away some of the effort, but often... There's learning a new language, and then there's also just waiting into a code base that you're not necessarily familiar with, right? I mean, heck, sometimes I don't recognize some of the code that I wrote six months ago or a year ago. It feels like I'm wading into new territory. But maybe you need to fix a bug in an app that you don't often touch, wading into that code base is kind of learning and creating a mental map for that code base.

Ryan J. Salva (00:17:30):
One of the really magical pieces of Copilot here is that, that AI is collecting context of the application that you're going into. It can help you build that mental map and learn the code base, even if it's a language that you're already familiar with.

Lenny (00:17:47):
Awesome. Going back to the beginning of Copilot and how it started, I'm always curious how a project that ends up being a huge deal to a larger company begins and especially how it builds momentum, how it gets buy in, and then just gets out the door. Can you talk about just the original seed of this idea like, who did it come from, who had the original vision, how did this idea emerge and build momentum where you put resources into it?

Ryan J. Salva (00:18:13):
Oh wow, what a long, and I don't know, depending upon your point of view, sorted or exciting story that is. Microsoft and OpenAI have been collaborating for quite a while now on large language models, making its way into all different experiments and different parts of both Microsoft's software portfolio, as well as just helping OpenAI by providing the compute necessary. It takes massive amounts of compute to train these models. They were mostly large language models. Couple years ago now, it kind of dawned on us that, well, language models aren't just English and Spanish and German and Korean and Japanese, but Python and JavaScript and Java and C# and Closure.

Ryan J. Salva (00:19:07):
All of these are languages too. In fact, they're kind of nice from an AI perspective because they're relatively constrained in terms of their semantics, right? The number of words, I put that the in scare quotes as it were, that can be expressed in Python, for example, is much smaller than the English language, which has all sorts of different grammar rules and nouns, verbs, adjectives, adverbs. We started to see what it would be like to actually bring code to these large language models. The way that I actually got introduced to it is kind of funny. Microsoft and OpenAI had this idea.

Ryan J. Salva (00:19:53):
At the time, one of the teams that I was responsible for was GitHub's infrastructure team, the team responsible for our data centers, our reliability, our rep time. We noticed one day that we were getting hammered, I mean absolutely hammered with a tremendous amount of clone requests. We're like, "Oh my gosh! Is this like a denial of service attack? How are we going to respond to this? What's going to happen?" We figured out pretty quickly that it was actually OpenAI. They were cloning all of our repositories to harvest the data out of GItHub.I mean, it's totally legit practice, but it does have a real consequence.

Ryan J. Salva (00:20:33):
We were able to step in and mitigate it very quickly. There was not a reliability kind of an uptime incident there, but we're like, "Hey, you all, cool. Love this thing. Let's see if we can get that data to you in a more responsible way, in a way that's packaged a little bit more to meet your needs." What we did is just the year before that, We had actually created a snapshot of GitHub's public code for what we call the Arctic Code Vault, right? Essentially, this is up in like way in the Northlands of Finland, there's a seed vault. We were like, you know what? Seed vaults are really there to preserve the diversity of the world's flora in seeds in case of some crazy either natural or manmade disaster.

Ryan J. Salva (00:21:25):
But another really important asset to the world is our code, our open source. This represents actually a lot of the collective, well, certainly software, if not intelligence of kind of the modern world, right? This represents actually a lot of the collective, well, certainly software, if not intelligence of kind of the modern world. We had put this snapshot of public repositories on this silver film that would be preserved for thousands of years in this Arctic Code Vault. Well, we took that same data snapshot and we brought it to our friends over at OpenAI to see like, okay, what can we do with these large language models built on public code?

Ryan J. Salva (00:22:03):
Well, it turns out we can do some pretty cool things. Just like a translation tool that goes from English to Spanish, Spanish to German, you can also go from English to Python or Python to C#. We're like, okay, this is cool. We can start to get not only translation, but a little bit of predicted text here as well. We're all I think fairly already familiar with predictive text already in our code editors as IntelliSense. But in, I don't know, you go to your favorite word processor and chances are that you've got some kind of predictive text happening there as well.

Ryan J. Salva (00:22:43):
We started experimenting with different user experiences, right? Do we want it so that you, I don't know, right click and get a little side panel that comes up with a bunch of different options for things that you might want here. That was nice because it would give you hold functions, but it's out of the cursor, right? You had to really... Even if you weren't switching over to a different window, you still had to switch over to a different panel, which itself was a little bit distracting. We eventually came to this idea of inline autocomplete.

Ryan J. Salva (00:23:20):
We were able to with the kind of partnership of some of our friends over on the Microsoft side of things, partner with our friends in Visual Studio Code, they're like, hey, there's not really an extensibility yet in your editor for this multi-line autocomplete, but we've got an idea for how this might work. Played around with the actual presentation of it. What should the key strokes be? What should the presentation layer be? The gray italicized tech seemed to be a good way of indicating that it was ephemeral, as it were. Pretty early on, we landed on this user experience that is Copilot as most developers experience it today. I want to say that was at least 16 months ago, 14, 16 months ago. Since then, we brought it to developers.

Lenny (00:24:15):
Just to double click on that, you're saying just less than a year and a half ago, this kind of really started as a project and now it's out to the world. Is that right?

Ryan J. Salva (00:24:26):
That is exactly right. That's exactly right. It's about a year and a half ago.

Lenny (00:24:30):
That's insane. What was that period between OpenAI almost taking down GitHub to I guess that point?

Ryan J. Salva (00:24:38):
The period in between kind of OpenAI almost taking down GitHub and then us really arriving at the user experience, part of that was, frankly, a lot of really smart researchers at OpenAI experimenting and doing what only world class AI researchers can do. It was a lot of them experimenting, occasionally asking for updates to the data set, tossing back to us a model that we might play with and tinker around with. These models have literally thousands of parameters that you can pass to them. When you're really thinking about GPT-3 and CodeX and then the transition from that to something like Copilot, it was not just like the model...

Ryan J. Salva (00:25:27):
Creating the model is one thing, but then figuring out how to use the model in terms of what parameters do you want to adjust for, what do you want to optimize for in terms of... A great example of this is performance, right? When you're in a code editor, you don't necessarily want to type, type, type and then have to wait one second, two seconds, three seconds to get a suggestion back when your entire goal is to stay in the flow. We would run experiments to see how many milliseconds are the right amount such that a developer doesn't feel like they're being interrupted by Copilot and a suggestion.

Lenny (00:26:06):
What's the answer to that?

Ryan J. Salva (00:26:09):
It seems like right now it's around 200 milliseconds. Depending upon where you're in the world, your latency can go up or down a little bit from there. But it seems like the sweet spot is somewhere around 200 milliseconds.

Lenny (00:26:20):
Good to know.

Ryan J. Salva (00:26:22):
We also experimented quite a bit. It's not just about the model, but it's also about what you feed the model. How do you prompt the model to return back a useful response? This kind of began a journey of experimentation for what we call prompt crafting.

Lenny (00:26:40):
Going back to the way this started, it sounds like basically it was kind of this fortunate accident where OpenAI just did something that you didn't expect. And then somebody within this PhD group that you described is like, "Oh wow. Maybe we could do something really good with this." Is that kind of how it began?

Ryan J. Salva (00:26:57):
That's fairly accurate. Yeah. I mean, we had a model that really was amazingly good, like a step level change in actual intelligence, right? And then marrying that up against a really good use case that actually changes developers' fundamental experience of the creation process, the creative process.

Lenny (00:27:25):
Was there kind of a point at which it was clear to you or leadership in general like, we should double down on this thing and go big? Or this smaller team was working on this idea and then you're like, "Oh wow, this is going to work?" Or is it always like, "We will bet on this thing, this is such a big and great idea. We're going to invest resources for sure from the beginning?"

Ryan J. Salva (00:27:48):
The original team that was working on Copilot at GitHub was the team that we call GitHub Next. Essentially their job is to work on second and third horizon projects. What some folks might call moonshots, right? Things that we never really expect work in the next one or two years, but might three, five years down the line actually turn into something meaningful.

Lenny (00:28:17):
Is there a concrete definition of horizon two and three? Is it like number of years out like Amazon style?

Ryan J. Salva (00:28:23):
Not necessarily a concrete definition. For me, I usually ballpark it as first horizon is the next year, second horizon, the next three years, third horizon, the next five years. But we generally think of it more as a measure of ambiguity and confidence level more than calendar dates.

Lenny (00:28:47):
This episode is brought to you by Modern Treasury. Modern Treasury is a next generation operating system for moving and tracking money. They're modernizing the developer tools and financial processes for companies managing complex payment flows. Think digital wallets via crypto on-ramps, right sharing marketplaces, instant lending, and more. They work with high growth companies like Gusto, Pipe, ClassPass, and Marqeta. Modern Treasury's robust APIs allow engineering to build payment flows right into your product, while finance can monitor and approve everything through a sleek and modern web dashboard.

Lenny (00:29:22):
Enabling realtime payments, automatic reconciliation, continuous accounting and compliance solutions, Modern Treasury's platform is used to reconcile over $3 billion per month. They're one of the hottest young FinTech startups on the market today, having raised funding from top firms like Benchmark, Altimeter, SVB Capital, Salesforce Ventures, and Y Combinator. Check them out at ModernTreasury.com. I'd love to spend a little bit more time on this. It's so interesting. Is this a Microsoft thing, just having these three horizons in a certain percentage of resources or bet on different horizons?

Ryan J. Salva (00:29:58):
I would say it is not necessarily Microsoft thing, but is definitely at GitHub, how we have really contextualized it. Not to say that there aren't teams at Microsoft who might also use that methodology, but where we've been really maybe explicit or intentional about it is at GitHub where we've actually ring-fenced a team to think about that horizon two and horizon three work and kept them separate from EPD. EPD here being engineering, product, and design, the folks who are working on building productized operational products that we bring to market and we either give away or monetize in some way.

Lenny (00:30:39):
This is so interesting. There's a lot of companies that have these sorts of R&D groups, new product experience team at Facebook and Google has one. I'm not sure how many successes have come out of these teams. From what I've seen, and I'm curious, what have you... And clearly you had a huge success as far as I can tell so far. Is there anything you've learned about how to do this, where you invest in these big moonshots within a larger company?

Ryan J. Salva (00:31:05):
I mean, I think the first step is to invest in it. The first step is really hire really smart people, attract smart people, and give them the opportunity to be creative. Don't expect anything out of them that is going to turn into a money maker or something that is going to be beholden to fundamentals around security, privacy, uptime, accessibility, all that groovy kind of stuff upfront. They need space to create and experiment.

Ryan J. Salva (00:31:37):
And also, when you do get to a place where that team has an idea that is clearly connected to a representative set of customers who have a genuine problem and there is signal with at least medium confidence that this solution, whatever it is, solves it in a novel way, that's the time to start thinking about, okay, let's actually put a little bit of... I'm going to call this market testing. It's nothing so formal as market testing. It's really just like, let's start to actually bring prototypes of this in front of more and more customers to kind of test it out and see, hey, is this actually solving a problem for you? Is this something that you would use? This is where the transition between Next and EPD at GitHub really started.

Ryan J. Salva (00:32:35):
This is actually where my role in the product cycle kind of really started to increase. I had kind of been in tight connection and been monitoring the work and kind of consulting a little bit with the Next team prior to that. But it was that moment when we identified that, okay, this is actually something real. Customers are saying, developers are saying, "This is magical. This does something extraordinary that I could not do on my own," that we started to think about, okay, how do we transition this over? From there, we're really just like, okay, we think we've got a hit here. We think we've got something that we can actually bring to developers.

Ryan J. Salva (00:33:21):
We made an intentional decision to take some of the researchers who were in the Next team and for a finite period of time, move them over to create a new EPD squad. We want them to be researchers, but we need to do knowledge transfer and we needed to actually provide the seed for a team that could eventually operationalize and productize. And that kind of began the technical preview where we started to invite tens of thousands, then hundreds of thousands to the technical preview. In that technical preview, we started to see crazy mind-blown emoji tweets and threads on Hacker News about people getting really, really excited about it.

Ryan J. Salva (00:34:09):
That's how we knew it was time to start scaling and it was time to really start thinking about how do we do hiring so that we can build in some insulation around these researchers so that they can eventually go back to GitHub Next to do what they do best, which is be innovative and creative and think about the next moonshot. That process, that took... Well, we're actually still kind of at the tail end of it now. Here we are, like I said, roughly a year and a half after the initial creation of the product, having gone through technical preview, have achieved general availability. We've now hired in a team around them.

Ryan J. Salva (00:34:53):
The researchers actually as early as last month have started to gradually move back over to GitHub Next. An EPD squad, multiple EPD squads actually are now taking the product forward and starting to respond to customer feedback to think about, okay, how do we now as a product team, carry this roadmap forward from an idea that originated in GitHub Next?

Lenny (00:35:22):
I love that insight of bringing the people along and not just kind of like, cool, we'll take it from here. If you were to build a team like this again somewhere to this kind of R&D horizon three or two teams, is there anything else you would do differently, any lessons you take away from this experience for maybe founders or PMs working at larger companies that are like, "Hey, we should have something like this?" Is there anything else that you find is important for making something like this successful?

Ryan J. Salva (00:35:49):
The criteria for moving researchers back into their R&D team, whatever that happens to be for your organization, that can't be based on a calendar. It needs to be based on a replacement in seat, who's actually doing the job and has picked up all of the skills necessary, and only then can the researcher move back. Make sure that you've got continuity of expertise and sets and domain familiarity before you move over. I feel like we've managed that pretty well today. As well, it's critical that the team who is taking over from the R&D shop feels like they have control over their own future. You can't really delegate roadmap to an R&D team.

Ryan J. Salva (00:36:44):
The team who's responsible for maintaining the product, for building the product, who has the closest feedback loop with the end customer, they're the ones who really need to own and feel like they control the roadmap. Making sure that you're not outsourcing innovation exclusively to an R&D team, but that is happening within the product team as they take ownership over the idea and over the use case in the customer. Last I would say here is really that engineering fundamentals in a lot of ways are the contracts that differentiate an R&D team from an operational product team.

Ryan J. Salva (00:37:30):
Bringing that fundamentals process into it is going to feel candidly a little bit unnatural to the researchers. That takes therefore a little bit of cultural change management for everyone to just adapt their way of working and understand that we're graduating from an experiment and a research project to an operational product, and often because those researchers are... They're the first wave that come over. They're the seed of the project. It's going to feel a little bit unnatural to them and they probably won't have all the right skillsets in order to make that transition.

Ryan J. Salva (00:38:08):
Making sure that you've got a good mix of engineers who are comfortable maintaining a service, as well as engineers and researchers who are really thinking about, what is the idea that we've created, what is the new thing that we've brought to market, and can bring that vision to it.

Lenny (00:38:27):
Yeah, I can totally see the challenge that comes from... This was my thing. I've been working on this. What are you guys doing to this project? Where is this going? I'm not sure I'm feeling... And then there's all these new asks that are coming at you like, oh my God, this was so much fun and now I have to scale this freaking thing.

Ryan J. Salva (00:38:46):
I mean, this is the best problem in the world to have. Talk about kind of customer ask, for Copilot in particular, the amount of chatter, the amount of customer feedback that was coming in especially for us with AI, I mean, the world is still figuring out AI, candidly. I mean, we're getting a lot better at it, especially in the last couple of years with things like Dolly and Copilot. But it brings with it not only engineering challenges, but also, frankly, ethical challenges and legal challenges, like making sense of what our expectations are of AI. If AI produces something that is offensive, who's at fault?

Ryan J. Salva (00:39:37):
Our stance on it, what we ended up coming to is actually the framing of Copilot as an AI pair programmer I think is a useful one. Pair programmer, I suspect most of your listeners will know, but pair programmer is usually two developers sitting side by side working on a problem together. One's at the keyboard and the other one's kind of helping them talk through it, talk through the ideas and make corrections, that kind of thing. Well, if Copilot is your AI pair programmer and they're whispering crazy stuff into your ear and they're bringing politics into it or gender identity into it or, I don't know, whatever other...

Ryan J. Salva (00:40:19):
They're spouting off slang and slander and all that kind of stuff. You're probably not going to be able to focus on your work, right? It's going to be really distracting. Really coming down to some principles about what is the use case we're trying to solve, what is appropriate, I put this in scare quotes, behavior of the AI bot sitting side by side with you, helped us create some principles or some guidelines for the developer experience that we wanted to create.

Lenny (00:40:52):
Oh, I love that. Just kind of creating a persona of the thing to help you inform how the behavior of the thing should work. How do you work through these challenges? Is it discussions with you and the legal team? I don't know, these ethical things are really tricky, I imagine. How do you approach them like that as a product team?

Ryan J. Salva (00:41:09):
It is conversations with a very, very wide cast of characters. This product in particular, I probably spent more time with legal than any other products that I've ever kind of been responsible for. All wonderful creative people. But it's not just legal. It is also privacy and security champions. It is, frankly, developers, like the people who are using it, listening to them. Hey, what works here? What doesn't work for you here? Why is this offensive? Why is it not offensive? We'll continue on the example of the crazy pair programmer whispering crazy things into our year. When we first started out, we didn't really have any filter on Copilot whatsoever the very, very, very early days.

Ryan J. Salva (00:41:58):
And then eventually we're like, okay, it needs to be slightly more controlled experience. We need to edit out some of the most egregious stuff. We introduced a simple block list of words, and these block lists are always fraught with peril, like which words are okay, which words are not okay. All of a sudden, we become editors of language and that's kind of a scary place to be. I'm not comfortable with it at least. But at a certain level, it has to be done, because otherwise you're going to create a bad developer experience.

Ryan J. Salva (00:42:35):
Often we would get feedback from developers of like, "Hey, this particular word was blocked. That it was blocked either was offensive to me or prevented me from being able to get good value out of the product."

Lenny (00:42:51):
Oh man.

Ryan J. Salva (00:42:52):
Always kind of dancing the dance of editorial content. We're actually at a place now where we're able to partner with the Azure Department of a Responsible AI, and they've created some really extraordinary models that help detect I'll call it sentiment for lack of a better word, but basically when there is something that is patently offensive. Because there are some words that in some contexts may be offensive and in some context may be totally reasonable, especially when you get into software for medical kind of scenarios, right?

Ryan J. Salva (00:43:35):
Being able to start to shift a little bit to focus or to rely on AI models that can also do a better job than we could with crude or simple block lists is maybe another proof point both of how AI as a solution for common development problems is getting way better at solving more parts of our stack or filling in for more parts of our stack. At least in our case, we were pretty fortunate to be able to deliver on or depend on a parent company's contributions to solve a real acute problem that GitHub probably could not have solved on our own.

Lenny (00:44:16):
I never thought that Copilot would be... That you would have to worry about it saying things that are crazy. That is wild that you guys have to deal with that. Wasn't it Microsoft that had that bot that turned really negative and eventually shut down?

Ryan J. Salva (00:44:31):
It was.

Lenny (00:44:31):
There's experience there.

Ryan J. Salva (00:44:32):
What was its name? Talia or something like that?

Lenny (00:44:35):
Something like that.

Ryan J. Salva (00:44:36):
Yeah, something like that. We don't want another one of those incidences.

Lenny (00:44:40):
Wow. What this makes me think about is your team is at the forefront of AI in this applied way. I'm curious what your thinking is on just where this goes for developers especially. I saw a stat that maybe 40% of people's code is now written by Copilot. I don't know if that's right. But is the vision in the future becomes something like 90? Where do you see this all going?

Ryan J. Salva (00:45:02):
Just to put a fine point on that stat, it is 40% is specifically for Python developers. Candidly, it varies depending upon the language. Because as you might imagine, some languages have better representation in the public domain than others. And usually both the volume and the diversity of training data correlates with the quality of suggestions, which is then represented by either the number of lines written or the acceptance rate or any one of a number of other metrics.

Lenny (00:45:35):
Awesome. Thanks for clarifying.

Ryan J. Salva (00:45:36):
Yeah, totally. We see it range anywhere from the upper twenties to the forties across all the different languages.

Lenny (00:45:43):
Just to throw this out there, as a not great engineer, I used to be an engineer for about 10 years, I welcome our AI Overlords writing all my code. I'm excited for this to do more and more. And yes, I'm curious where you think this goes.

Ryan J. Salva (00:45:58):
It does. It enables even mediocre developers like myself to be able to do some pretty amazing things. But where's it going? First, I think, I hope it's obvious to most developers that AI is going to infuse pretty much our entire development stack in the not so distant future. Copilot is really just the very tip of the sphere for a lot of innovations and better managing maybe our build queues or helping to... Here's a great one. I don't know about you, but often the comments that I get with commit messages and PRs aren't super great. It puts a lot of effort onto the code reviewer to go figure out what the developer was actually trying to do.

Ryan J. Salva (00:46:55):
What if AI could summarize all of your changes with your full request and you just have to, as the contributing developer, just review it to make sure it's accurate, send it on its way, and you don't have to put in extra effort for that. There are lots and lots of different opportunities for AI to essentially be able to take some of the drudgery out of our work so that we can focus on creative acts. What I hear from developers and what I experience myself is that Copilot kind of forces me to think a little bit more about what are the design patterns I'm trying to create?

Ryan J. Salva (00:47:33):
What is the end user experience or the outcomes that I'm trying to drive with my code, and that I can rely on Copilot to scaffold out a lot of that so that I can focus on more creative work? That is really what I hope for our industry five, 10 years from now, is that not only will we be inviting more developers or more people to become developers by essentially providing a layer of abstraction a little bit, or at least a little bit of a hand in development, but that also the really experienced developers are focusing on much larger problems and focusing on outcomes and creativity rather than really low level difficult rote memorization of things like syntax or ordering of parameters and the like.

Lenny (00:48:32):
Great. If nothing else, that'll keep people from just having a tab of Stack Overflow, copy and pasting every function that they're trying to figure out.

Ryan J. Salva (00:48:42):
I want Stack Overflow to stay in business, but I would mind a little bit less contact switching myself.

Lenny (00:48:48):
In the experience of scaling this thing, what would you say has been the biggest challenge either technologically or even operationally just kind of scaling it to a real product that people are paying for?

Ryan J. Salva (00:49:01):
There's a few dimensions of that. One is a problem that's very much of our time in the world, namely that supply chains have been disrupted dramatically over the course of the last few years. It turns out that Copilot for both training and operating the models requires some very rare and unique GPUs that there's not a lot of global supply of. Part of it is just like, can we get enough hardware in order to run these things? We've actually earmarked quite a bit of capacity, and we are greedy, greedy, greedy for more capacity globally. As soon as we can produce those chips and get them in data centers, we do it.

Ryan J. Salva (00:49:50):
That's been one kind of unique challenge. I would also say here that operationally, another challenge has been, how do we create a model that the community really feels like ownership over, right? The dialogue that's had to happen as we brought an AI tool to market, especially one that is trained on public code, has required a lot of dialogue between us and our community. Every good product manager should be spending as much of their time as possible with their customers, with their potential customers.

Ryan J. Salva (00:50:34):
Copilot, in particular, has been a more complicated kind of rollout because we as an industry, as a society are still figuring out how to make sense of it. The amount of give and take between developers and us as a product team has really required us to scale up more of the product team than it has the engineering team.

Lenny (00:51:02):
Interesting. And why is that?

Ryan J. Salva (00:51:04):
It's a couple of different reasons. I mean, one, like I said, we are trained on public code. Not all of the community is really sure like, when is it okay to train a model on public code? When is it not okay to train a model on public code? Is Copilot producing secure suggestions? Is Copilot producing bug buggy suggestions? There's a lot of doubt. There's a lot of very healthy skepticism. Actually I mean that genuinely. I want people to be skeptical of Copilot. We owe it to ourselves as a community to be skeptical of any AI.

Ryan J. Salva (00:51:40):
Because just like there's great potential for benefit, there's also great potential for harm. People keeping us accountable like, how are you preventing things like model poisoning? Is there going to be a new attack vector that we just haven't really thought of yet around AI that might produce negative consequences? We think that we've done a really good and responsible job of that by making sure that first, we are very clear that Copilot is not a replacement for a developer. It will never be.

Ryan J. Salva (00:52:17):
We do not want Copilot auto generating code where a thinking, reasoning, breathing human being is not on the other side of that keyboard making recent decisions. We do not want Copilot to replace any other part of the stack, whether it is static analysis tools or your unit tests or whatever kind of measures you're putting in today to make sure that your humans produce good quality code. We want you to keep all of those same systems in place to make sure that humans who are leveraging tools like Copilot continue to produce that good quality code.

Ryan J. Salva (00:52:56):
But there's a lot of at the same time anxiety of like, where is AI stack? Is AI eventually going to be... This is back to your question about where will we be five, 10 years from now. Will it be writing 90% of the code? We don't want Copilot to be that... We don't want it to replace anything. We want it to augment. The idea here is really that AI is an enabler for developers to focus on the creative work, to stay in the flow, to be able to move faster. Working through those anxieties, working through that healthy skepticism takes conversation. It takes dialogue. And that takes us on the product side having that guided conversation with the community.

Lenny (00:53:50):
It feels like it connects back to your education back in the day, philosophy and literature. How convenient is that?

Ryan J. Salva (00:53:57):
It often feels very connect... I mean, certainly the education side of things taught me that the importance of dialogue, the importance of skepticism is valuable in so much more than esoteric armchair ponderings. It's actually applicable to the real world.

Lenny (00:54:17):
Maybe a final question before we get to our very exciting lightning round.

Ryan J. Salva (00:54:21):
Woo!

Lenny (00:54:23):
Just looking back at this whole experience of, one, just building, incubating, launching this big bold bet within a big company, you can go in either direction, either just any lessons on just taking a bold bet versus incremental wins and how you think about investing in these two kind of categories, or just within a large company, a lesson of just how to build something like this, like a massive new product from just a seed of an idea to a large new business line potentially.

Ryan J. Salva (00:54:51):
As both a product manager and a portfolio manager of multiple products, I'm responsible for multiple product lines at GitHub, the allocation of time, of focus, energy, and resources becomes a really challenging question. The answer to which isn't always the same, depending upon the time, world circumstances, organizational circumstances, technology circumstances. As a general rule, as a general principle, I certainly try to make sure that we're always reserving some capacity for bold, audacious experimental research projects. You can think of those really uncertain bets as being five to 10% of the team's capacity. About 25, maybe 30% of the team's capacity should generally be on just operations.

Ryan J. Salva (00:55:54):
How do we keep our in-market products meeting customer expectations? And then the remainder of it, what is that, about 60% or so, is really on incremental progress for our end market products. How do we make iterative improvements and continue to actually realize payoff for the larger bets that we made one, two, three, four years back? And from a rough distribution, that's generally how I run my larger teams. That works when you have larger teams though. At startups, where we were pretty much only a big bet, obviously your percentages get very different and it becomes a matter of you're all in for that one proverbial lottery ticket.

Lenny (00:56:50):
Awesome. Thanks for sharing that. I was going to ask you the percentages that you recommend. Thank you for getting to that. With that, we've gotten to our very exciting lightning round. I'm just going to ask you five questions briefly and just whatever comes to mind, whatever answer you have. Let's do it. Sound good? Okay. What are two or three books that you recommend most to other people?

Ryan J. Salva (00:57:13):
Oh, good question. One of them is a book on user experience called Make It So. It's a reference back to Star Trek, and the idea here is essentially that user experiences that are presented to us in sci-fi often make their way into our everyday products and tools 20, 30 years down the line. It is a great eye-opening, illuminating and just really fun book. That's one. And then completely different take, I'll go outside of tech and I'll just do entertainment value. There's a David Foster Wallace book called Brief Interviews with Hideous Men that I love. It's a collection of short stories.

Ryan J. Salva (00:58:04):
And essentially what it is, is it is if you're watching a movie and the villain gets their opportunity to have their big speech, which kind of explains why they are who they are, it makes them maybe a little bit vulnerable in that moment, it's that speech 10 times over for different hideous people, terrible, terrible people. Interesting read. I recommend it.

Lenny (00:58:31):
I love that. It reminds me of this book that is the interior design of dictators and they show you their homes of Saddam Hussein, Hitler, and all these guys.

Ryan J. Salva (00:58:43):
Dude! Oh my gosh, that's awesome. I got to find that one. You'll have to send it to me.

Lenny (00:58:47):
I found one at an old bookstore, like used bookstore. I don't know if they're around anymore, but I'll find it. Second question. What's a favorite other podcast that you like to listen to or recommend if there's any?

Ryan J. Salva (00:59:02):
Oh god, there's so many. I consume hundreds of hours of podcasts every month. It is crazy. I can choose many. I'll give you just one. The Memory Palace with Nate DiMeo is an excellent storytelling podcast. He does about 20 minute vignettes, usually selected from kind of American history. He also was the artist in residence at one of the museums in Washington, DC. And if you're ever at I think it's the American History Museum or something like that, if you're ever there, you can go to different rooms in the museum and he'll tell you stories about the objects or the rooms that you see there. It's a magical experience recommended to anyone.

Lenny (00:59:56):
Wow! I love those. What's a recent movie or TV show that you've really enjoyed?

Ryan J. Salva (01:00:00):
I don't know if this counts as recent, but it's one that I watched recently, which was Arrival. Yeah, that counts. Arrival. Movie ostensibly about aliens, but is really about language and memory. I found that really, really compelling.

Lenny (01:00:20):
Have you read Ted Chiang books and short stories?

Ryan J. Salva (01:00:23):
I have not. I have not.

Lenny (01:00:24):
Oh wow! Oh, you would love it. Arrival is from one of his story, I believe, is one of his stories and there's a whole book of many more short stories by the same guy. They're amazing.

Ryan J. Salva (01:00:34):
Brilliant. I've got my weekend cut out for me then.

Lenny (01:00:39):
There you go. Just leave work and get to reading. What's a favorite interview question that you like to ask in interviews?

Ryan J. Salva (01:00:46):
Let's see here. I'll give you a fun one more than it is a challenging one. This is kind of my icebreaker interview question, particularly for more early to mid career product managers. I ask them to teach me something new in one minute. Usually I'll pull up my phone and I'll start the timer. I'll give them a second to think about it and start the timer. They're graded on three different criteria. One is completeness. Did they actually finish the lesson inside of one minute? Two is complexity. It's one thing if you teach me how to, I don't know, pat my head and rub my stomach at the same time.

Ryan J. Salva (01:01:28):
It's another thing if you teach me something about 18th century ardent connection to religious trends at the time. And then last is really clarity. Oh yeah, clarity is the last one. Clarity is like, do I actually understand? Did I learn something by the end of the lesson? Did they convey the idea fully and wholly?

Lenny (01:01:52):
I have to ask, what's the most interesting thing somebody has taught in this question?

Ryan J. Salva (01:01:57):
My go-to kind of throwaway answer there about did they teach me something about 18th century art and its connection to religious trends at the time, someone taught me that. It was astounding. It was actually a university candidate, so someone who was still in university, and she was from Vanderbilt University.

Lenny (01:02:18):
And was that a strong yes hire?

Ryan J. Salva (01:02:20):
It was an extremely strong yes hire. She was freaking amazing. Such a smart person.

Lenny (01:02:28):
Amazing. Final question, who else in the industry would you say you most respect as a thought leader or just influence person?

Ryan J. Salva (01:02:36):
There are many, but I think for today I'd probably beat myself up if I didn't say Uga Damore. Uga is the primary researcher who really kind of is the true innovator for Copilot. He deserves credit for the initial work and is a brilliant technologist and futurists. I really, really respect him a lot.

Lenny (01:03:05):
Amazing. Cool call out. Ryan, this has been so fascinating. You guys are at the forefront of so much interesting work. I honestly can't wait for Copilot for my newsletter so that I can do less work. Maybe that'll come someday. But in any case, I'm excited to see where this whole thing goes. Thank you for being here. Two last questions. Where can folks find you online if they're curious to learn more, reach out? And then is there a way that listeners can be useful to you?

Ryan J. Salva (01:03:33):
Easy one. How can folks find me? I am Ryan J. Salva everywhere, Twitter, GitHub. Pick your choice. LinkedIn, Ryan J. Salva. And then how can folks be useful to me? Please, there is a 60 day free trial of Copilot that is there for everyone to pick up and use. Go try it out. When you do, post either on Twitter or Hacker News or on discussions, GitHub Discussions, your experience.

Ryan J. Salva (01:04:07):
Give us the good feedback. Give us the bad feedback. I am so hungry to see how people are using it in novel ways and where they're running up against the rough edges too. Like I said, there's lots of room for us to grow and improve from here, but I'm pretty confident that developers will be pretty freaking amazed at what it's already capable of.

Lenny (01:04:30):
Awesome. Thanks for being here, Ryan.

Ryan J. Salva (01:04:31):
Yeah, dude, thank you so much. It's been a lot, a lot of fun.

Lenny (01:04:35):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review, as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

