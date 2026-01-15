---
guest: Itamar Gilad
title: Becoming evidence-guided | Itamar Gilad (Gmail, YouTube, Microsoft)
youtube_url: https://www.youtube.com/watch?v=aJWSn-tz3jQ
video_id: aJWSn-tz3jQ
description: 'Itamar Gilad is a product coach, author, and speaker with over two decades
  of experience in senior product roles at Google, Microsoft, and various startups.
  He is also the author of Evidence-Guided...

  '
duration_seconds: 4372.0
duration: '1:12:52'
view_count: 14878
channel: Lenny's Podcast
keywords:
- growth
- activation
- onboarding
- churn
- metrics
- okrs
- roadmap
- prioritization
- user research
- mvp
- iteration
- experimentation
- analytics
- revenue
- culture
---

# Becoming evidence-guided | Itamar Gilad (Gmail, YouTube, Microsoft)

## Transcript

Itamar Gilad (00:00:00):
You fake it, you do a fake door test, you do a smoke test, Wizard of Oz tests. We used a lot of those in the tabbed inbox by the way, one of the first early versions was actually we showed the tabbed inbox working to people. But it wasn't really Gmail, it was just a facade of HTML and behind the scenes and according to the permissions that the users gave us some of us moved just the subject and the sender into the right place. So initially the interviewer kind of distracted them and then showed them their inbox and then the top 50 messages were sorted to the right place more or less if we got it right. And people were like, "Wow, this is actually very cool." But it gave us some evidence to go and say, "Hey, we should try and build this thing."

Lenny (00:00:43):
Welcome to Lenny's Podcast where I interview world-class product leaders and growth experts to learn from their hard won experiences, building and growing today's most successful products. Today my guest is Itamar Gilad. Itamar, is a product coach, author, speaker and former longtime product manager at Google where you worked on Gmail, identity and YouTube. He also just published an awesome new book called Evidence-Guided: Creating High-Impact Products in the Face of Uncertainty. Itamar, has an important perspective on why and also how you can push your team and organization from an opinion-based decision-making process to a more evidence guided approach. In our conversation, Itamar, shares a number of very practical and handy frameworks that do just that including the confidence meter, metrics trees, GIST and the GIST board, plus his take on how people often misuse ICE for prioritizing ideas. Also, how you could make your OKRs more effective and so much more. Enjoy this episode with Itamar Gilad, after a short word from our sponsors. This episode is brought to you by Ezra, the leading full body cancer screening company.

(00:01:49):
I actually used Ezra, earlier this year unrelated to this podcast completely on my own dime because my wife did one and loved it and I was super curious to see if there's anything that I should be paying attention to in my body as I get older. The way it works is you book an appointment, you come in, you put on some very cool silky pajamas that they give you that you get to keep afterwards. You go into an MRI machine for 30 to 45 minutes and then about a week later you get this detailed report sharing what they found in your body. Luckily, I had what they called an unremarkable screening which means they didn't find anything cancerous. But they did find some issues in my back which I'm getting checked out at a physical next month probably because I spend so much time sitting in front of a computer. Half of all men will have cancer at some point in their lives, as will one third of women. Half of all of them will detect it late.

(00:02:40):
According to the American Cancer Society, early cancer detection has an 80% survival rate compared to less than 20% for late stage cancer. The Ezra, team has helped 13% of their customers identify potential cancer early and 50% of them identify other clinically significant issues such as aneurysms, disc herniations, which may be is what I have or fatty liver disease. Ezra, scans for cancer and 500 other conditions in 13 organs using a full body MRI powered by AI and just launched the world's only 30-minute full body scan which is also their most affordable. Their scans are non-invasive and radiation free and Ezra, is offering listeners $150 off their first scan with code Lenny150. Book your scan at ezra.com/lenny. That's E-Z-R-A.com/lenny. This episode is brought to you by Vanta, helping you streamline your security compliance to accelerate your growth. Thousands of fast-growing companies like Gusto, Quorum, Quora and Modern Treasury, trust Vanta to help build, scale, manage and demonstrate their security and compliance programs and get ready for audits in weeks not months. By offering the most in-demand security and privacy frameworks such as SOC 2, ISO 27001, GDPR, HIPAA, and many more.

(00:04:02):
Vanta, helps companies obtain the reports they need to accelerate growth, build efficient compliance processes, mitigate risks to their businesses and build trust with external stakeholders. Over 5,000 fast-growing companies use Vanta to automate up to 90% of the work involved with SOC 2 and these other frameworks. For a limited time Lenny's Podcast listeners get $1,000 off Vanta. Go to vanta.com/lenny, that's V-A-N-T-A.com/lenny to learn more and to claim your discounts get started today. Itamar, thank you so much for being here. Welcome to the podcast.

Itamar Gilad (00:04:40):
It's a pleasure being here, thank you for inviting me.

Lenny (00:04:42):
It's my pleasure. I thought we'd start with the story of your work on Google+ and Gmail and how those experiences formed your perspective on how to build a successful product. Can you share that story?

Itamar Gilad (00:04:57):
Google+ was my first experience at Gmail, I joined Gmail in August 2011 and the first thing they asked me is, "Let's connect Gmail with Google+." If you're hazy about the story, back then Facebook was massive. It's still massive but then it was growing like mushrooms, people were spending hours. That really freaked out Google and the obvious solution was to launch a social network of Google called Google+ and we all believe in this thing, it really caught on very well initially we all used it, we all believed in it. So our mission was to build this thing and Google really cut no costs. It created a whole new division within Google and it created a whole strategy around Google+ and we had to connect Gmail and YouTube and search to Google+ to make them more personalized in a sense and more social. So that was the idea and we went on and we launched a series of features in Gmail for a couple of years, honestly and Google+ itself became this massive project, very feature rich and with a lot of redesigns and iterations and none of it worked.

(00:06:09):
It turned out people actually didn't need another social network, people didn't love it, people didn't use it. Eventually in Gmail we rolled back all the Google+ integration a few years later and Google+ itself was shut down in 2019. So putting aside all the tremendous waste that went into this, all the millions of person hours and personal weeks. In hindsight, not only did Google bet on the wrong thing it missed much easier opportunities. So just not far from Google's headquarters there was WhatsApp, not very famous in the US but they actually created massive impact. Hundreds of millions of people were using their stuff and they became a threat to Facebook much more than Google was. So Google missed the opportunity of social mobile apps like WhatsApp, like Snapchat, etc and for me this story kind of was the epitome of what I call today, opinion-based development. We come up with an idea, we believe in it, all the indications show it's good.

(00:07:13):
Maybe the early tests show it's good, then we just go all in and we try to implement it and I made this very mistake many times as the product manager, I was the guy pushing for the ideas. So for me, this was kind of a turning point I felt we need to adopt a different system.

Lenny (00:07:32):
And just before you move on to the next story, how big was the team? Roughly how many years was spent on this area? Just to give people a sense of the waste as you said.

Itamar Gilad (00:07:41):
So there was a tremendous earthquake inside Google to create the Google+ team, teams and the entire divisions were kind of thrown apart and reformatted and I think at its peak it was about 1000 people inside-

Lenny (00:07:55):
Wow, [inaudible 00:07:56].

Itamar Gilad (00:07:56):
It was a division the size of Android and Docs and a really sizable thing, they're under their own buildings. It's taken from the playbook of Steve Jobs, create this whole secretive project inside and just run like hell.

Lenny (00:08:13):
Yeah. I remember though Facebook was really scared, I remember they shut everything down. It as like a code DEFCON one situation too, so it really scared Facebook at the same time.

Itamar Gilad (00:08:22):
Yeah, it's true. But at the end of the day, neither Google's advertising revenue was affected, neither was Facebook affected. So it turned out this idea was not that necessary after all.

Lenny (00:08:35):
Yeah, okay. So that's an example of something that didn't work because it was opinion based software, I think the phrase you used and then there's a different experience with tabs I think with Gmail.

Itamar Gilad (00:08:47):
That's right. So Google, is a very successful company. It's not for me to criticize it or to in hindsight kind of say you guys need to be better and some of the people that were behind Google+ was some of the smartest leaders and I still think they are despite this story. If you look back at the history of Google, how things started in the first decade or so. Google, was what I call an evidence guided company. So essentially it put a high premium on focusing on customers, coming up with a lot of ideas on looking at the data, looking at how these ideas actually worked out. They weren't shy about launching betas and things that were very rough and incomplete and learning from that and then they expected people to take action based on the results. So fail fast is a very famous paradigm and so you had to kill your project or pivot it seriously if it didn't work out and I think had we kept fail fast it would've really have helped Google+, if we had this mentality.

(00:09:56):
But for some reason with Google+, Google put this playbook aside and used a different playbook which I call plan and execute essentially. But I think inside Google the DNA still existed. So inside Gmail, the next project after Google+ was the tabbed inbox. So it was kind of the reverse of Google+, it started as a very small idea that no one believed in and we started looking what's behind the city? What's the goal? What's the problem actually we're trying to solve? It turned out that a lot of people were receiving social notifications and promotions, etc, and most of them were very passive. They weren't clearing their inbox, they were just living in this world of clutter and I came up with an idea how to fix this. I was sure it was great, I wanted to push it, plan and execute, but my colleagues were like, "Hold on, we actually tried this. We have a bunch of ideas to help people organize their inbox, they're not using it. Why is your idea good?"

(00:10:57):
So that sent us, kind of me and my team into researching these users into establishing a goal that was much more user-centric and then thinking of other ideas. And then we started testing them much more rigorously and basically we started testing on our own inboxes and then we recruited other dog footers, other Googlers to test the same inbox, then we put it outside for external testers. We did usability studies, we did data, we built a whole data mining team and a whole machine learning team to build the right categorization and we ended up with a solution that turned out to be very successful for a lot of these passive users. This was a surprise to a lot of people because most of my colleagues and most of the people I talk with actually know how to manage their inbox. So for them that solution makes complete nonsense, like splitting promotions and social to the side sounds like the stupidest idea. But there's about 85% of the population, 85 to 88% that absolutely love it and today Gmail has about 1.8 billion active users according to Gmail.

(00:12:14):
Most of these users are using this feature, so it was a pretty high impact feature as well.

Lenny (00:12:20):
And the feature specifically, just in case people aren't totally getting it is the promotions folder and the social I think and then the regular.

Itamar Gilad (00:12:27):
Yeah, there are a couple more that you can enable in settings if you like.

Lenny (00:12:30):
Yeah, I use it, I love it. Except it puts my newsletter in people's promotions folder, who do I talk to about that?

Itamar Gilad (00:12:36):
Yeah. Newsletters are a very complicated scenario for the categorization engine.

Lenny (00:12:41):
Yeah. We just need an exception for my newsletter and then we're good. Okay, but go on.

Itamar Gilad (00:12:45):
So in hindsight I was asking and saying, "Why was this project so different?" And I think the reason is that we didn't have that much confidence in our opinions. We had opinions, we had ideas but we didn't just go all in and just let's build it. We actually used an evidence guided system and I think that's not unique just to Google. I think every successful product company out there that you look at Amazon, Airbnb, anyone you will check, at least in their best periods they found a way to balance human judgment with evidence. They didn't try to obliterate human judgment and opinion just to supercharge them with evidence and they came up with very different models. Apple, is another example but the principle still holds in all of these companies.

Lenny (00:13:33):
Awesome. So you took that experience and all the experience you've had from coaching product leaders working with companies and you wrote this book called Evidence-Guided, which people on YouTube could see sitting there behind you. So I want to talk through some of these stories and then some of these other lessons and frameworks that emerged. But maybe just to start, what's the elevator pitch for this book?

Itamar Gilad (00:13:55):
So this is a book for people like us, product people who want to bring evidence guided thinking or modern product management if you like into their organizations. There's a lot of challenges, it's not simple, we all read the books, we all know the theory, we all know some parts of the system. It tries to give you a system how to do that, it's a meta framework that kind of helps you lift your organization in the direction of evidence guidance if that's what you want to do.

Lenny (00:14:23):
So going back to the story briefly before we get into the frameworks and lessons of the book. In the first example of Google+, basically it came top down, "Hey, we need to build a social network, go build it." Obviously that happens at a lot of companies, I don't know if there's an easy answer to this. But are there cases where it does make sense to approach it that way? Obviously Apple is a classic example of Steve Jobs, is like we need to build an iPhone. I don't know if that's exactly how it went. But are there instances where it is worth just approaching new product ideas that way based on the experience and creativity and insights of the founder? Or is your thinking it should always come from this evidence-based approach?

Itamar Gilad (00:15:01):
I think the founders are very important, especially in the startup and scale-ups phase. They come up with many of the most important ideas and it's super important that they have the space to express and to push the organization to look at those. However, it's not about shutting them down it's about looking at them critically. You need to create the environment in the organization where the leader comes and says, "You know what? I talked to these three customers, I figured it out. Here's what we need to do in the next five years." And you need to ask, "Where's your evidence?" And by the way, the example you give that's a classic example. Steve Jobs, he just brainstorm in his kitchen the iPhone and then just told the team to build it. That's the story Steve Jobs, told but it's not the real story at all. Now we know what actually happened and the iPhone has actually a story of discovery, of trial and error, multiple projects to do it, multitouch with phones, most of them failed.

(00:16:02):
Steve Jobs, was the architect. He kind of managed to connect the dots and eventually come up with this perfect device but he wasn't actually the creator, it wasn't his brainchild. He was actually against it for a while but over time as he saw the evidence, as he saw what this thing can do, as he saw the demos he was able to piece together something that was very useful.

Lenny (00:16:26):
That's really important insight. People that are hearing this might feel like I like this idea of pushing back and encouraging the founders to make it more evidence guided. In the case of say Google+, was it even possible? Could you have come to Larry and Sergey and be like, "Here's all this data I've gathered that tells us this is not going to work?" Do you have any advice for how to push back and encourage the founders and execs to really take the counterpoint seriously or really kind of vet their idea?

Itamar Gilad (00:16:58):
So another nice thing about Google is that it's a very open culture and people are not shy to tell even Sergey and Larry that they are wrong and they do this all the time. In certain forms, right? You need to know the right channels. But there was a very big discussion about Google+ and whether it's the right thing to create a clone of Facebook, there was a very public internal discussion. I think what I would change is not have this discussion based on opinions, because when you have the discussion you come with your own opinions usually the most senior person's opinions will win. That's just the way it is. If we had come with hard data and we said, "Listen, things are not actually panning out the way you guys are expecting. What can we do? Should we continue? Should we pivot this?" I think the discussion would've done better. Now I'm doing a huge disservice, I was not in all the discussions. I know probably in Google+, there were very serious discussions happening along these lines.

(00:18:02):
But it's just as a general trend, I find that evidence is very empowering for us smaller people in the organization or mid-level managers to be empowered to challenge the opinions.

Lenny (00:18:15):
Is there anything tactically you found to be useful and effective in giving people, say they don't work at Google. They work at companies where founders and bosses and execs are not as open to challenge. [inaudible 00:18:26] any tactically found about how to present a counter proposal or like, "Hey, I have this data that we should really pay attention to?"

Itamar Gilad (00:18:33):
I think if you come with data, if you run a secret experiment and you come back and you show them you usually get one of two results. Either they get extremely mad at you and they tell you to get back to work and to do what you were told and in that case, probably you need to start polishing your resume and look for another place either inside the organization or outside it because that person is not being reasonable to be honest. But the more common case is they're pleasantly surprised and that's what happened with Steve Jobs, as well. He was against phones but then people showed him all sorts of evidence that Apple can make a phone. He was against multitouch initially but then he changed his mind, there was a lot of back and forth. So even, Steve Jobs, given evidence was willing to flip and I say this in many organizations. So evidence is so powerful, that's why this is the principle I based the book on.

Lenny (00:19:28):
You have this concept of being evidence guided. People listening may feel like, "Hey, we're evidence guided, we're in experiments, we make decisions using data." Oftentimes they aren't actually and so what are signs that maybe you're not actually that evidence guided or as evidence guided as you think you are?

Itamar Gilad (00:19:45):
I think there's a few telltale signs that I look for, first the goals are very unclear. Either there are many or they're very kind of obscure and vague or they are about output, there's misalignment. So the goals part is not there, usually this goes hand in hand with metrics. Missing metrics or just using revenue and business metric but there's no user facing metrics. So that's another telltale sign, then there's a lot of time and effort spent on planning especially on road mapping. Creating the perfect roadmap which really can consume a lot of time of the top management and PMs, etc. Then as you go down you see there's not a lot of experimentation and if there is experimentation there's not a lot of learning and finally another telltale sign is that the team is disengaged. So the engineers are kind of getting the signal that what they need to do is deliver, they're focused on output, that's what they're measured on. So they're kind of disengaged, they're disengaged from the users, from the business, they don't care that much.

(00:20:57):
It's usually something that you can fix by adopting a more evidence guided system.

Lenny (00:21:05):
Okay. So let's dive into your approach to becoming more evidence guided. In the book, you share this model that you call the GIST model which is kind of this overarching approach to building a product that almost forces you to be more evidence guided. So let's just start with what's the simplest way to understand this GIST model?

Itamar Gilad (00:21:26):
With your permission, I can show a few slides.

Lenny (00:21:28):
Oh, let's do it.

Itamar Gilad (00:21:29):
And maybe that will help.

Lenny (00:21:32):
Here we go, and then yeah, a good excuse to go check this out on YouTube.

Itamar Gilad (00:21:36):
All right, you're seeing this? So this is the GIST model, goals, ideas, steps and tasks, and essentially it's tries to break the change which is a really big change for a lot of companies into four slightly more manageable parts. They're still big but each one you can tackle on its own and that's kind of the reason I kind of split it, and goals are about defining what we're trying to achieve, ideas are hypothetical ways to achieve the goals, steps are ways to implement the idea and validate it at the same time. So essentially build, measure learn loops and tasks are the things we manage in Kanban and Jira and all these good tools. These are the things that your development team is usually very focused on and just listening to this, a lot of this will sound familiar to you because GIST is not a brand new invention. It's a meta framework that puts in place a lot of existing methodologies. It's based on lean startup, on design thinking, product discovery, growth, There's a lot of all of these things here. It just tries to put them all into one framework or one model.

Lenny (00:22:43):
So what's the simplest way to think about what this model is meant for? Is this how you think about your roadmap? Is this how you plan? What is this trying to tell people to do differently in the way they build product broadly?

Itamar Gilad (00:22:56):
I would say these are four areas that you need to look at and ask, are we doing the right thing in each? In each you may need to change or even transform and as I go and explain each one of those I'll give you basically three things. In each chapter in the book I try to touch on three things. The principles behind them, the frameworks or models that implement the principles and then process and the process honestly is the most brittle part and the one that you would need to change and adapt to your company. Because not two companies are exactly the same, and it's very tempting when you write a book not to give any process but that's the part that people actually want the most. So it's included as well, but just be aware that you will have to change this process.

Lenny (00:23:44):
Awesome. Okay, so we're going to talk about each of these four layers. Before we do that, where do vision and strategy fit into this? Do they bucket into one of these four layers and how do you think about strategy and vision?

Itamar Gilad (00:23:55):
That's a great question, so there's this whole strategic context that is outside of GIST. GIST, is not trying to tackle that, it assumes it's in place, there's another huge blob which is research. GIST, is not about research it's more about discovery and delivery. But strategy is extremely important and you can use some of the tools we will talk about to develop your strategy as well. In many companies the strategy is just a roadmap on steroids, it's small plan and execute just on a grand scale and Google+ again, was a strategic choice actually if you think about it. So in the book there is a chapter where I touch on strategy and I explain how the same evidence guided methods are being used by companies to develop their strategy as well.

Lenny (00:24:43):
Awesome, maybe one last context question. So people might be seeing this and thinking okay cool, I have goals, I have ideas steps, I have tasks, I'm already doing this. What is this kind of a counter or reaction to? What are people probably missing when they're seeing this and they're like, "Oh, I see. This is like what we're not doing and this is the most important, this is something we should probably change." And we'll go through these in detail too.

Itamar Gilad (00:25:03):
I think talking about each one will help.

Lenny (00:25:06):
Okay, let's do it.

Itamar Gilad (00:25:09):
But we can talk about in each level what's actually being done. So when people say I have goals, usually they take the goals layer and use it as a planning session. They talk about what shall we build by when, what are the resources? And that's actually not goals at all, that's planning work.

Lenny (00:25:26):
Cool, let's talk about goals and I know part of this is OKRs related too, so I'm excited to hear your take on OKRs.

Itamar Gilad (00:25:33):
Oh, that's a whole different discussion. You had, Christina, the real expert over there so I doubt I can add more to that. But it's true OKR is all part of it, but let's start with goals. What's our goals supposed to be? Goals are supposed to paint the end state to define where we want to end up and the evidence will not guide you unless you know where you want to go, and in many companies what you have is goals at the top for revenue, market share, whatever it is, and then a bunch of siloed goals for each department. There's engineering goals, there's design goals, there's marketing goals, etc, and that actually pushes people into different vectors and it's really hard to decide. I would argue that in evidence guided companies, and you've worked for a few so probably you've seen this. They use models in order to construct overarching goals for the entire organization. One of the models I show in the chapter about goals is the value exchange loop.

(00:26:34):
 Where basically the organization is trying to deliver as much value as it can to the market and to capture as much value back, and by creating a feedback loop between these two you are actually able to grow very fast. Now, I would argue that you want to measure both of these and to put a metric on each and the metric we usually use to measure value delivered is called the North Star metric. I know you wrote an article, a very good article about it.

Lenny (00:27:01):
Thank you.

Itamar Gilad (00:27:02):
And in it you listed dozens and dozens of companies, like leading companies and what they considered the North Star metric is super interesting. I would argue that what they told you is what is the most important metrics we measure? What is the number one metric for us? But it's not what I call the North Star metric, the North Star metric measures how much value we create for the market. For example, let's take WhatsApp. WhatsApp for a very long time measured messages sent because every message sent is a little incremental of value for the sender, the receiver, it's free, it's rich media, you can send it for anywhere in the world, compared to SMS that's huge value. So if in year one we have a billion messages being sent in year two, two billion probably we doubled the amount of value. In Airbnb, I think one of your key metrics or the real North Star metric was nights booked. I don't know if it was still the case while you were there?

Lenny (00:27:55):
Yeah, absolutely.

Itamar Gilad (00:27:56):
And there are examples like this in Amplitude for example, they measure active learning users or weekly active learning users. Which are users that found in the tool some insight that was so important that they shared it with at least two other users and they consume it. So it's a very powerful thing to point at this metric and say, "This is the most important metric combined with the value metric that we want to capture, revenue, market share, whatever it is." Once you have these two, you can further break them down into what I call metrics trees. So there's a metric three for the North Star metric and there's the metric three for the top KPI, the top business metric which you see here on the left side in blue and usually they overlap. So you might find in the middle some metrics that are super, super important because moving them actually moves the needle on everything else.

Lenny (00:28:57):
Can you clarify again the difference between what you call this top KPI versus North Star metric?

Itamar Gilad (00:29:02):
So the North Star metric is measuring how much value we're creating for the user, the core value that they're getting. In this case this is some productivity suite, so this is number of documents created per month for example. Because we think that every document created maybe it's a small document, I don't know. AI is in fashion now, is a little incremental value, so that's the number we're trying to grow. The top KPI is what we expect to get, it should be revenue or profit.

Lenny (00:29:31):
I see, this is the value exchange. I see, one is what users are getting, one is what you're getting back from them.

Itamar Gilad (00:29:36):
Exactly.

Lenny (00:29:37):
Basically how the business is benefiting. Awesome. I think this is a really important concept, the metric tree. I think a lot of people think they have something like this in mind where they're just like, "Cool, here's our North Star Metric, here's the levers and things that we can work on to move that." But I think actually mapping it out the way you have it here where it kind of goes layers and layers deep to all of the different variables that impact this metric. Not only is it a way to think about impact and goals and things like that, but also helps you estimate the impact of the experiment you're potentially thinking about running. So if you're going to work on something at the bottom here like activation rate, say you move that 10%. How much is that going to impact this global metric? It's probably a very small amount.

Itamar Gilad (00:30:19):
This is a very important one and we'll talk about impact assessment shortly, this helps with it. It also helps with alignment because the entire organization is trying to move these two metrics, it's the two sides of our mission essentially. We have the mission that's the top objective of the company and these are the two top most key results if you like, the top most things. So when you go and work with another team and you say, "Hey, why don't you work on my project?" They might say, "This idea actually might move the North Star metric model in your idea." And that helps you guys align and I've seen cases where team B put aside their own ideas to jump on the ideas of team A, because of this model. It also creates an opportunity to give some sub metrics to teams to own on an ongoing basis, so it creates a little sense of ownership as well and mission within the tree.

Lenny (00:31:10):
It also helps you figure out what teams you should have, which teams have the biggest potential to impact the metric.

Itamar Gilad (00:31:18):
Another thing that happens in a lot of organizations, the team topology reflects the structure of the software or some hierarchical model where we want to organize the organization in a particular way. But if you start with a metrics tree, you can try to arrange the topology around goals and sometimes you need to readjust. It's not a constant reorg but from time to time you will realize the goals have changed and we need to reorganize, so the tree helps visualize that as well.

Lenny (00:31:49):
I think for people that are listening to this and thinking about this, I think the simplest way to even think about this is basically there's a math formula that equals your North Star metric or your revenue or whatever you're trying to do and if you don't have some ideally really clear sense of what that math formula is you should work on that. Because that will inform so much of how you think about where to invest, what teams to have, where to invest more resources, less resources.

Itamar Gilad (00:32:13):
Right.

Lenny (00:32:15):
Imagine a place where you can find all your potential customers and get your message in front of them in a cost-efficient way. If you're a B2B business, that place exists and it's called LinkedIn. LinkedIn Ads allows you to build the right relationships, drive results, and reach your customers in a respectful environment. Two of my portfolio companies Webflow and Census are LinkedIn success stories. Census had a 10x increase in pipeline with the LinkedIn startup team, for Webflow after ramping up on LinkedIn in Q4 they had the highest marketing source revenue quarter to date. With LinkedIn Ads, you'll have direct access to and can build relationships with decision makers including 950 million members, 180 million senior execs and over 10 million C-level executives. You'll be able to drive results with targeting and measurement tools built specifically for B2B. In tech LinkedIn, generated two to five X higher return on ad spend than any other social media platforms. Audiences on LinkedIn, have two times the buying power of the average web audience and you'll work with a partner who respects the B2B world you operate in.

(00:33:20):
Make B2B marketing everything it can be and get $100 credit on your next campaign, just go to linkedin.com/podlenny to claim your credit. That's linkedin.com/podlenny, terms and conditions apply. Okay. So metrics trees, what comes next?

Itamar Gilad (00:33:39):
All right. So next we need to go to the ideas layer and the ideas layer is there to help us sort through the many ideas we might encounter and they may come from as you said the founders, the managers, the stakeholders, from the team, from research, from competitors. We're flooded with ideas, and what usually happens inside organization is some sort of battle of opinions or some sort of politics sometimes or highest paid person's opinion. You had, Ronny Kohavi, who invented this term in your show. What doesn't happen is very rational, logical decisions these are the best ideas, because it's really, really hard to predict honestly. There is so much uncertainty in the needs of the users, in the changes in the market, in our technology, in our product, in our own organization. It's almost impossible to say this idea is going to be the best, but we do say this because we have cognitive biases that kind of convince us that this idea is far superior to anything else and it's definitely the right choice.

(00:34:48):
In order to avoid this, what we want to do is to evaluate the ideas in a much more objective and consistent and transparent way. In the book I suggest using ICE, impact, confidence and ease. I think I have a slide coming on this. So impact, confidence and ease which is basically a way to assign three values to each idea. The impact tries to assess how much impact it'll have on the goals and that's why it's so important that we have very clear goals and not many. How we are measuring the ideas on the North Star metric, on the top business KPI, on a local metric of the team. Whatever it is, let's be clear about it and then let's evaluate the ideas against this thing. Ease, is basically the opposite of effort. How easy or hard it's going to be, but both of those are guesstimates, both of those are things we need to estimate. I would argue that just by breaking the question to these two questions we usually have a slightly better discussion than just my idea is better than yours.

(00:35:52):
But then there's the third element which is confidence, which tries to assess how sure are we or should we be about our first guesstimates about the impact and the ease.

Lenny (00:36:03):
It's interesting you use the word ease, because I think it's usually effort. You kind of make it positive, is that an intentional tweak you made?

Itamar Gilad (00:36:12):
I'm using the definitions of, Sean Ellis. Sean, invented ICE. You know Sean, I don't know if you've had him yet? But he's-

Lenny (00:36:21):
I haven't had him on yet.

Itamar Gilad (00:36:23):
Yeah. For the people who don't know him, Sean, is amazing. He's like one of the fathers of the growth movement, he coined the term growth hacking and he popularized the concept of product market fit.

Lenny (00:36:36):
Yeah.

Itamar Gilad (00:36:36):
He created ICE, he created a bunch of things that we use in product that we don't even know.

Lenny (00:36:40):
Wow, I didn't know he came up with ICE. Okay, cool. So the original version of ICE is ease instead of effort.

Itamar Gilad (00:36:45):
Exactly, yeah.

Lenny (00:36:45):
Fun fact.

Itamar Gilad (00:36:47):
A lot of your viewers are wondering where's the R because there's another variant of this culture. RICE, where there's rich as well. I prefer ICE because I prefer to fold the rich into the I for various reasons but both are valid, both are equivalent in a sense.

Lenny (00:37:04):
I'm in your boat, that's exactly how I think about it. I think people over complicate this stuff and try to get so many math formulas involved with estimating impact, and I feel like these are just simple heuristics to kind of bubble the best ideas to the top. It doesn't have to be a perfect estimate of impact and confidence and all those things, so I think the simpler is better and it always ends up being a spreadsheet. People always have these tools to estimate these things but it's like a spreadsheet, Google Sheets. Great.

Itamar Gilad (00:37:28):
So yeah, you're actually leading me to my next point. So when you come to estimate impact you will realize it's the hardest part. So sometimes it's just a gut feeling and it's a guess and sometimes it's based on some spreadsheet or some analysis and the back of envelope calculation you've done and I think that's legitimate. Sometimes these things do show you some things you didn't think of and sometimes the best case it's based on tests. You actually tested it, you interviewed 12 customers, you show them the thing and out of those only one actually liked it. You should reduce your impact based on that usually, or you do other types of tests. We'll talk about testing in a second. What happens is that people tend to just go with gut instinct and then give themselves a high confidence. They say it's an eight and I'm pretty convinced, so it's eight for confidence and I found this a bit disturbing because it kind of subverts the whole system.

(00:38:22):
So I wanted to help people realize when they have strong evidence in support of their guesses and when it's weak evidence, how to calculate confidence in a sense. For that I created a tool called the confidence meter, which you can see here this colorful thing and should I go and explain it?

Lenny (00:38:41):
Yeah, let's do it. And then again, if you're just listening to this you can check this out on YouTube and you can see the actual slide.

Itamar Gilad (00:38:47):
All right, awesome. So basically I constructed it a bit like a thermo meter. It goes from very low confidence which is the blue area or the upper right, all the way to high confidence which is the red area and you can see the numbers going from zero to 10. Where zero is very low confidence, we don't know basically anything we're just guessing in the dark and 10 is full confidence. You know for sure this thing is a success, no doubt about it and across the circle I put various classes of evidence you might find along the way. So for example, starting at the top right, all of these blue areas about opinions. It could be your own self-confidence in the idea, your self conviction, you feel it's a great idea. Guess what? Behind every terrible idea that was ever someone thought it was great, that gives you 0.01 out of 10. Maybe you created a shiny pitch deck or a six-page document that explains in detail why this is a great idea. Slightly harder to do but still very low confidence, maybe you connected it to some theme, it's about the blockchain...

(00:39:59):
Well sorry, the blockchain is out of fashion. What's hot right now?

Lenny (00:39:59):
AI.

Itamar Gilad (00:40:04):
Exactly, AI. It's about AI, that makes it a good idea? Absolutely not. Or the strategy of the company, that's another thematic support. Thousands and thousands of terrible ideas are being implemented right now as we speak based on these themes. So all these things combined can give you a maximum 0.1 out of 10 according to the tool, if you follow it then we move into slightly harder tests. One is reviewing it with your colleagues, your managers, your stakeholders the idea. They don't know it either, they don't have a crystal ball, they're usually not the users, they cannot predict. But they can evaluate it in a slightly more objective way and maybe find flaws in your idea. On the other hand groups tend to have biases too, politics group thing. So groups can actually arrive sometimes with worse decisions than individuals, there's some research to that. Next, our estimates and plans. So you may do some sort of back of the envelope calculation or your colleagues might go out and try to evaluate the ease a little bit better.

(00:41:07):
That gives you a little bit more confidence, but still we're at the level of guesswork at this point. Next we're moving to data and data could be anecdotal. So you find a few data points dotted across your data or you talk to a handful of customers or maybe one competitor has that same idea. In many companies I meet, if the leading competitor has this feature and we think it's a good idea validation is done. Let's launch it, that's it. It's a great idea, we need to do it. It never works honestly, you should not assume that your competitor actually knows what they're doing anymore than you do. Data could be also what I call market data. That comes from surveys, from assessing a lot of your data by doing a deep competitive analysis and there are other methods where you create a larger dataset and you contrast your idea against it. Finally, to gain medium and high confidence you really need to build your idea and test it and that's where the red area is.

(00:42:11):
So there's various forms of tests, we'll talk about them if we have time and they give you various levels of confidence.

Lenny (00:42:19):
Awesome, this is a very cool visual. We'll link to a image of this in the show notes too if people want to check it out. I think what's awesome about this is you could just use this as a little tool on your team of just like where are we along the spectrum? We think the impact of this is very high. But we're probably in this blue area of confidence and so let's just make sure we understand that and it's really clear language to help people understand. I see if we had this, it'd be a lot more confident.

Itamar Gilad (00:42:45):
So you can also tie your investment into the idea based on the level of confidence you had found essentially, so early on you want to do the cheap stuff just to gain more confidence and then you can go and invest more. If it's a really cheap idea, you can jump to a high confidence idea, you can test, you can do an AB experiment. Early adopter program, whatever it is and then launch it. Some ideas you don't need to test, sometimes the expert opinion is enough. If you're just changing the order of the settings, no one sees this or no one will be impacted. The risk is low, you can launch it without testing. So part of the trick is also knowing when to stop, not just trying to force your way all the way up when you don't have to.

Lenny (00:43:31):
That's a really important point. The other important point here is just a big part of a PM's job is to say no and to stop stupid shit from happening and this is an awesome tool to help you do that. To be like, okay, here's this idea you have, just like let's just be real, how confident are we in this? And, okay, it's going to take us three months to do this. Maybe we should think about something different, maybe we should work up the confidence meter before we actually commit to this.

Itamar Gilad (00:43:56):
Yeah. This is a real world usage that I hear about a lot, some people use this to kind of do... An objective way to say no and gently. Or to say we'll think about it but look at these other ideas we have and how their impacting is and confidence stack up.

Lenny (00:44:12):
Classic PM move, just like that was a great idea but what about this better idea? Coming back to something that we talked a bit about at the beginning, say you have a founder who's actually very smart and experienced. Say even at a startup where you don't really have the time to build tons of evidence for ideas. Do you have a different perspective on how much time to spend building confidence in ideas versus just like cool, they actually have really good ideas let's just see what happens?

Itamar Gilad (00:44:41):
So there's always like a trade-off between speed of delivery and speed of discovery, and that actually leads to the next layer of how do we combine the two? Because people tend to think it's an either/or. Either we are building very fast or we are learning and then we're building very slow, but I think we're using the wrong metric. The metric is not how fast can we get the bits into production, when there's a lot of uncertainty and we all face uncertainty and startup especially. It's not about getting the bits to production, it's about getting the right bits to production. It's about creating the outcomes that you need, the impact, and so it's about time to outcomes and I would argue that the evidence guided method is far more impactful. It's far faster, it's far more resource efficient than the opinion-based method. Because opinion-based methods tend to waste a lot more of your resources, building the wrong things or discovering, learning too late. Well, evidence guided helps you learn earlier.

(00:45:50):
Plus it is a fallacy that if you learn you don't build, good teams know how to do both at the same time and that's actually what the steps layer is meant to teach you or to help you do.

Lenny (00:46:03):
Awesome. So maybe just to close off that loop, say someone listening is at a bigger company, say Netflix versus a series A, series B or startup. Is there something you'd recommend about them approaching this differently? Any kind of guidance there of just how to take what you're sharing differently if you're a different source of companies like that?

Itamar Gilad (00:46:23):
Absolutely. I think the concept we talked about of the North Star metric, the value created versus the value captured is very important in every company. Building your entire metrics trees, maybe overkill, doing heavy weighted OKRs may be overkill for early stage. Early stage companies even don't know how they create value, so they need to iterate and their goals is really to find product market fit. Beyond that, what happens is that you need to start building your business model. So that's your goal and you iterate towards that and you need to put metrics on that and then when you move into scale, you need to try to create order because when you scale up... And all of this is covered in the book, there's a special chapter just about these questions. When you scale up, you get a lot of people and a lot of money and everything is happening at the same time. So there you need a order of evaluating ideas in a very systematic way. In a company like Netflix, by the way I don't know if they need this specific method. They're very-

Lenny (00:47:27):
Yeah, maybe that was a bad example. They're probably doing things pretty well.

Itamar Gilad (00:47:30):
One thing I discovered by the way, there's two types of companies that really benefit from this technique. One is those companies that are kind of emerging into modern product development. They have product teams, they have product managers, they have OKRs, they're starting to do Agile. But they're starting to do experimentation, but they're struggling to put it all together. Every CPO is building their own little framework and the other type is those companies that used to be evidence guided and they regressed and that happens way too often. Change of management, change of culture, and then all of a sudden they need to rediscover, to rekindle that spirit that was lost along Google+. So some of the people that actually respond to the strongest are actually surprisingly in these companies.

Lenny (00:48:19):
What I love about your frameworks and kind of all these things we're talking about is these are just a... You can almost think of them as a grab bag set of tools to make you more evidence guided as a company. You could start with thinking about the confidence meter, you could start using ICE more. You could start using the metrics tree and all these things just push you closer and closer to being more evidence guided, you don't have to adopt this whole thing all at once.

Itamar Gilad (00:48:41):
Absolutely. I would recommend that you don't try because if the transformation is way too big, you will get fatigued and you will just create a lot of process for a lot of people and you would not see the results and after a quarter you'll give up. So exactly what you suggested is the right approach.

Lenny (00:48:57):
What would be the first thing you'd suggest if people were trying to move closer to being less opinion oriented and more evidence-based? Which of these frameworks or models would you recommend first?

Itamar Gilad (00:49:06):
I recommend that they discuss internally where is the biggest problem that they're facing. If the goals are unclear, there's misalignment, we keep chasing the wrong things, start at the goals layer. Try to establish your North Star metric, your top business metric, your metrics trees, start assigning teams with their own area of responsibility. If you're spending a lot of time in debates and you're constantly fighting and changing your mind. Start with the ideas there and establish impact is confidence or whatever prioritization model you like, but involve evidence in it. I think the confidence meter is a good tool to use irrespective. If you're building too much and you're not learning enough, start adopting the steps layer which we haven't seen yet and if your team is very disengaged. You have one of these teams where the developers are very into Agile, very into quality, very into launching things, start working on the tasks there.

Lenny (00:50:10):
Awesome. Okay, let's keep going.

Itamar Gilad (00:50:13):
All right, so steps. Steps are about kind of helping us learn and build at the same time as we said and one of the patterns I see is that organizations don't know that they can actually learn at a much lower cost. They believe they need to build this elaborate MVP which is not minimal in any way and then launch it and then they will discover it and basically it's what we used to call beta 20 years ago but just with a different name. What I'm trying to do here in the steps layer is to help companies realize there's a gamut of ways to validate your ideas or more specifically to validate the assumptions in your idea and I created a little model for this, it's called after assessment fact finding, tests, experiments and release results. But again, it's just putting together things that much smarter people invented. So in assessment you have very easy things, things that don't require a lot of work. You check if it aligns with the goals, this idea that you have in your hand.

(00:51:14):
You do maybe some business modeling, you do ICE analysis, you do Assumption Mapping which is great tool by, David J. Blend, or you talk to your stakeholders one-on-one just to see if there are any risks, etc. These are usually not expensive things and they can teach you an awful lot about the impact and the ease of your idea. The next step is to dig data and usually that goes hand in hand with this. So you can find data in your data analysis through surveys, through competitive analysis, through user interviews and through field research, observing your users. Obviously these last two are pretty expensive, so it's often good not to wait until you have the idea and then start doing your research. It's best to keep doing your research ongoing and then you have some sort of data to lie on and to compare your idea against. But until now we didn't build anything, now you're ready to start testing, building versions of the product and putting them in front of users and measuring the results. But initially you don't build anything, you fake it.

(00:52:18):
You do a fake door test, you do a smoke test, Wizard of Oz test, a concierge test, usability test. We used a lot of those in the tabbed inbox by the way, one of the first early versions was actually we showed the tabbed inbox working to people. But it wasn't really Gmail, it was just a facade of HTML and behind the scenes and according to the permissions that the users gave us. Some of us moved just the subject and the sender into the right place. So initially the interviewer distracted them and then showed them their inbox and in it the top 50 messages were sorted to the right place, more or less if we got it right and people were like, "Wow, this is actually very cool." And that gave us a lot of evidence.

Lenny (00:53:02):
That's an awesome story. So that was in the user research, it wasn't rolled out to people? It was a manual individual?

Itamar Gilad (00:53:08):
There wasn't a single line of code written, this was just cooked up by the researchers and our designers. But it gave us some evidence to go and say, we should try and build this thing.

Lenny (00:53:19):
Love that.

Itamar Gilad (00:53:21):
So initially you fake it, mid-level tests are about building a rough version of it, it's not complete, it's not polished, it's not scalable, but it's good enough to give to users to start using. So those are early adopter programs, alphas, longitudinal user studies and fish food. Fish food is testing on your own team.

Lenny (00:53:40):
Fish food? I haven't heard that term before. So it's dog fooding, but more local to your team.

Itamar Gilad (00:53:46):
I think it's a Googly thing, but some people told me that they use fish food as well in their company the name. So I'm using it, I don't know if there's a better name for it.

Lenny (00:53:54):
I wonder why it's called fish food, because it's like little? It's like little gentle little clicks?

Itamar Gilad (00:53:58):
It could be. Yeah, I don't know.

Lenny (00:54:00):
Wow. Okay, super cool. I'm learning a lot here.

Itamar Gilad (00:54:03):
So the next stage is to actually build a kind of more complete version of this and then you can dog food it, then you can give this to your users internally. When I joined Microsoft many years ago, the first thing I noticed was that Outlook was very buggy and I asked people what's going on? And they told me we are all dog fooding the next version of Outlook that hasn't come out yet and that's a very common practice in Silicon Valley. You can do previews, you can do betas, you can do labs, so those are tests. Now, there's a special class of tests which are experiments because they have a control element. So AB tests, multivariate tests, those are all experiments. I'm using the word experiment the way data scientists use it, although people tend to call experiments to everything that you see here and finally, even the release you can do stage release, you can do percent launches, you can do hold backs. All of these things help you further validate your assumptions. Sometimes you need to roll back and change things, but it's another opportunity to learn.

(00:55:06):
So the key point is you don't have to start at the right-hand side, which is expensive. You can start early on and that leads to poking a lot of ideas very quickly. You realize they're not as good as you thought, and then you can invest more effort into the good ideas. If they generate positive evidence, you can go further and further until that point where you feel you're ready for delivery.

Lenny (00:55:29):
Okay. So we've talked about goals, we've talked about ideas, we're talking about steps here. Is there anything else along steps? And then next I know comes tasks.

Itamar Gilad (00:55:37):
No, this is it for steps. There's a lot more with this, we will not go into all of it.

Lenny (00:55:42):
Okay, that sounds good. Let's talk about tasks and what you mean there.

Itamar Gilad (00:55:46):
All right, awesome. So in many organizations there's these two worlds. There's the planning world where basically you have the managers, the stakeholders, some of the PMs really sit and think about what we need to launch and that's where we create the strategies and the roadmaps and the projects. But guess who is not invited to the party? The people who are actually doing the work. They live in Agile world, they're very focused on moving tickets to the done state, on completing burning story points, pushing stuff into production and there's a big gap between these two worlds. They don't understand each other, they don't see eye to eye, there's a lot of mistrust being built sometimes against the plans or the managers feels that the teams are just not being very effective. We've seen all of this and the solution, the stop gap is to put a PM in the middle. The PM is supposed to make all of this work, deliver on the roadmap like a project manager, feed the Agile machine with perfectly prioritized product backlogs and stories and it just doesn't work honestly.

(00:56:50):
And the PMs I meet are very tired and they have to spend so much time in planifications and roadmap discussions and they're very busy, they don't have time to do research or to test ideas. So I suggest changing this and bringing the developers a little bit out of their Agile cage if you like and no disrespect to Agile, it's a great thing but let's let them do more than just develop. Let's let them discover as well and one of the tools I suggest and again this is a process is what I call the GIST board. So it's basically the top three layers of GIST. The goals are on the right, these are just the key results usually per team I suggest not more than four. So you create a GIST board per team, then the ideas we're working on right now sometimes with our ICE scores and then the next few steps that we might want to pursue in order to validate these ideas and this is a very dynamic thing.

(00:57:48):
It changes all the time, the team leads need to update it and the team needs to meet around it at least once every other week to think to talk about what's going on. Are we still following the right ideas? How are we doing on the goals? What are the next steps? What's blocking us from completing the most important steps? And this is a discussion that is not happening today, because most of the discussion happens at the roadmap level and then there's a lot of discussion at the task level. But this middle layer of what actually are we trying to achieve and how well are we doing on it doesn't exist. If you do have this, you create a lot more context in the minds of your team and then they need to ask you fewer questions. You need to tell them less what to do. They know what's success and they are able to actually do a lot more on their own.

Lenny (00:58:37):
Is the way to think about the GIST board as the way you should be road roadmapping or is this more of a strategy framework to think about why you should be prioritizing broadly?

Itamar Gilad (00:58:48):
The way I say this is at the beginning of the quarter, the team defines its goals. The leads of the team define the goals, but they review it with the team, they review it with the managers, of course with the stakeholders. Everyone's in agreement, these are the maximum four key results and the one or two objectives you guys need to work on, teams cannot deliver on more than that. You copy these key results into the GIST board, then you start looking at your idea bank or you start generating ideas and say, how can we achieve these key results?

Lenny (00:59:18):
And to clarify the thing you copy is the key result as the goal?

Itamar Gilad (00:59:22):
Yes, exactly. You can write the objectives alongside that to remind people what are we trying to achieve, but the key results are the thing we show here. Then you pick some ideas, the ones that look most promising and as unintuitive as it sounds or counterintuitive as this sounds I would recommend that you let the team pick these ideas. The manager of the stakeholders can propose the ideas, everyone can propose, but the team should use the ICE process to kind of... And especially the product manager is very important here to choose which ideas to test first. Then the team together needs to develop which steps should we run, how can we validate this? Some of the steps will be done by the PM, some by the data analyst, some by the user researcher. But some will involve the team, there'll be some coding, there'll be some running of experiments and so there's some ownership around the steps. A sub team owns each one of these steps and we will change the board very actively.

(01:00:24):
So if an idea turns out to be bad we will take it off the board and put another idea in this place or maybe we achieve the goal, we don't need to work on this anymore, we can focus something else. So it's a project management tool in a sense.

Lenny (01:00:36):
Awesome. So I'm looking at it and I think maybe the most important piece of this is that steps aren't just like a project, like launch a better onboarding or add the step to onboarding. It's you want to emphasize the steps that you're going to take to get to more and more confidence essentially, and more and more evidence guided thinking versus just, "Well, let's figure out how to launch this feature idea."

Itamar Gilad (01:01:03):
Exactly. It's not a engineering milestone or a design milestone, it's a learning milestone. So we build something and along the way we actually grow the scope of what we build. We are building the product in the process and we learn, so the two have to come hand in hand.

Lenny (01:01:20):
And for folks that aren't watching this on YouTube, just to walk through an example, we'll do it real quick. So one of your goals here is average onboarding time, you want your goal to be the average onboarding time less than two days, currently five and a half days. An idea there is an onboarding wizard, and then the steps are a usability test with mockups and then a usability test as a prototype and then an AB test?

Itamar Gilad (01:01:42):
Yeah, basically, and you can alter this as you go along. Sometimes you can run multiple steps in parallel it's not always sequential. But that's basically the process, yeah.

Lenny (01:01:53):
Awesome. So again, what you're trying to emphasize here as a team is just we're not just going to launch this onboarding wizard and we're not going to figure it out later. It's like let's be upfront about the steps we're going to take to build more and more confidence. This is something we should keep investing more and more in, which is really interesting.

Itamar Gilad (01:02:09):
Yeah, and another interesting thing that happens every time you run a step if it's successful you have evidence and you can go back to the managers and tell them and share and say, "With this idea we thought it was great, but we got this result. What do you think that means?" And sometimes that manager that propose it would say, "I think the test failed, let's rerun it." Or sometimes they will say, "Maybe it's not as strong as I thought. The discussion just becomes that much more nuanced and objective if you like.

Lenny (01:02:42):
Maybe just to close out this framework. How does this relate to a roadmap that they may have in a spreadsheet or in Jira or in Asana or something like that. Does this sit on top of that? Is this replacing a roadmap somewhere else?

Itamar Gilad (01:02:54):
I would say that release roadmaps where you are just saying by Q3 we want to launch this or by October we have to launch that, they're kind of competing with this. If you're doing that and people know that the goal is to launch that thing by October, forget about learning, forget about evidence guided, I recommend using outcome roadmaps saying by October we want to achieve this outcome. By Q4 we want to launch in another three countries, or we want to grow our usage in India by that much, by this time we need to tackle the problem of churn and how we achieve this. Sometimes we know we have a concrete idea that is high confidence that we already tested, we switch into delivery, then we can put it on the roadmap and say, "Yeah, we're going to build this thing and we'll aim for October." But otherwise you want to keep it open and the roadmaps can kind of suffocate this process if you decide upfront with low confidence that this particular idea must be launched.

Lenny (01:04:04):
Okay. So you're proposing people switch the roadmapping practice to this, which is very ambitious. I love it.

Itamar Gilad (01:04:10):
Well, this is not a roadmap. This is just a tool for the team to manage the project, but I have a proposal for outcome roadmaps inside the book.

Lenny (01:04:20):
Okay, awesome. Okay. So I was going to ask if people wanted to try this approach, the book is the best way to fully understand the framework and how implement it.

Itamar Gilad (01:04:30):
That's one way. I have articles, I have resources on my site, but I try to condense much of what we just discussed in a lot more nuance in the book. So if you are interested in that, I would give it a go.

Lenny (01:04:45):
Awesome. Maybe just on the topic of OKRs real quick. How do OKRs connect to all this? It sounds like broadly you kind of assume people will keep working on here's our metric or key results or objectives and then that plugs into this kind of GIST framework.

Itamar Gilad (01:05:01):
So the metrics trees, plus your mission, plus the individual missions of the teams give you most of what you need to populate your OKRs. There's of course a process of alignment, top down, bottom up, side to side, which I talk a little bit about as well. OKRs is a very rich topic, but those things are usually the core. There's usually some other OKRs that's about the health of the company, the health of the product, etc. Those are called supplementary OKRs, I talk about those as well. So yeah, I think OKRs are a helpful tool if you like them.

Lenny (01:05:37):
And just zooming out again. Basically you don't need to take all of these ideas and lump them all together and change the way you work as a business. You can start with picking some of these ideas and starting to become more and more evidence guided. It sounds like this GIST board isn't where you probably want to start, but maybe it's once you have more and more experience using some of these tools or you tell me. Do you sometimes go straight to this way of thinking about the roadmap and the plan?

Itamar Gilad (01:06:04):
So it might not be the full board because you're missing some of the pieces, maybe your goals are not as good or your idea prioritization isn't as good. But if your team is very, very delivery focused and sometimes it's also the opposite. The managers are telling them how to build and you want to break this kind of dynamic, you want to create a step backlog. So instead of a product backlog, let's create a backlog of steps which are just validation steps, betas and previews, etc, and that changes the dynamic pretty strongly.

Lenny (01:06:39):
So by the time this podcast comes out, the book will be out. What is the best place to find the book?

Itamar Gilad (01:06:44):
Hopefully on Amazon, you can search for it. You can go to my site, itamargilad.com and it'll be presented prominently there and there's also the book landings page where you'll find everything you need to know about the book, evidenceguided.com.

Lenny (01:06:59):
Well, with that we've reached our very exciting lightning round. Are you ready?

Itamar Gilad (01:07:03):
Yes, let's go.

Lenny (01:07:04):
What are two or three books you've recommended most to other people?

Itamar Gilad (01:07:07):
So I'm going to cheat, I'm going to recommend a series of books so two series. One is the-

Lenny (01:07:12):
Cheating is allowed.

Itamar Gilad (01:07:13):
All right, cool. One, and those are obvious one. One is the series published by SVPG, Silicon Valley Product Group. So INSPIRED, EMPOWERED, now I think TRANSFORMED has come out, I haven't read it yet but I'm sure it's amazing. So this is Marty Cagan and his colleagues, they write some tremendous books and every product manager should read them. The other series, a bit older, this is the Lean series, The Lean Startup, Lean Enterprise, Lean Analytics, there's gold in all these books, Lean UX, really, really important books and I think they're not as appreciated as they should. Running Lean, that's another example.

Lenny (01:07:54):
What is a favorite recent movie or TV show?

Itamar Gilad (01:07:57):
I'm not really a big TV or movie buff, I just put on whatever comes up. I'm discovering that YouTube is actually becoming one of my sources of information entertainment. I'm learning a lot of Spanish recently, so I discovered this channel called Dreaming Spanish which is if you're learning Spanish it's incredible. So that's my recommendation.

Lenny (01:08:19):
That's a unique choice, I love it. Favorite interview question you like to ask candidates.

Itamar Gilad (01:08:24):
I like to ask them to design something for a niche audience. So a navigation system for elderly people or some sort of laptop for people with vision impairment, etc. So those are good questions to see their customer empathy, their creativity, their ability to evaluate multiple ideas, their ability to find flaws in their own ideas. So there's a lot of room to dig in there and kind of see how this person is thinking as a product person.

Lenny (01:08:57):
What is a favorite product you recently discovered that you love?

Itamar Gilad (01:09:00):
It's a cliche, but it's AI. There's a company called ElevenLabs, that do voices and the best voices, synthetic voices you heard, but they can also replicate your own voice so you can create a voice signature. If you're American you can use their kind of default free version or cheap version to replicate your own voice and that could be pretty useful if you need to narrate an audiobook or do some online course. So I'm finding this service very interesting.

Lenny (01:09:36):
This is all part of my big retirement plan, find all of these components together that can replace me eventually. You got AI generating content, we'll have this voice thing. I love it, it's all happening.

Itamar Gilad (01:09:45):
There's an AI version of you, right? I can ask you questions now with-

Lenny (01:09:48):
Oh, there is lennybot.com.

Itamar Gilad (01:09:50):
Right.

Lenny (01:09:51):
It's all part of the plan. Okay. What is a favorite life motto that you repeat most to yourself that you share with others?

Itamar Gilad (01:09:59):
That's a big one. Albert Einstein I think said, "Strive not to be a success, but to be of value." And I think that's a great motto for people and for companies. It's something that kind of guides me and this whole concept of the value exchange, etc, is kind of loosely connected to that.

Lenny (01:10:19):
I love that, that's such a important point for people putting out content online. So many people are just like, I just want to be successful, get followers, here's all these things I'm tweeting and showing and the thing that actually works is deliver value, create valuable stuff that people really value and want. I find the signal for that is, do you find it interesting and valuable? If you're like, "Oh wow, that's really interesting." Oftentimes other people are going to find it interesting. So I love that, great choice, I'm going to look at that one up. Two more questions. What's the most valuable lesson you learned from your mom or your dad?

Itamar Gilad (01:10:53):
I think both of them in their own way, they had relatively modest jobs, teaching or doing other things, but they always strived again to be the best they can and to deliver the most value they can. So it's very connected somehow, maybe I'm seeing the world through this lens. But they kind of taught me to strive to be the best I can at what I do.

Lenny (01:11:19):
The final question, you're Israeli for folks that can't tell. What is your favorite Israeli food that people should definitely check out or I try to get whenever they can?

Itamar Gilad (01:11:29):
When I arrive in Israel I usually go for shawarma, which is like döner kebab if you know it, it's just better. So if you're in Israel, if you go visit Haifa, which is the city where I grew up definitely check out the shawarma.

Lenny (01:11:44):
Awesome. Itamar, I hope people got the gist of your book from our conversation. What's the best way to find it? What's the best way to learn about you and reach out if they want to ask any questions? And then also, how can listeners be useful to you?

Itamar Gilad (01:11:56):
To find it you can go to itamargilad.com or to evidenceguided.com, and you'll find a book and you'll find me. Best value to me, try it out, just take some of these ideas, bring them back to your office, talk with your colleagues, say what do you think we should do about this? Just give it a go and reach back to me, tell me I'm easy to find in my website. Tell me what happened I'm really interested.

Lenny (01:12:22):
Amazing. Itamar, thank you again so much for being here.

Itamar Gilad (01:12:25):
Thank you.

Lenny (01:12:26):
Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

