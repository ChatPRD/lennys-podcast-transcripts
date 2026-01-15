---
guest: Ronny Kohavi
title: The ultimate guide to A/B testing | Ronny Kohavi (Airbnb, Microsoft, Amazon)
youtube_url: https://www.youtube.com/watch?v=hEzpiDuYFoE
video_id: hEzpiDuYFoE
description: 'Ronny Kohavi, PhD, is a consultant, teacher, and leading expert on the
  art and science of A/B testing. Previously, Ronny was Vice President and Technical
  Fellow at Airbnb, Technical Fellow...

  '
duration_seconds: 4988.0
duration: '1:23:08'
view_count: 69278
channel: Lenny's Podcast
keywords:
- growth
- retention
- acquisition
- activation
- onboarding
- churn
- metrics
- roadmap
- iteration
- a/b testing
- experimentation
- data-driven
- analytics
- funnel
- conversion
---

# The ultimate guide to A/B testing | Ronny Kohavi (Airbnb, Microsoft, Amazon)

## Transcript

Ronny Kohavi (00:00:00):
I'm very clear that I'm a big fan of test everything, which is any code change that you make, any feature that you introduce has to be in some experiment. Because again, I've observed this sort of surprising result that even small bug fixes, even small changes can sometimes have surprising, unexpected impact.

Ronny Kohavi (00:00:22):
And so I don't think it's possible to experiment too much. You have to allocate sometimes to these high risk, high reward ideas. We're going to try something that's most likely to fail. But if it does win, it's going to be a home run.

Ronny Kohavi (00:00:38):
And you have to be ready to understand and agree that most will fail. And it's amazing how many times I've seen people come up with new designs or a radical new idea. And they believe in it, and that's okay. I'm just cautioning them all the time to say, "If you go for something big, try it out, but be ready to fail 80% of the time."

Lenny (00:01:05):
Welcome to Lenny's Podcast, where I interview world-class product leaders and growth experts to learn from their hard win experiences building and growing today's most successful products.

Lenny (00:01:14):
Today my guest is Ronny Kohavi. Ronny is seen by many as the world expert on A/B testing and experimentation. Most recently, he was VP and technical fellow of relevance at Airbnb where he led their search experience team. Prior to that, he was corporate vice president at Microsoft, where he led Microsoft Experimentation Platform team. Before that, he was director of data mining and personalization at Amazon.

Lenny (00:01:38):
He's currently a full-time advisor and instructor. He's also the author of the go-to book on experimentation called Trustworthy Online Controlled Experiments. And in our show notes, you'll find a code to get a discount on taking his live cohort-based course on Maven.

Lenny (00:01:53):
In our conversation, we get super tactical about A/B testing. Ronny shares his advice for when you should start considering running experiments at your company, how to change your company's culture to be more experiment driven, what are signs your experiments are potentially invalid, why trust is the most important element of a successful experiment, culture, and platform. How to get started if you want to start running experiments at your company. He also explains what actually is a P value and something called Twyman's law, plus some hot takes about Airbnb and experiments in general. This episode is for anyone who's interested in either creating an experiment driven culture at their company or just fine-tuning one that already exists. Enjoy this episode with Ronny Kohavi after a short word from our sponsors.

Lenny (00:02:39):
This episode is brought to you by Mixpanel. Get deep insights into what your users are doing at every stage of the funnel, at a fair price that scales at you grow. Mixpanel gives you quick answers about your users from awareness, to acquisition, through retention. And by capturing website activity, ad data, and multi-touch attribution right in Mixpanel, you can improve every aspect of the full user funnel. Powered by first party behavioral data instead of third party cookies, Mixpanel is built to be more powerful and easier to use than Google Analytics. Explore plans for teams of every size and see what Mixpanel can do for you at mixpanel.com/friends/lenny. And while you're at it, they're also hiring. So check it out at mixpanel.com/friends/lenny.

Lenny (00:03:27):
This episode is brought to you by Round. Round is the private network built by tech leaders for tech leaders. Round combines the best of coaching, learning, and authentic relationships to help you identify where you want to go and accelerate your path to get there, which is why their wait list tops thousands of tech execs. Round is on a mission to shape the future of technology and its impact on society. Leading in tech is uniquely challenging, and doing it well is easiest when surrounded by leaders who understand your day-to-day experiences. When we're meeting and building relationships with the right people, we're more likely to learn, find new opportunities, be dynamic in our thinking, and achieve our goals. Building and managing your network doesn't have to feel like networking. Join Round to surround yourself with leaders from tech's most innovative companies. Build relationships, be inspired, take action. Visit round.tech/apply and use promo code Lenny to skip the wait list. That's round.tech/apply.

Lenny (00:04:30):
Ronny, welcome to the podcast.

Ronny Kohavi (00:04:33):
Thank you for having me.

Lenny (00:04:34):
So you're known by many as maybe the leading expert on A/B testing and experimentation, which I think is something every product company eventually ends up trying to do, often badly. And so I'm excited to dig quite deep into the world of experimentation and A/B testing to help people run better experiments. So thank you again for being here.

Ronny Kohavi (00:04:54):
That's a great goal. Thank you.

Lenny (00:04:56):
Let me start with kind of a fun question. What is maybe the most unexpected A/B tests you've run or maybe the most surprising result from an A/B test that you've run?

Ronny Kohavi (00:05:06):
So I think the opening example that I use in my book and in my class is the most surprising public example we can talk about. And this was kind of an interesting experiment. Somebody proposed to change the way that ads were displayed on Bing, the search engine. And he basically said, "Let's take the second line and move it, promote it to the first line so that the title line becomes larger."

Ronny Kohavi (00:05:37):
And when you think about that, and if you're going to look in my book, or in the class, there's an actual diagram of what happened, the screenshots. But if you think about it, just realistically it looks like a meh idea. Why would this be such a reasonable, interesting thing to do? And indeed, when we went back to the backlog, it was on the backlog for months, and languished there, and many things were rated higher.

Ronny Kohavi (00:06:05):
But the point about this is it's trivial to implement. So if you think about return on investment, we could get the data by having some engineers spend a couple of hours implementing it.

Ronny Kohavi (00:06:19):
And that's exactly what happened. Somebody at Bing who kept seeing this in the backlog and said, "My God, we're spending too much time discussing it. I could just implement it." He did. He spent a couple of days implementing it, as is the common thing at Bing, he launched the experiment.

Ronny Kohavi (00:06:37):
And a funny thing happened. We had an alarm. Big escalation, something is wrong with the revenue metric. Now this alarm fired several times in the past when there were real mistakes, where somebody would log revenue twice, or there's some data problem. But in this case, there was no bug. That simple idea increased revenue by about 12%.

Ronny Kohavi (00:07:01):
And this is something that just doesn't happen. We can talk later about Wyman's law, but that was the first reaction, which is, "This is too good to be true. Let's find a bug." And we did. And we looked for several times, and we replicated the experiment several times, and there was nothing wrong with it. This thing was worth $100 million at the time when Bing was a lot smaller.

Ronny Kohavi (00:07:22):
And the key thing is it didn't hurt the user metrics. So it's very easy to increase revenue by doing theatrics. Displaying more ads is a trivial way to raise revenue, but it hurts the user experience. And we've done the experiments to show that. In this case, this was just a home run that improved revenue, didn't significantly hurt the guardrail metrics. And so we were in awe of what a trivial change. That was the biggest revenue impact to Bing in all its history.

Lenny (00:07:57):
And that was basically shifting in two lines, right? Switching two lines in the search results.

Ronny Kohavi (00:08:02):
And this was just moving the second line to the first line. Now you then go and run a lot of experiments to understand what happened here. Is it the fact that the title line has a bigger font, sometimes different color? So we ran a whole bunch of experiments.

Ronny Kohavi (00:08:16):
And this is what usually happens. We have a breakthrough. You start to understand more about, what can we do? And there suddenly a shift towards, "Okay, what are other things we could do that would allow us to improve revenue?" We came up with a lot of follow on ideas that helped a lot.

Ronny Kohavi (00:08:34):
But to me, this was an example of a tiny change that was the best revenue generating idea in Bing's history, and we didn't rate it properly. Nobody gave this the priority that in hindsight, it deserves. And that's something that happens often. I mean, we are often humbled by how bad we are at predicting the outcome of experiments.

Lenny (00:09:01):
This reminds me of a classic experiment at Airbnb while I was there, and we'll talk about Airbnb in a bit. The search team just ran a small experiment of what if we were to open a new tab every time someone clicked on a search result, instead of just going straight to that listing. And that was one of the biggest wins in search-

Ronny Kohavi (00:09:18):
And by the way, I don't know if you know the history of this, but I tell about this in class. We did this experiment way back around 2008 I think. And so this predates Airbnb. I remember it was heavily debated. Why would you open something in a new tab? The users didn't ask for it. It was a lot of pushback from the designers. And we ran that experiment. And again, it was one of these highly surprising results that made it that we learned so much from it.

Ronny Kohavi (00:09:49):
So we first did this. It was done in the UK for opening Hotmail, and then we moved it to MSN, so it would open search in new tab, and all the set of experiments were highly, highly beneficial. We published this. And I have to tell you, when I came to Airbnb, I talked to our joint friend Ricardo about this. And it was sort of done, it was very beneficial, and then it was semi forgotten, which is one of the things you learned about institutional memories. When you have winners, make sure to address them and remember them. So it was at Airbnb done for a long time before I joined that listings opened in a new tab, but other things that were designed in the future were not done. And I reintroduced this to the team, and we saw big improvements.

Lenny (00:10:35):
Shout out to Ricardo, our mutual friend who helped make this conversation happen. There's this holy grail of experiments that I think people are always looking for of one hour of work and it creates this massive result. I imagine this is very rare, and don't expect this to happen. I guess in your experience, how often do you find one of these gold nuggets just lying around?

Ronny Kohavi (00:10:57):
Yeah. So again, this is a topic that's near and dear to my heart. Everybody wants these amazing results, and I show them in chapter one in my book, multiple of these small efforts, huge gain.

Ronny Kohavi (00:11:13):
But as you said, they're very rare. I think most of the time, the winnings are made this inch by inch. And there's a graph that I show in my book, a real graph of how Bing ads has managed to improve the revenue per a thousand searches over time, and every month you can see a small improvement and a small improvement. Sometimes the degradation because of legal reasons or other things. There were some concern that we were not marking the ads properly. So you have to suddenly do something that you know is going to hurt revenue. But yes, I think most results are inch by inch. You improve small amounts, lots of them. I think that the best example that I can say is a couple of them that I can speak about.

Ronny Kohavi (00:12:00):
One is at Bing, the relevance team, hundreds of people all working to improve bing relevance. They have a metric, we'll talk about OEC, the overall evaluation criterion. But they have a metric that their goal is to improve it by 2% every year. It's a small amount, and that 2% you can see here's a 0.1, and here's a 0.15, here's a 0.2, and then they add up to around 2% every year, which is amazing.

Ronny Kohavi (00:12:28):
Another example that I am allowed to speak about from Airbnb is the fact that we ran some 250 experiments in my tenure there in search relevance. And again, small improvements added up. So this became overall a 6% improvement to revenue. So when you think about 6%, it's a big number, but it came out not of one idea, but many, many smaller ideas that each gave you a small gain.

Ronny Kohavi (00:13:00):
And in fact, again, there's another number I'm allowed to say. Of these experiments, 92% failed to improve the metric that we were trying to move. So only 8% of our ideas actually were successful at moving the key metrics.

Lenny (00:13:17):
There's so many threads I want to follow here, but let me follow this one right here. You just mentioned of 92% of experiments failed. Is that typical in your experience seeing experiments running a lot of companies? What should people expect when they're running experiments? What percentage should they expect to fail?

Ronny Kohavi (00:13:31):
Well, first of all, I published three different numbers for my career. So overall at Microsoft, about 66%, two thirds of ideas fail. And don't think the 66 is accurate. It's about two thirds. At Bing, which is a much more optimized domain after we've been optimizing it for a while, the failure rate was around 85%. So it's harder to improve something that you've been optimizing for a while. And then at Airbnb, this 92% number is the highest failure rate that I've observed.

Ronny Kohavi (00:14:09):
Now I've quoted other sources. It's not that I worked at groups that were particularly bad, Booking, Google Ads, other companies published numbers that are around 80 to 90% failure rate of ideas. This is where it's important of experiments. It's important to realize that when you have a platform, it's easy to get this number. You look at how many experiments were run and how many of them launched. Not every experiment maps to an idea.

Ronny Kohavi (00:14:39):
So it's possible that when you have an idea, your first implementation, you start an experiment. Boom, it's egregiously bad, because you have a bug. In fact, 10% of experiments tend to be aborted on the first date. Those are usually not that the idea is bad, but that there is an implementation issue or something we haven't thought about, that forces an abort.

Ronny Kohavi (00:15:01):
You may iterate and pivot again. And ultimately, if you do two, or three, or four pivots or bug fixes, you may get to a successful launch. But those numbers of 80 to 92% failure rate are of experiments.

Ronny Kohavi (00:15:17):
Very humbling. I know that every group that starts to run experiments, they always start off by thinking that somehow, they're different. And their success rate's going to be much, much higher, and they're all humbled.

Lenny (00:15:29):
You mentioned that you had this pattern of clicking a link and opening a new tab as a thing that just worked at a lot of different places.

Ronny Kohavi (00:15:36):
Yeah.

Lenny (00:15:37):
Are there other versions of this? Do you do you collect a list of, "Here's things that often work when we want to move" there's some you could share. I don't know if you have a list in your head.

Ronny Kohavi (00:15:48):
I can give you two resources. One of them is a paper that we wrote called Rules of Thumb, and what we tried to do at that time at Microsoft was to just look at thousands of experiments that run and extract some patterns. And so that's one paper that we can then put in the notes.

Lenny (00:16:07):
Perfect.

Ronny Kohavi (00:16:08):
But there's another more accurate, I would say, resource that's useful that I recommend to people. And it's a site called goodui.org, and goodui.org is exactly the site that tries to do what you're saying at scale.

Ronny Kohavi (00:16:25):
So guy's name is Jacob [inaudible 00:16:28]. He asks people to send them results of experiments, and he puts them into patterns. There's probably 140 patterns I think at this point. And then for each pattern he says, "Well, who has that helped? How many times and by how much?" So you have an idea of this worked, three out of five times. And it was a huge win. In fact, you can find that open a new window in there.

Lenny (00:16:54):
I feel like you feed that into ChatGPT, and you have basically a product manager creating a roadmap tool.

Ronny Kohavi (00:17:01):
In general, by the way, a lot of that is institutional memory, which is can you document things well enough so that the organization remembers the successes and failures, and learns from them?

Ronny Kohavi (00:17:17):
I think one of the mistakes that some company makes is they launch a lot of experiments and never go back and summarize the learnings. So I've actually put a lot of effort in this idea of institutional learning, of doing the quarterly meeting of the most surprising experiments.

Ronny Kohavi (00:17:32):
By the way, surprising is another question that people often are not clear about. What is a surprising experiment? To me, a surprising experiment is one where the estimated result beforehand and the actual result differ by a lot. So that absolute value of the difference is large.

Ronny Kohavi (00:17:53):
Now you can expect something to be great and it's flat. Well, you learn something. But if you expect something to be small and it turns out to be great, like that ad title promotion, then you've learned a lot. Or conversely, if you expect that something will be small and it's very negative, you can learn a lot by understanding why this was so negative. And that's interesting.

Ronny Kohavi (00:18:17):
So we focused not just on the winners, but also surprising losers, things that people thought would be a no-brainer to run. And then for some reason, it was very negative. And sometimes, it's that negative that gives you insight. Actually, I'm just coming up with one example that of that, that I should mention.

Ronny Kohavi (00:18:36):
We were running this experiment at Microsoft to improve the windows indexer, and the team was able to show on offline tests that it does much better at indexing, and they showed some relevance is higher, and all these good things. And then they ran it as an experiment. You know what happened? Surprising result. Indexing the relevance was actually high, but it killed a battery life.

Ronny Kohavi (00:19:03):
So here's something that comes from left field that you didn't expect. It was consuming a lot more CPU on laptops. It was killing the laptops. And therefore, okay, we learned something. Let's document it. Let's remember this, so that we now take this other factor into account as we design the next iteration.

Lenny (00:19:23):
What advice do you have for people to actually remember these surprises? You said that a lot of it is institutional. What do you recommend people do so that they can actually remember this when people leave, say three years later?

Ronny Kohavi (00:19:34):
Document it. We had a large deck internally of these successes and failures, and we encourage people to look at them. The other thing that's very beneficial is just to have your whole history of experiments and do some ability to search by keywords.

Ronny Kohavi (00:19:52):
So I have an idea. Type a few keywords and see if from the thousands of experiments that ran... And by the way, these are very reasonable numbers. At Microsoft, just to let you know, when I left in 2019, we were on a rate of about 20 to 25,000 experiments every year. So every working, day we were starting something like 100 new treatments. Big numbers. So when you're running in a group like Bing, which is running thousands and thousands of experiments, you want to be able to ask, "Has anybody did an experiment on this or this or this?" And so that searching capability is in the platform.

Ronny Kohavi (00:20:32):
But more than that, I think just doing the quarterly meeting of the most successful... Most interesting, sorry, not just successful, most interesting experiments is very key. And that also helps the flywheel of experimentation.

Lenny (00:20:45):
It's a good segue to something I wanted to touch on, which is there's often, I guess a weariness of running too many experiments and being too data-driven, and the sense that experimentation just leads you to these micro optimizations, and you don't really innovate and do big things. What's your perspective on that? And then, can you be too experiment driven in your experience?

Ronny Kohavi (00:21:07):
I'm very clear that I'm a big fan of test everything, which is any code change that you make, any feature that you introduce has to be in some experiment. Because again, I've observed this surprising result that even small bug fixes, even small changes can sometimes have surprising unexpected impact.

Ronny Kohavi (00:21:30):
And so I don't think it's possible to experiment too much. I think it is possible to focus on incremental changes because some people say, "Well, if we only tested 17 things around this," you have to think about, it's like in stock. You need a portfolio. You need some experiments that are incremental that move you in the direction that you know you're going to be successful over time if you just try enough. But some experiments, you have to allocate sometimes to these high risk, high reward ideas. We're going to try something that's most likely to fail, but if it does win, it's going to be a home run.

Ronny Kohavi (00:22:14):
And so you have to allocate some efforts to that, and you have to be ready to understand and agree that most will fail. And I've amazing how many times I've seen people come up with new designs, or a radical new idea, and they believe in it, and that's okay. I'm just cautioning them all the time to say, "Hey, if you go for something big, try it out, but be ready to fail 80% of the time."

Ronny Kohavi (00:22:42):
And one true example, that again, I'm able to talk about because we put it in my book, is we were at Bing trying to change the landscape of search. And one of the ideas, the big ideas was we are going to integrate with social. So we hooked into the Twitter fire hose feed and we hooked into Facebook, and we spent 100 person years on this idea.

Ronny Kohavi (00:23:14):
And it failed. You don't see it anymore. It existed for about a year and a half, and all the experiments were just negative to flat. And it was an attempt. It was fair to try it. I think it took us a little long to fail, to decide that this is a failure. But at least we had the data. We had hundreds of experiments that we tried. None of them were a breakthrough. And I remember mailing Qi Lu with some statistics showing that it's time to abort, it's time to fail on this. And he decided to continue more. And it's a million dollar question. Do you continue, and then maybe the breakthrough will come next month, or do you abort? And a few months later, we aborted.

Lenny (00:24:07):
That reminds me of at Netflix, they tried a social component that also failed. At Airbnb, early on there was a big social attempt to make, "Here's your friends that have stayed at these Airbnbs," completely had no impact. So maybe that's one of these learnings that we should document.

Ronny Kohavi (00:24:21):
Yeah, this is hard. This is hard. But again, that's the value of experiments, which are this oracle that gives you the data. You may be excited about things. You may believe it's a good idea. But ultimately, the oracle is the controlled experiment. It tells you whether users are actually benefiting from it, whether you and the users, the company and the users.

Lenny (00:24:48):
There's obviously a bit of overhead and downside to running an experiment, setting all up, and analyzing the results. Is there anything that you ever don't think is worth A/B testing?

Ronny Kohavi (00:24:59):
First of all, there are some necessary ingredients to A/B testing. And I'll just say outright, not every domain is amenable to A/B testing. You can't A/B test mergers and acquisitions. It's something that happens once, you either acquire or you don't acquire.

Ronny Kohavi (00:25:14):
So you do have to have some necessary ingredient. You need to have enough units, mostly users, in order for the statistics to work out. So if you're too small, it may be too early to A/B test. But what I find is that in software, it is so easy to run A/B testing and it is so easy to build a platform.

Ronny Kohavi (00:25:39):
I don't say it's easy to build a platform. But once you build a platform, the incremental cost of running an experiment should approach zero. And we got to that at Microsoft, where after a while, the cost of running experiments was so low that nobody was questioning the idea that everything should be experimented with.

Ronny Kohavi (00:25:59):
Now, I don't think we were there at Airbnb for example. The platform at Airbnb was much less mature, and required a lot more analysts in order to interpret the results and to find issues with it. So I do think there's this trade off. You're willing to invest in the platform. It is possible to get the marginal cost to be close to zero. But when you're not there, it's still expensive, and there may be reasons why not to run A/B tests.

Lenny (00:26:28):
You talked about how you may be too small to run A/B tests, and this is a constant question for startups is, when should we start running A/B tests? Do you have kind of a heuristic or a rule of thumb of, here's a time you should really start thinking about running an A/B test?

Ronny Kohavi (00:26:42):
Yeah, a dollar question that everybody asks. So actually, we'll put this in the notes, but I gave a talk last year, what I called it is practical defaults. And one of the things I show there is that unless you have at least tens of thousands of users, the math, the statistics just don't work out for most of the metrics that you're interested in.

Ronny Kohavi (00:27:05):
In fact, I gave an actual practical number of a retail site with some conversion rate, trying to detect changes that are at least 5% beneficial, which is something that startups should focus on. They shouldn't focus on the 1%, they should focus on the 5 and 10%. Then you need something like 200,000 users.

Ronny Kohavi (00:27:25):
So start experimenting when you're in the tens of thousands of users. You'll only be able to detect large effects. And then once you get to 200,000 users, then the magic starts happening. Then you can start testing a lot more. Then you have the ability to test everything and make sure that you're not degrading and getting value out of experimentation. So you ask for rule of thumb, 200,000 users, you're magical. Below that, start building the culture, start building the platform, start integrating. So that as you scale, you start to see the value.

Lenny (00:28:00):
Love it. Coming back to this kind of concern people have of experimentation, keeps you from innovating and taking big bets, I know you have this framework overall evaluation criterion, and I think that helps with this. Can you talk a bit about that?

Ronny Kohavi (00:28:14):
The OEC or the overall evaluation criterion is something that I think many people that start to dabble in A/B testing miss. And the question is, what are you optimizing for? And it's a much harder question that people think because it's very easy to say we're going to optimize for money, revenue. But that's the wrong question, because you can do a lot of bad things that will improve revenue. So there has to be some countervailing metric that tells you, how do I improve revenue without hurting the user experience?

Ronny Kohavi (00:28:53):
So let's take a good example with search. You can put more ads on a page and you will make more money. There's no doubt about it. You will make more money in the short term. The question is, what happens to the user experience, and how is that going to impact you in the long term?

Ronny Kohavi (00:29:13):
So we've run those experiments, and we were able to map out this number of ads causes this much increase to churn, this number of ads causes this much increase to the time that users take to find a successful result. And we came up with an OEC that is based on all these metrics that allows you to say, "Okay, I'm willing to take this additional money if I'm not hurting the user experience by more than this much." So there's a trade-off there.

Ronny Kohavi (00:29:41):
One of the nice ways to phrase this, as a constraint optimization problem. I want you to increase revenue, but I'm going to give you a fixed amount of average real estate that you can use. So for one query, you can have zero ads. For another query, you can have three ads. For a third query, you can have wider, bigger ads. I'm just going to count the pixels that you take, the vertical pixels. And I will give you some budget. And if you can under the same budget make more money, you're good to go.

Ronny Kohavi (00:30:16):
So that to me turns the problem from a badly defined, let's just make more money. Any page can start plastering more ads and make more money short term, but that's not the goal. The goal is long-term growth and revenue. Then you need to insert these other criteria, and what am I doing to the user experience? One way around it is to put this constraint. Another one is just to have these other metrics. Again, something that we did, to look at the user experience. How long does it take the user to reach a successful click? What percentage of sessions are successful? These are key metrics that were part of the overall evaluation criteria, that we've used.

Ronny Kohavi (00:30:55):
I can give you another example by the way, from the hotel industry or Airbnb that we both worked at. You can say, "I want to improve conversion rate," but you can be smarter about it and say, "It's not just enough to convert a user to buy or to pay for a listing. I want them to be happy with it several months down the road when they actually stay there."

Ronny Kohavi (00:31:19):
So that could be part of your OEC to say, "What is the rating that they will give to that listing when they actually stay there?" And that causes an interesting problem, because you don't have this data now. You're going to have it three months from now when they actually stay. So you have to build the training set that allows you to make a prediction about whether this user, whether Lenny is going to be happy at this cheap place. Or whether no, I should offer him something more expensive, because Lenny likes to stay at nicer places where the water actually is hot and comes out of the faucet.

Lenny (00:31:52):
That is true. Okay, so it sounds like the core to this approach is basically have a drag metric that makes sure you're not hurting something that's really important to the business, and then being very clear on what's the long-term metric we care most about.

Ronny Kohavi (00:32:05):
To me, the key word is lifetime value, which is you have to define the OEC such that it is causally predictive of the lifetime value of the user. And that's what causes you to think about things properly, which is, am I doing something that just helps me short term, or am I doing something that will help me in the long term? Once you put that model of lifetime value, people say, "Okay, what about retention rates? We can measure that. What about the time to achieve a task? We can measure that." And those are these countervailing metrics that make the OEC useful.

Lenny (00:32:43):
And to understand these longer term metrics, what I'm hearing is use models, and forecast, and predictions, or would you suggest sometimes use a long-term holdout or some other approach? What do you find is the best way to see these long term?

Ronny Kohavi (00:32:57):
Yeah, so there's two ways that I like to think about it. One is you can run long-term experiments for the goal of learning something. So I mentioned that at Bing, we did run these experiments where we increased the ads and decreased the ads, so that we will understand what happens to key metrics.

Ronny Kohavi (00:33:16):
The other thing is you can just build models that use some of our background knowledge or use some data science to look at historical... I'll give you another good example of this. When I came to Amazon, one of the teams that reported to me was the email team that it was not the transactional emails when you buy something, you get an email. But it was the team that sent these recommendations. "Here's a book by an author that you bought. Here's a product that we recommend." And the question is, how do we give credit to that team?

Ronny Kohavi (00:33:49):
And the initial version was, whenever a user comes from the email and purchases something on Amazon, we're going to give that email credit. Well, it turned out this had no countervailing metric. The more emails you send, the more money you're going to credit the team. And so that led to spam. Literally a really interesting problem. The team just ramped up the number of emails that they were sending out, and claimed to make more money, and their fitness function improved.

Ronny Kohavi (00:34:20):
So then we backed up and then we said, "Okay, we can either phrase this as a constraint satisfaction problem. You're allowed to send user an email every X days or," which is what we ended up doing is, "Let's model the cost of spamming the users."

Ronny Kohavi (00:34:37):
What's that cost? Well, when they unsubscribe, we can't mail them. So we did some data science study on the side and we said, "What is the value that we're losing from an unsubscribe?" And we came up with a number, it was a few dollars. But the point was, now we have this countervailing metric. We say, "Here's the money that we generate from the emails. Here's the money that we're losing on long-term value. What's the trade-off?" And then when we started to incorporate those formula, more than half the campaigns that were being sent were negative.

Ronny Kohavi (00:35:14):
So it was a huge insight at Amazon about how to send the right campaigns. And this is what I like about these discoveries. This fact that we integrated the unsubscribe led us to a new feature to say, "Well, let's not lose their future lifetime value through email. When they unsubscribe, let's offer them by default to unsubscribe from this campaign."

Ronny Kohavi (00:35:41):
So when you get an email, there's a new book by the author. The default to unsubscribe would be unsubscribe me from author emails. And so now, the negative, the countervailing metric is much smaller. And so again, this was a breakthrough in our ability to send more emails, and understand based on what users were unsubscribing from, which ones are really beneficial.

Lenny (00:36:06):
I love the surprising results.

Ronny Kohavi (00:36:08):
We all love them. This is the humbling reality. And people talk about the fact that A/B testing sometimes leads you to incremental... I actually think that many of these small insights lead to fundamental insights about which areas to go, some strategies we should take, some things we should develop. Helps a lot.

Lenny (00:36:31):
This makes me think about how every time I've done a full redesign of a product, I don't think ever, has it ever been a positive result. And then the team always ends up having to claw back what they just hurt and try to figure out what they messed up. Is that your experience too?

Ronny Kohavi (00:36:47):
Absolutely, yeah. In fact, I've published some of these in LinkedIn posts showing a large set of big launches and redesigns that dramatically failed, and it happens very often. So the right way to do this is to say, "Yes, we want to do a redesign, but let's do it in steps and test on the way and adjust," so you don't need to take 17 new changes, that many of them are going to fail. Start to move incrementally in a direction that you believe is beneficial. Adjust on the way.

Lenny (00:37:24):
The worst part of those experiences I find is it took three to six months to build it. And by the time it's launched, it's just like, "We're not going to unlaunch this. Everyone's been working in this direction. All the new features are assuming this is going to work," and you're basically stuck.

Ronny Kohavi (00:37:41):
I mean, this is a sunk cost fallacy. We invested so many years in it. Let's launch this, even though it's bad for the user. No, that's terrible. Yeah. Yeah. So this is the other advantage of recognizing this humble reality that most ideas fail. If you believe in that statistics that I published, then doing 17 changes together is more likely to be negative. Do them in smaller increments, learn from, it's called OFAT one-factor-at-a-time. Do one factor, learn from it, and adjust. Of the 17, maybe you have four good ideas. Those are the ones that will launch and be positive.

Lenny (00:38:22):
I generally agree with that, and always try to avoid a big redesign, but it's hard to avoid them completely. There's often team members that are really passionate like, "We just need to rethink this whole experience. We're not going to incrementally get there." Have you found anything effective in helping people either see this perspective, or just making a larger bet more successful?

Ronny Kohavi (00:38:42):
By the way, I'm not opposed to large redesigns. I try to give the team the data to say, "Look, here are lots of examples where big redesigns fail." Try to decompose your redesign if you can't decompose it to one factor at a time, to a small set of factors at a time. And learn from these smaller changes what works and what doesn't.

Ronny Kohavi (00:39:08):
Now, it's also possible to do a complete redesign. Just, as you said yourself, be ready to fail. I mean, do you really want to work on something for six months or a year, and then run the A/B test, and realize that you've hurt revenues or other key metrics by several percentage points? And a data-driven organization will not allow you to launch. What are you going to write in your annual review?

Lenny (00:39:33):
But nobody ever thinks it's going to fail. They think, "No, we got this. We've talked to so many people."

Ronny Kohavi (00:39:38):
But I think organizations that start to run experiments are humbled early on from the smaller changes. Right? You're right. I'll tell you a funny story. When I came from Amazon to Microsoft, I joined the group, and for one reason or another, that group disbanded a month after I joined.

Ronny Kohavi (00:39:57):
And so people came to me and said, "Look, you just joined the company. You're at partner level. You figure out how you can help Microsoft." And I said, "I'm going to build an experimentation platform," because nobody at Microsoft is running experiments. And more than 50% of ideas in Amazon that we tried failed. And the classical response was, "We have better PMs here."

Ronny Kohavi (00:40:26):
Right? There was this complete denial that it's possible that 50% of ideas that Microsoft is implementing, in a three-year development cycle by the way. This is how long it took Office to release. It was a classical every three years we release.

Ronny Kohavi (00:40:42):
And the data came about showing that Bing was the first to truly implement experimentation at scale. And we shared with the rest of the companies the surprising results. And so when Office was... And this was credit to Qi Lu and Satya Nadella, they were ones that says, "Ronny, you try to get Office to run experiments. We'll give you the air support." And it was hard, but we did it. It took a while, but Office started to run experiments, and they realized that many of their ideas are failing.

Lenny (00:41:20):
You said that there's a site of a failed redesigns. Is that in your book or is that a site that you can point people to, to help build this case?

Ronny Kohavi (00:41:29):
I teach this in my class, but I think I've posted this on LinkedIn and answered some questions. I'm happy to put that in the notes.

Lenny (00:41:36):
Okay, cool. We'll put that in the show notes. Because I think that's the kind of data that often helps convince a team, "Maybe we shouldn't rethink this entire onboarding flow from scratch. Maybe we should iterate towards and learn as we go."

Lenny (00:41:48):
This episode is brought to you by Eppo. Eppo is a next generation A/B testing platform built by Airbnb alums for modern growth teams. Companies like DraftKings, Zapier, ClickUp, Twitch, and Cameo rely on Eppo to power their experiments.

Lenny (00:42:02):
Wherever you work, running experiments is increasingly essential, but there are no commercial tools that integrate with a modern growth team stack. This leads to wasted time building internal tools or trying to run your own experiments through a clunky marketing tool.

Lenny (00:42:15):
When I was at Airbnb, one of the things that I loved most about working there was our experimentation platform, where I was able to slice and dice data by device types, country, user stage.

Lenny (00:42:25):
Eppo does all that and more, delivering results quickly, avoiding annoying prolonged analytic cycles, and helping you easily get to the root cause of any issue you discover. Eppo lets you go beyond basic click through metrics, and instead use your North Star metrics like activation, retention, subscription and payments. Eppo supports tests on the front end, on the back end, email marketing, even machine learning clients. Check out Eppo at geteppo.com, that's geteppo.com, and 10X your experiment velocity.

Lenny (00:42:55):
Is it ever worth just going, "Let's just rethink this whole thing and just give it a shot," to break out of a local minima or local maxima essentially?

Ronny Kohavi (00:43:03):
Yeah. So I think what you said is fair. I do want to allocate some percentage of resources to big bets. As you said, we've been optimizing this thing to hell. Could we completely redesign it? It's a very valid idea. You may be able to break out of a local minima. What I'm telling you is 80% of the time, you will fail. So be ready for that. What people usually expect is, "My redesign is going to work." No, you're most likely going to fail, but if you do succeed, it's a breakthrough.

Lenny (00:43:35):
I like this 80% rule of thumb. Is that just a simple way of thinking about it? 80% of your-

Ronny Kohavi (00:43:39):
That's my rule of thumb. And I've heard people say it's 70% or 80%. But it's in that area where I think when you talk about how much to invest in the known versus the high risk, high reward, that's usually the right percentage that most organizations end up doing this allocation, right? You interviewed Shreyas. I think he mentioned that Google is like 70% the searching ads, and it's 20% for some of the apps and new stuff, and then it's the 10% for infrastructure.

Lenny (00:44:16):
And I think the most important point there is if you're not running an experiment, 70% of stuff you're shipping is hurting your business.

Ronny Kohavi (00:44:23):
Well, it's not hurting, it's flat too negative. Some of them are flat. And by the way, flat to me, if something is not Statsig, that's a no ship, because you've just introduced more code. There is a maintenance overhead to shipping your stuff. I've heard people say, "Look, we already spent all this time. The team will be demotivated if we don't ship it." And I'm, "No, that's wrong guys. Let's make sure that we understand that shipping this project has no value, is complicating the code base. Maintenance costs will go up." You don't ship on flat, unless it's a legal requirement. When legal comes along and says, "You have to do X or Y," you have to ship on flat or even negative. And that's understandable.

Ronny Kohavi (00:45:08):
But again, I think that's something that a lot of people make the mistake of saying, "Legal told us we have to do this, therefore we're going to take the hits." No, legal gave you a framework that you have to work under. Try three different things, and ship the one that hurts the least.

Lenny (00:45:25):
That reminds me when Airbnb launched the rebrand, even that they ran as an experiment with the entire homepage redesigned, the new logo, and all that. And I think there was a long-term holdout even, and I think it was positive in the end from what I remember.

Lenny (00:45:41):
Speaking of Airbnb, I want to chat about Airbnb briefly. I know you're limited in what you can share, but it's interesting that Airbnb seems to be moving in this other direction where it's becoming a lot more top-down, Brian vision oriented. And Brian's even talked about how he's less motivated to run experiments. He doesn't want to run as many experiments as they used to. Things are going well, and so it's hard to argue with the success potentially. You worked there for many years. You ran the search team essentially. I guess, what was your experience like there? And then roughly, what's your sense of how things are going, where it's going?

Ronny Kohavi (00:46:15):
Well as you know, I'm restricted from talking about Airbnb. I will say a few things that I am allowed to say. One is in my team in search relevance, everything was A/B tested. So while Brian can focus on some of the design aspects, the people who are actually doing the neural networks and the search, everything was A/B tested to hell. So nothing was launching without an A/B test. We had targets around improving certain metrics, and everything was done A/B test.

Ronny Kohavi (00:46:50):
Now other teams, some did, some did not. I will say that when you say things are going well, I think we don't know the counterfactual. I believe that had Airbnb kept people like Greg Greeley, which was pushing for a lot more data driven, and had Airbnb run more experiments, it would've been in a better state than today. But it's the counterfactual. We don't know.

Lenny (00:47:14):
That's a really interesting perspective. Airbnb's such an interesting natural experiment of a way of doing things differently. There's de-emphasizing experiments, and also, they turned off paid ads during Covid. And I don't know where it is now, but it feels like it's become a much smaller part of the growth strategy. Who knows if they've ramped it up to back to where it's today, but I think it's going to be a really interesting case study looking back five, 10 years from now.

Ronny Kohavi (00:47:38):
It's a one-off experiment where it's hard to assign value to some of the things that Airbnb is doing. I personally believe it could have been a lot bigger and a lot more successful if it had run more controlled experiments. But I can't speak about some of those that I ran and that showed that some of the things that were initially untested were actually negative and could be better.

Lenny (00:48:04):
All right. Mysterious. One more question. Airbnb, you were there during Covid, which was quite a wild time for Airbnb. We had Sanchan on the podcast talking about all the craziness that went on when travel basically stopped, and there was a sense that Airbnb was done, and travel's not going to happen for years and years. What's your take on experimentation in that world where you have to really move fast, make crazy decisions, and make big decisions? What was it like during that time?

Ronny Kohavi (00:48:34):
So I think actually in a state like that, it's even more important to run A/B tests, right? Because what you want to be able to see is if we're making this change, is it actually helping in the current environment? There's this idea of external generalizability. Is it going to work out now during Covid? Is it going to generalize later on? These are things that you can really answer with the controlled experiments, and sometimes it means that you might have to replicate them six months down when Covid say is not as impactful as it is.

Ronny Kohavi (00:49:11):
Saying that you have to make decisions quickly, to me, I'll point you to the success rate. If in peace time you're wrong two thirds to 80% of the time, why would you be subtly right in wartime, in Covid time?

Ronny Kohavi (00:49:26):
So I don't believe in the idea that because bookings went down materially, the company should suddenly not be data driven and do things differently. I think if Airbnb stayed the course, did nothing, the revenue would've gone up in the same way.

Lenny (00:49:49):
Fascinating.

Ronny Kohavi (00:49:49):
In fact, if you look at one investment, one big investment that was done at the time was online experiences, and the initial data wasn't very promising. And I think today, it's a footnote.

Lenny (00:50:01):
Yeah. Another case study for the history books, Airbnb experiences. I want to shift a little bit and talk about your book, which you mentioned a couple times. It's called Trustworthy Online Controlled Experiments, and I think it's basically the book on A/B testing. Let me ask you, what surprised you most about writing this book, and putting it out, and the reaction to it?

Ronny Kohavi (00:50:24):
I was pleasantly surprised that it sold more than what we thought, more than what Cambridge predicted. So when first we were approached by Cambridge after a tutorial that we did to write a book, I was like, "I don't know, this is too small of a niche area."

Ronny Kohavi (00:50:47):
And they were saying, "So you'll be able to sell a few thousand copies and help the world." And I found my co-authors, which are great. And we wrote a book that we thought is not statistically oriented, has fewer formulas than you normally see, and focuses on the practical aspects and on trust, which is the key.

Ronny Kohavi (00:51:10):
The book, as I said, was more successful. It sold over 20,000 copies in English. It was translated to Chinese, Korean, Japanese, and Russian. And so it's great to see that we help the world become more data-driven with experimentation, and I'm happy because of that. I was pleasantly surprised.

Ronny Kohavi (00:51:31):
By the way, all proceeds from the book are donated to charity. So if I'm pitching the book here, there is no financial gain for me from having more copies sold. I think we made that decision, which was a good decision. All proceeds go with the charity.

Lenny (00:51:47):
Amazing. I didn't know that. We'll link to the book in the show notes. Trust is in the title. You just mentioned how important trust is to experimentation. A lot of people talk about, "How do I run experiments faster?" You focus a lot on trust. Why is trust so important in running experiments?

Ronny Kohavi (00:52:03):
So to me, the experimentation platform is the safety net, and it's an oracle. So it serves really two purposes. The safety net means that if you launch something bad, you should be able to abort quickly, right? Safe deployments, safe velocity. There's some names for this. But this is one key value that the platform can give you.

Ronny Kohavi (00:52:25):
The other one, which is the more standard one, is at the end of the two-week experiment, we will tell you what happened to your key metric and to many of the other surrogate, and debugging, and guardrail metrics. Trust builds up, it's easy to lose.

Ronny Kohavi (00:52:43):
And so to me, it is very important that when you present this and say, "This is science, this is a controlled experiment, this is the resolve," you better believe that this is trustworthy.

Ronny Kohavi (00:52:57):
And so I focus on that a lot. I think it allowed us to gain the organizational trust that this is really... And the nice thing is when we built all this checks to make sure that the experiment is correct, if there were something wrong with it, we would stop and say, "Hey, something is wrong with the experiment."

Ronny Kohavi (00:53:17):
And I think that's something that some of the early implementations in other places did not do, and it was a big mistake. I've mentioned this in my book so I can mention this here.

Ronny Kohavi (00:53:28):
Optimizely in its early days were very statistically naive. They sort of said, "Hey, we're real time. We can compute your P values in real time," and then you can stop an experiment when the P value is statistically significant. That is a big mistake. That inflates your, what's called type one error or the false positive rate materially. So if you think you've got a 5% type one error, or you aim for that P value less than 0.05, using real time P value monitoring to optimize the offer, you would probably have a 30% error rate.

Ronny Kohavi (00:54:06):
So what this led is that people that started using Optimizely thought that the platform was telling them they were very successful. But when they actually started to see, "Well it told us this is positive revenue, but I don't see this over time. By now, we should have made double the money."

Ronny Kohavi (00:54:23):
So their questions started to come up around the trust in the platform. There's a very famous post that somebody wrote about how, "Optimizely almost got me fired," by a person who basically said, "Look, I came to the org. I said, 'We have all these successes.' But then I said, 'Something is wrong.'"

Ronny Kohavi (00:54:40):
And he tells of how he ran an A/A test when there is no difference between the A and the B. And Optimizely told him that it was statistically significant too many times. Optimizely learned. Optimizely, several people pointed, I pointed this out in my Amazon review of the book that the authors wrote early on. I said, "Hey, you're not doing the statistics correctly."

Ronny Kohavi (00:55:05):
Ramesh Johari at Stanford pointed this out, became a consultant to the company, and then they fixed it. But to me, that's a very good example of how to lose trust. They lost a lot of trust in the market. They lost all this trust because they built something that had very much inflated error rate.

Lenny (00:55:26):
That is pretty scary to think about you've been running all these experiments, and they weren't actually telling you accurate results. What are signs that what you're doing may not be valid if you're starting to run experiments? And then how do you avoid having that situation? What kind of tips can you share for people trying to run experiments?

Ronny Kohavi (00:55:47):
There's a whole chapter of that in my book, but I'll say one of the things that is the most common occurrence by far, which is a sample ratio mismatch. Now, what is a sample ratio mismatch?

Ronny Kohavi (00:56:00):
If you design the experiment to send 50% of users to control and 50% of users to treatment, it's supposed to be a random number, or a hash function. If you get something off from 50%, it's a red flag.

Ronny Kohavi (00:56:15):
So let's take a real example. Let's say you're running an experiment, and it's large, it's got a million users, and you've got 50.2. So people say, "Well, I don't know. It's not going to be exactly the same as 50.2. Reasonable or not?" Well, there's a formula that you can plug in. I have a spreadsheet available for those that are interested, and you can tell, here's how many users are in control. Here's how many users have in treatment. My design was 50/50, and it tells you the probability that this could have happened by chance.

Ronny Kohavi (00:56:45):
Now in a case like this, you plug in the numbers, it might tell you that this should happen one in half a million experiments. Well, unless you've run half a million experiment, very unlikely that you would get a 50.2 versus 49.8 split. And therefore, something is wrong with the experiment.

Ronny Kohavi (00:57:06):
I remember when we implemented this check, we were surprised to see how many experiments suffered from this. Right? And there's a paper that was published, 2018, where we share that at Microsoft, even though we'd be running experiments for a while, is around 8% of experiments that suffered from the sample ratio mismatch.

Ronny Kohavi (00:57:29):
And it's a big number. I think about this. You're running 20,000 experiments a year. So many of them, 8% of them are invalid. And somebody has to go down and understand, what happened here? We know that we can't trust the results, but why?

Ronny Kohavi (00:57:44):
So over time, you begin to understand there's something wrong with the data pipeline. There's something that happens with bots. Bots are a very common factor for causing sample ratio mismatch. So that paper that was published by my team talks about how to diagnose sample ratio mismatches.

Ronny Kohavi (00:58:06):
In the last probably year and a half, it was amazing to see all these third party companies implement sample ratio mismatches, and all of them were reporting, "Oh my god, 6%, 8%, 10%." So it's sometimes fun to go back and say, how many of your results in the past were invalid before you had this sample ratio mismatched test?

Lenny (00:58:32):
Yeah, that's frightening. Is the most common reason this happens is you're assigning users in the wrong place in your code?

Ronny Kohavi (00:58:40):
So when you say most common, I think the most common is bots. Somehow, they hit the controller, the treatment in different proportions. Because you change the website, the bot may fail to parse the page, and try to hit it more often. And that's a classical example. Another one is just the data pipeline.

Ronny Kohavi (00:58:58):
We've had cases where we were trying to remove bad traffic under certain conditions, and it was skewed because of the control and treatment. I've seen people that start an experiment in the middle of the site on some page, but they don't realize that some campaign is pushing people from the side.

Ronny Kohavi (00:59:13):
So there's multiple reasons. It is surprising how often this happens. And I'll tell you a funny story, which is when we first added this test to the platform, we just put a banner say, "You have a sample ratio mismatch. Do not trust these results." And we noticed that people ignored it. They were starting to present results that had this banner.

Ronny Kohavi (00:59:37):
And so we blanked out the scorecard. We put a big red, "Can't see this result. You have a sample ratio mismatch. Click to expose the results." And why we do we need that okay? We need that okay button because you want to be able to debug the reasons, and sometimes the metrics help you understand why you have a sample ratio mismatch.

Ronny Kohavi (01:00:00):
So we blanked out the scorecard, we had this button, and then we started to see that people pressed the button and still presented the results of experiments with sample ratio mismatch. And so we ended up with an amazing compromise, which is every number in the scorecard was highlighted with a red line, so that if you took a screenshot, other people could tell you how to sample ratio mismatch.

Lenny (01:00:24):
Freaking product managers.

Ronny Kohavi (01:00:26):
This is intuition. People just say, "Well, my [inaudible 01:00:30] was small, therefore I can still present the results." People want to see success. I mean, this is a natural bias, and then we have to be very conscientious and fight that bias and say when something looks too good to be true, investigate.

Lenny (01:00:45):
Which is a great segue to something you mentioned briefly, something called Twyman's law. Yeah. Can you talk about that?

Ronny Kohavi (01:00:51):
Yeah. So Twyman's law, the general statement is if any figure that looks interesting or different is usually wrong. It was first said by this person in the UK who worked in radio media, but I'm a big fan of it. And my main claim to people is if the result looks too good to be true, your normal movement of an experiment is under 1% and you suddenly have a 10% movement, hold the celebratory dinner. It was just your first reaction, right? Let's take everybody to a fancy dinner, because we just improved revenue by millions of dollars. Hold that dinner, investigate, see, because there's a large probability that something is wrong with the result. And I will say that nine out of 10, when we call it Twyman's law, it is the case that we find some flaw in the experiment.

Ronny Kohavi (01:01:45):
Now there are obviously outliers. That first experiment that I shared where we promoted that made long titles, that was successful. But that was replicated multiple times, and double and triple checked, and everything was good about it. Many other results that were so big turn out to be false. So I'm a big fan of Twyman's law. There's a deck, I could also give this in the note, where I shared some real examples of Twyman's law.

Lenny (01:02:14):
Amazing. I want to talk about rolling this out of companies and things that you run into that fail. But before I get to that, I'd love for you to explain P value. I know that people kind of misunderstand it, and this might be a good time to just help people understand, what is it actually telling you, P value of say 0.05?

Ronny Kohavi (01:02:30):
I don't know if this is the right forum for explaining P values, because the definition of a P value is simple. What it hides is very complicated. So I'll say one thing, which is many people assign one minus P value as the probability that your treatment is better than control. So you ran an experiment, you got a P value of 0.02. They think there's a 98% probability that the treatment is better than the control. That is wrong. So rather than defining P values, I want to caution everybody that the most common interpretation is incorrect.

Ronny Kohavi (01:03:08):
P value assumes, it's a conditional probability or an assumed probability. It assumes that the null hypothesis is true. And we're computing the probability that the data we're seeing matches the hypothesis, this null hypothesis.

Ronny Kohavi (01:03:27):
In order to get the probability that most people want, we need to apply Bayes' rules and invert the probability from the probability of the data given the hypothesis, to the probability of the hypothesis given the data. For that, we need an additional number, which is the probability, the prior probability that the hypothesis that you're testing is successful or not.

Ronny Kohavi (01:03:49):
That's an unknown. What we do is we can take historical data and say, "Look, people fail two thirds of the time or 80% of the time." And we can apply that number and compute that. We've done that in a paper that I will give in the notes, so that you can assess the number that you really want, what's called a false positive risk.

Ronny Kohavi (01:04:10):
So I think that's something for people to internalize, that what you really want to look at is this false positive risk, which tends to be much, much higher than the 5% that people think, right? So I think the classical example in the Airbnb where the failure rate was very, very high, is that when you get a statistically significant result, let me actually pull the note so that I know the actual number. If you're at Airbnb, or Airbnb search where the success rate is only 8%, if you get a statistically significant result with a P value less than 0.05, there is a 26% chance that this is a false positive result. It's not 5%, it's 26%.

Ronny Kohavi (01:04:54):
So that's the number that you should have in your mind. And that's why when I worked at Airbnb, one of the things we did is we said, "Okay, if you're less than 0.05, but above 0.01, rerun, replicate." When you replicate, you can combine the two experiments, and get a combined P value using something called Fisher's method or Stouffer's method, and that gives you the joint probability. And that's usually much, much lower. So if you get two 0.5's or something like that, then the probability that you've got them is much, much lower.

Lenny (01:05:26):
Wow, I've never heard it described that way. It makes me think about how even data scientists in our teams are always just like, "This isn't perfect. We're not 100% sure this experiment is positive." But on balance, if we're launching positive experiments, we're probably doing good things. It's okay if sometimes we're wrong.

Ronny Kohavi (01:05:42):
By the way, it's true. On balance, you're probably better than 50/50, but people don't appreciate how much that 26% that I mentioned is high. And the reason that I want to be sure is that I think it leads to this idea of the learning, the institutional knowledge. What you want to be able to say is share with the org's success. And so you want to be really sure that you're successful. So by lowering the P value, by forcing teams to work with the P value maybe below 0.01 and do replication on higher, then you can be much more successful, and the false positive rate will be much, much lower.

Lenny (01:06:20):
Fascinating. And also shows the value of keeping track of what percentage your experiments are failing historically at the company or within that specific product. Say someone listening wants to start running experiments, say they have tens of thousands of users at this point. What would be the first couple steps you'd recommend?

Ronny Kohavi (01:06:38):
Well, so if they have somebody in the org that has previously been involved with a experiment, that's a good way to consult internally. I think the key decision is whether you want to build or buy. There's a whole series of eight sessions that I posted on LinkedIn where I invited guest speakers to talk about this problem. So if people are interested, they can look at what the vendors say and what agency said about build versus buy question. And it's usually not a zero one, it's usually both. You build some and you buy some, and it's a question of do you build 10% or do you build in 90%?

Ronny Kohavi (01:07:17):
I think for people starting, the third party products that are available today are pretty good. This wasn't the case when I started working. So when I started running experiments at Amazon, we were building the platform because nothing existed. Same at Microsoft. I think today, there's enough vendors that provide good experimentation platforms that are trustworthy, that I would say not a good way to consider using one of those.

Lenny (01:07:44):
Say you're at a company where there's resistance to experimentation and A/B testing, whether it's a startup or a bigger company. What have you found works in helping shift that culture, and how long does that usually take, especially at a larger company?

Ronny Kohavi (01:07:57):
My general experience is with Microsoft, where we went with this beach head of Bing. We were running a few experiments and then we were asked to focus on Bing, and we scaled experimentation and built a platform at scale at Bing.

Ronny Kohavi (01:08:13):
Once Bing was successful and we were able to share all these surprising results, I think that many, many more people in the company were amenable. It was also the case that helped a lot that, there's a usual cross pollination. People from Bing move out to other groups, and that helped these other groups say, "Hey, there's a better way to build software."

Ronny Kohavi (01:08:34):
So I think if you're starting out, find a place, find a team where experimentation is easy to run. And by that, I mean they're launching often, right? Don't go with the team that launches every six months, or Office used to launch every three years. Go with the team that launches frequently. They're running on sprints, they launch every week or two. Sometimes they launch daily. I mean, Bing used to launch multiple times a day.

Ronny Kohavi (01:08:59):
And then make sure that you understand the question of the OEC. Is it clear what they're optimizing for? There are some groups where you can come up with a good OEC. Some groups are harder.

Ronny Kohavi (01:09:11):
I remember one funny example was the microsoft.com website, which this is not MSN, this is microsoft.com, has multiple different constituencies that are trying to determine this is a support site, and this is the ability to sell software through this site, and warn you about safety and updates. It has so many goals. I remember when the team said, "We want to run experiments," and I brought the group in and some of the managers and I said, "Do you know what you're optimizing for?"

Ronny Kohavi (01:09:47):
It was very funny because they surprised me. They said, "Hey Ronny, we read some of your papers. We know there's this term called OEC. We decided the time on site is our OEC." And I said, "Wait a minute. Some of your main goals is support site. Is people spending more time on the support site a good thing or a bad thing?" And then half the room thought that more time is better, and half the room thought that more time is worse. So an OEC is bad if directionally, you can't agree on it.

Lenny (01:10:18):
That's a great tip. Along these same lines, I know you're a big fan of platforms and building a platform to run experiments, versus just one-off experiments. Can you just talk briefly about that to give people a sense of where they probably should be going with their experimentation approach?

Ronny Kohavi (01:10:32):
Yeah, so I think the motivation is to bring the marginal cost of experiments down to zero. So the more you self-service, go to a website, set up your experiment, define your targets, define the metrics that you want, right? People don't appreciate that the number of metrics starts to grow really fast if you're doing things right. At Bing, you could define 10,000 metrics that you wanted to be in your scorecard. Big numbers.

Ronny Kohavi (01:11:02):
So it was so big, and people said it's computationally inefficient. We broke them into templates so that if you were launching a UI experiment, you would get this set of 2,000. If you were doing a revenue experiment, you would get this set of 2,000.

Ronny Kohavi (01:11:15):
So the point was build a platform that can quickly allow you to set up and run an experiment, and then analyze it. I think one of the things that I will say at Airbnb is the analysis was relatively weak, and so lots of data scientists were hired to be able to compensate for the fact that the platform didn't do enough.

Ronny Kohavi (01:11:36):
And this happens in other organizations too, where there's this trade-off. If you're building a good platform, invest in it so that more and more automation will allow people to look at the analysis, without the need to involve a data scientist.

Ronny Kohavi (01:11:53):
We published a paper. Again, I'll give it in the notes with this nice matrix of six axes, and how you move from crawl, to walk, to run, to fly, and what you need to build on those six axes. So one of the things that I do sometimes when I consult is I go into the org and say, "Where do you think you are on these six axes?" And that should be the guidance for what are the things you need to do next.

Lenny (01:12:21):
This is going to be the most epic show notes episode we've had yet. Maybe a last question. We talked about how important trust is to running experiments, and how even though people talk about speed, trust ends up being most important. Still, I want to ask you about speed. Is there anything you recommend for helping people run experiments faster and get results more quickly that they can implement?

Ronny Kohavi (01:12:40):
Yeah, so I'll say a couple of things. One is if your platform is good, then when the experiment finishes, you should have a scorecard soon after. Maybe takes a day, but it shouldn't be that you have to wait a week for the data scientist. To me, this is the number one way to speed up things.

Ronny Kohavi (01:13:00):
Now, in terms of using the data efficiently, there are mechanisms out there under the title of variance reduction that help you reduce the variance of metrics so that you need less users, so that you can get results faster. Some examples that you might think about are capping metrics. So if your revenue metric is very skewed, maybe you say, "Well, if somebody purchased over $1,000, let's make that $1,000." At Airbnb, one of the key metrics for example, is nights booked.

Ronny Kohavi (01:13:30):
Well, it turns out that some people book tens of nights. They're like an agency or something, hundreds of nights. You may say, "Okay, let's just cap this. It's unlikely that people book more than 30 days in a given month." So that various reduction technique will allow you to get statistically significant results faster.

Ronny Kohavi (01:13:53):
And a third technique is called cupid, which is an article that we published. Again, I can give it in the notes, which uses the pre-experiment data to adjust the result. And we can show that you get the result as unbiased, but with lower variance, and hence, it requires fewer users.

Lenny (01:14:11):
Ronny, is there anything else you want to share before we get to our very exciting lightning round?

Ronny Kohavi (01:14:15):
No, I think we've asked a lot of good questions. Hope people enjoy this.

Lenny (01:14:20):
I know they will.

Ronny Kohavi (01:14:21):
Lightning round.

Lenny (01:14:22):
Lightning round. Here we go. I'm just going to roll right into it. What are two or three books that you've recommended most to other people?

Ronny Kohavi (01:14:29):
There's a fun book called Calling Bullshit, which despite the name, which is a little extreme, I think, for a title, it actually has a lot of amazing insights that I love. And it sort of embodies, in my opinion, a lot of the Twyman's law showing that things that are too extreme, your bullshit meter should go up and say, "Hey, I don't believe that." So that's my number one recommendation.

Ronny Kohavi (01:14:57):
There's a slightly older book that I love called Hard Facts, Dangerous Half-Truths And Total Nonsense by the Stanford professors from the Graduate School of Business. Very interesting to see many of the things that we grew up with as well understood turn out to have no justification.

Ronny Kohavi (01:15:21):
So a stranger book, which I love, sort of on the verge of psychology, it's called Mistakes Were Made (But Not by Me), about all the fallacies that we fall into, and the humbling results from that.

Lenny (01:15:37):
The titles of these are hilarious, and there's a common theme across all these books. Next question, what is a favorite recent movie or TV show?

Ronny Kohavi (01:15:47):
So I recently saw a short series called Chernobyl, the disaster. I thought it was amazingly well done. Highly recommended it, based on true events. As usual, there's some freedom for the artistic movie. It was kind of interesting at the end, they say, "This woman in the movie wasn't really a woman. It was a bunch of 30 data scientists." Not data scientists, 30 scientists that in real life, presented all the data to the leadership of what to do.

Lenny (01:16:22):
I remember that. Fun fact, I was born in Odessa, Ukraine, which was not so far from Chernobyl. And I remember my dad told me he had to go to work. They called him into work that day to clean some stuff off the trees. I think ash from the explosion or something. It was far away where I don't think we were exposed, but we were in the vicinity. That's pretty scary. My wife, every time something's wrong with me, she's like, "That must be a Chernobyl thing." Okay, next question. Favorite interview question you like to ask people when you're interviewing them?

Ronny Kohavi (01:16:56):
So it depends on the interview, but when I do a technical interview, which I do less of, but one question that I love that it's amazing how many people it throws away for languages like C++, is tell me what the static qualifier does. And for multiple, you can do it for a variable, you can do it for function. And it is just amazing that I would say more than 50% of people that interview for engineering job cannot get this, and get it awfully wrong.

Lenny (01:17:31):
Definitely the most technical answer to this question yet.

Ronny Kohavi (01:17:34):
Very technical, yeah.

Ronny Kohavi (01:17:34):
I love it.

Lenny (01:17:36):
Okay. What's a favorite recent product you've discovered that you love?

Ronny Kohavi (01:17:39):
Blink cameras. So a Blink camera is this small camera. You stick in two AA batteries, and it lasts for about six months. They claim up to two years. My experience is usually about six months. But it was just amazing to me how you can throw these things around in the yard and see things that you would never know otherwise. Some animals that go by. We had a skunk that we couldn't figure out how he was entering, so I threw five cameras out and I saw where he came in.

Lenny (01:18:18):
Where'd he come in?

Ronny Kohavi (01:18:19):
He came in under a hole on the fence that was about this high. I have a video of this thing just squishing underneath. We never would've assumed that it came from there, from the neighbor. But yeah, these things have just changed. And when you're away on a trip, it's always nice to be able to say, "I can see my house. Everything's okay." At one point, we had a false alarm, and the cops came in and had this amazing video of how they're entering the house and pulling the guns out.

Lenny (01:18:56):
You got to share that on TikTok. That's good content. Wow. Okay. Blink cameras. We'll set those up in my house asap.

Ronny Kohavi (01:19:04):
Yes.

Lenny (01:19:06):
What is something relatively minor you've changed in the way your teams develop product, that has had a big impact on their ability to execute?

Ronny Kohavi (01:19:14):
I think this is something that I learned at Amazon, which is a structured narrative. So Amazon has some variance of this, which sometimes go by the name of a six pager or something. But when I was at Amazon, I still remember that email from Jeff, which is, "No more PowerPoint. I'm going to force you to write a narrative."

Ronny Kohavi (01:19:34):
I took that to heart. And many of the features that the team presented instead of a PowerPoint, you start off with a structured document that tells you what you need, the questions you need to answer for your idea. And then we review them as a team.

Ronny Kohavi (01:19:51):
And Amazon, these were paper-based. Now it's all based on Word or Google Docs where people comment, and I think the impact of that was amazing. I think the ability to give people honest feedback and have them appreciate, and have it stay after the meeting in these notes on the document, just amazing.

Lenny (01:20:13):
Final question, have you ever run an A/B test on your life, either your dating life, your family, your kids? And if so, what did you try?

Ronny Kohavi (01:20:21):
So there aren't enough units. Remember I said you need 10,000 of something to run true A/B tests? I will say a couple of things. One is I try to emphasize to my family, and friends, and everybody, this idea called the hierarchy of evidence. When you read something, there's a hierarchy of trust levels. If something is anecdotal, don't trust it. If there was an experiment, it was observational. Give it some bit of trust. As you get more up and up to a natural experiment, and controlled experiments, and multiple controlled experiments, your trust levels should go up. So I think that that's a very important thing that a lot of people miss when they see something in the news is, where does it come from?

Ronny Kohavi (01:21:06):
I have a talk that I've shared of all these observational studies that people made that were published. And then somehow, a control experiment was run later on and proved that it was directionally incorrect. So I think there's a lot to learn about this idea of the hierarchy of evidence, and share it with our family, and kids, and friends. I think there's a book that's based on this. It's like How to Read a Book.

Lenny (01:21:34):
Well, Ronny, the experiment of us recording a podcast I think is 100% positive P value 0.0. Thank you so much for being here.

Ronny Kohavi (01:21:44):
Thank you so much for inviting me and for great questions.

Lenny (01:21:47):
Amazing. I appreciate that. Two final questions. Where can folks find you online if they want to reach out, and is there anything that listeners can do for you?

Ronny Kohavi (01:21:55):
Finding me online is easy. It's LinkedIn. And what can people do for me? Understand the idea of control experiments as a mechanism to make the right data-driven decisions. Use science. Learn more by reading my book if you want. Again, all proceeds go to charity. And if you want to learn more, there's a class that I teach every quarter on Maven. We'll put in the notes how to find it, and some discount for people who managed to stay all the way to the end of this podcast.

Lenny (01:22:31):
Yeah, that's awesome. We'll include that at the top so people don't miss it, so there's going to be a code to get a discount on your course. Ronny, thank you again so much for being here. This was amazing.

Ronny Kohavi (01:22:39):
Thank you so much.

Lenny (01:22:40):
Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review, as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

