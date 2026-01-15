---
guest: Tanguy Crusson
title: Hard-won lessons building 0 to 1 inside Atlassian | Tanguy Crusson (Head of
  Jira Product Discovery)
youtube_url: https://www.youtube.com/watch?v=cZqpqb5qR5A
video_id: cZqpqb5qR5A
description: 'Tanguy Crusson is the product lead for Jira Product Discovery at Atlassian.
  In his more than 10 years at the company, he has been instrumental in taking several
  new products from zero to one,...

  '
duration_seconds: 6843.0
duration: '1:54:03'
view_count: 18833
channel: Lenny's Podcast
keywords:
- growth
- retention
- acquisition
- onboarding
- churn
- metrics
- okrs
- roadmap
- prioritization
- user research
- funnel
- revenue
- hiring
- culture
- leadership
---

# Hard-won lessons building 0 to 1 inside Atlassian | Tanguy Crusson (Head of Jira Product Discovery)

## Transcript

Tanguy Crusson (00:00:00):
Been in the product management team at Atlassian for roughly 10 years now. I worked on HipChat and Stride, and more recently I started Jira Product Discovery.

Lenny Rachitsky (00:00:09):
Why is it so hard to start new products, go zero to one within large companies?

Tanguy Crusson (00:00:13):
The company has a tendency to over-invest. Startups have the benefit of starving, and so you need to create scarcity. What we try to do is remind everyone things are going to fail, let's not drag the rest of the company into it.

Lenny Rachitsky (00:00:24):
Sounds like one of the biggest lessons is super silo sort of team.

Tanguy Crusson (00:00:28):
I needed the rest of the company to go away so we could get the autonomy to test the things that we needed, but it's not going to scale. That is not going to respect all design guidelines.

Lenny Rachitsky (00:00:35):
The biggest challenge I think a lot of companies have is just, it's been six months, no one wants this, we're going to kill it. How do you protect that?

Tanguy Crusson (00:00:41):
Be very clear about what we're testing, doing that with data, doing that with personal customer stories, give people a sense of velocity and speed. No one wants to fuck with a high-speed train.

Lenny Rachitsky (00:00:54):
Today, my guest is Tanguy Crusson. This is a really unique and important episode because we get into something you don't hear much on podcasts like this, the real talk challenges of trying to innovate and build zero to one at a large company like Atlassian. Tanguy has been at Atlassian for over 10 years and has worked on a bunch of internal big bets, some that have worked and some that have not, including products like HipChat, which I was a huge fan of back in the day, also a product called Status Page, and most recently Jira Product Discovery, which is one of the fastest growing products in Atlassian history that Tanguy led from idea to launch. We go through each of these stories, and Tanguy shares what went wrong, what went right, and everything that he's learned about creating space for innovation within a larger org, including how they structured their internal incubation program called Point A.

(00:01:45):
There's a ton of gold in this episode and a bunch of really interesting stories, which is part of the reason that it went this long. It's the longest episode I've done yet. If you're looking to create change in your organization and foster more innovation, this episode will be worth your time. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube, the best way to avoid missing feature episodes and it helps the podcast tremendously. With that, I bring you Tanguy Crusson.

(00:02:13):
Tanguy, thank you so much for being here, and welcome to the podcast.

Tanguy Crusson (00:02:21):
Thank you very much for welcoming me here, Lenny. I'm actually super proud to be on this podcast. I've been a huge fan. Whenever I get the chance, I listen to you when I drive somewhere so yeah.

Lenny Rachitsky (00:02:31):
What we're going to be talking about in this episode is we're going to be talking about building new products and going zero to one within larger companies, and in particular, the pain and the challenges that come along with that, but also the lessons that you've learned from doing this many times and seeing it done many times. You've seen a lot of this happening at Atlassian, you've been there for over 10 years at this point, and Atlassian has, I don't know, over a dozen different product lines at this point, something like that. I know a lot of people come to you asking for advice on how to build zero to one within a large company. So let me just start with a general question of just could you just share a bit about your history of building zero to one and just seeing zero to one happening within Atlassian?

Tanguy Crusson (00:03:14):
Yeah, so like you said, I've been in the product management team at Atlassian for roughly 10 years now, and I've been working mainly on bootstrapping new things. Initially, I joined to start the cloud developer ecosystem so developers can build apps on top of the Atlassian platform and sell them on the Atlassian marketplace. I worked on HipChat and Stride. HipChat was well-known, Stride less so. We were trying to win the enterprise communications market before Slack and Microsoft Teams came about. I did lead a business case to invest more in IT operations, got nowhere with it than we acquired Statuspage, Opsgenie, and something I tried to do with didn't quite get off the ground. More recently I started Jira Project Discovery, which was part of our internal incubator for two to three years, and came out of the incubator and generally available a year ago.

(00:04:13):
My track record at Atlassian has been 50/50 at best. Jira Project Discovery is actually my first, what I would call big success here. That one worked, but it was hard and all the ones that I worked on before were really hard to, and that's the kind of stuff that really bothered me for a super long time. The good thing is working on a product for product managers, I got to talk to a lot of product managers and across all sorts of industries in the past three to four years, and I realize that 50/50 is actually not that bad.

Lenny Rachitsky (00:04:46):
Awesome, and I know there's going to be a lot of real talk in this conversation. I'm excited to share and hear all these stories.

(00:04:52):
This episode is brought to you by Vanta. When it comes to ensuring your company has top-notch security practices, things get complicated fast, now you can assess risk, secure the trust of your customers, and automate compliance for SOC 2, ISO 27001, HIPAA, and more with a single platform, Vanta. Vanta's market leading trust management platform helps you continuously monitor compliance alongside reporting and tracking risks. Plus, you can save hours by completing security questionnaires with Vanta AI. Join thousands of global companies that use Vanta to automate evidence collection, unify risk management, and streamline security reviews. Get $1,000 off Vanta when you go to vanta.com/Lenny. That's V-A-N-T-A.com/lenny.

(00:05:45):
This episode is brought to you by WorkOS. If you're building a SaaS app, at some point your customers will start asking for enterprise features like SAML authentication and SCIM provisioning. That's where WorkOS comes in, making it fast and painless to add enterprise features to your app. Their APIs are easy to understand so that you can ship quickly and get back to building other features. Today, hundreds of companies are already powered by WorkOS, including ones you probably know like Vercel, Webflow, and Loom.

(00:06:16):
WorkOS also recently acquired Warrant, the fine-grain authorization service. Warrant's product is based on a groundbreaking authorization system called Zanzibar, which was originally designed for Google to power Google Docs and YouTube. This enables fast authorization checks at enormous scale while maintaining a flexible model that can be adapted to even the most complex use cases. If you're currently looking to build role-based access control or other enterprise features like single sign-on, SCIM, or user management, you should consider WorkOS. It's a drop-in replacement for Auth0 and supports up to 1 million monthly active users for free. Check it out at workos.com to learn more. That's workos.com.

(00:07:04):
Just broadly, why is it so hard in your experience to start new products go zero to one within large companies? What have you seen are the biggest challenges and hurdles generally?

Tanguy Crusson (00:07:14):
Yeah, so on the opportunity side, so Atlassian, 300,000 customers. We play in a whole bunch of different markets, everything in the collaboration space. We have a lot of markets that we play in, which means that we've got a lot of competitors. But basically when we look at the areas we could go in, there's an endless list of areas that we could go in, play and have a decent chance to win. Much harder to do if you're a startup. The breadth that we've got makes it easier to try find areas where we could expand into. We're not starving like a smaller company, so we can actually afford to try to play somewhere, to do some bets, to have some of them fail and some of them succeed, so that's amazing. Now our customers, I said 300,000. The thing that I admire the most about the Atlassian business model is it's very broad. It's across small and medium-sized companies. We have startups using our products, and we've got also enterprises and very large enterprises using the same products, which means that there's a lot of areas where we could find a niche and go after it and expand progressively into all these areas so there's a massive distribution potential that comes with that. When I worked on Jira Product Discovery, I didn't start with, okay, I'm going to need to start finding product managers and it's going to be how to find them. No, they were already all using Jira. Atlassian is a company that has a relatively deep organization hierarchy but relatively flat decision making. So it's more like a, imagine a network of key decision makers across the organization. It doesn't really matter the job title or whether you are a manager of people or not. The decisions are made by people who drive change.

(00:09:02):
So there's a lot of empowerment that comes from that, but also it's a mix of top-down, bottom-up happiness I'd say. And so it can feel really chaotic at first, but once you know how to navigate it, it's actually pretty easy to try to go after something that you care about. And of course, we're a big company, so there's lots of ways we can get help. Corporate development, research analysts that we can talk to whenever we want to explore something, thousands of customers that I just have to put something in the addressable community group and get hundreds of people applying to talk to me from one day to the next. So that's amazing, any startup would want that.

Lenny Rachitsky (00:09:45):
This sounds like how can anything not work when you launch a new product? You have 300,000 potential customers to launch it to. You have all the resources to build it. It sounds like decision making is efficient relatively, it's flat. You have all these different customer segments that use all these different version product lines of Atlassian. It's just like all of the opportunity possible to launch new products and still, many things do not work out, so I think this is a really important point and I think many big companies are in this. We have so much opportunity. Everything we're going to build is going to, it's going to grow like crazy because we have everything we need, but still it doesn't work out. And that's why I think we're going to talk about, it's going to be so important.

Tanguy Crusson (00:10:27):
It's going to be a little bit of therapy for me. Hopefully some people out there could go, "Okay, it's not just me having a hard time." It can happen in companies like Atlassian too.

Lenny Rachitsky (00:10:38):
Amazing.

Tanguy Crusson (00:10:38):
So yeah, let's talk about the challenges.

Lenny Rachitsky (00:10:40):
Let's do it.

Tanguy Crusson (00:10:41):
Yeah, for that. So you want to start a new thing. This thing is going to take time, and you need to be able to have that time for the time it takes until you can prove whether there is a thing or not. The thing inside Atlassian is that the path for success is super high for a new bet. If you come in and you create a product and it's got 100 customers, it's going to look cute. Remember, we serve startups and enterprises, we have self-service and sales, we've got all these motions that are in place for our bigger products. A $100 million business is a good start basically. In most companies out there, $100 million business is a home run. For us, it's not like that. We're trying to build businesses that grow really big and keep growing big over time.

(00:11:36):
Now, evaluating success can look very different between early stage and established products. For a long time at Atlassian, we were treating everything a little bit equally in that the metrics success for the same. For example, things like monthly active users is the way that you, for a long time we looked at you go, is that product being successful on it? And what if you are building an "internal startup," your monthly active user number should look very low for quite some time up until you know that your product is ready to serve the vast majority of the customers that you want to put it in front of, so that they don't just look at it and go, "It's not ready for me."

(00:12:20):
They're going to try it and then they're going to churn and it's going to take forever to claim them back, so that makes it pretty challenging to try and start new things unless we've got the right metrics and processes and everything internally that can give room and breathing space for the bets to succeed internally. And for many years, we were not there. We started getting there more recently with the start of Point A, which was our internal incubator program, which is one of my latest that was successful. The ones before didn't have that, and I really struggled from that, and I see many companies struggling with that exact aspect.

Lenny Rachitsky (00:12:58):
Amazing. Let's dive into an actual story. There's three that I want to talk about. There's HipChat, which you mentioned. There's Status Page and then there's the product you're working on now, Jira Product Discovery. So with HipChat, funny story, I loved HipChat. I was a huge user of HipChat at my startup back in the day. I can never forget the billboard that you all put out promoting HipChat where there's this little stick figure meme guy and it just said, "Why use HipChat?" And I thought that was the funniest thing, and the product was so delightful. There's just all these little emojis in there, and the idea with HipChat for Atlassian was basically to become the Slack killer, that was the vision.

Tanguy Crusson (00:13:39):
You just killed me. We were way before Slack.

Lenny Rachitsky (00:13:43):
Okay, so first mover advantage, amazing product.

Tanguy Crusson (00:13:47):
It works, yeah.

Lenny Rachitsky (00:13:47):
And it was an acquisition for Atlassian.

Tanguy Crusson (00:13:48):
It was an acquisition.

Lenny Rachitsky (00:13:50):
Awesome. So let's talk about what went wrong with HipChat. What did you learn?

Tanguy Crusson (00:13:53):
All know Atlassian as company, as the tool that could almost have a, okay. [inaudible 00:13:57].

Lenny Rachitsky (00:13:57):
Yeah, this is the therapy. The therapy session begins.

Tanguy Crusson (00:14:03):
Yeah, it's going to start right there. Me and everyone else from the HipChat team I can tell you. Okay, so yes, HipChat was an acquisition, team of 20 people or so. It was Slack before Slack was there. Great traction and lot of, it was a darling with startups. It was a new way to collaborate back then. There were a few of these smaller apps that were trying to do this thing. I remember actually joining Atlassian. Before that, I was working with financial services, banks and stuff like that, and we were big meeting to talk about stuff, or going to someone's desk to talk about stuff. I joined this company where my colleagues who sit on the same floor as me and on the same table, we talk over the computer via chat. I often felt weird at first looking over my shoulder to the person I'm currently talking to and we're having an argument, but we're doing it over text. Anyway, it might seem a bit cute to the people who had been born in the Slack world, but it was a major change back then.

Lenny Rachitsky (00:15:03):
Yeah, I remember that. I remember that, I was in the same office with my team and we're using HipChat to chat and it felt strange. Now it's completely normal.

Tanguy Crusson (00:15:10):
It's just normal, and Hipchat was one of the first to move there. Slack came out of nowhere. Company actually initially was focused more on gaming and they really took the market by storm. The growth numbers were dizzying when we're looking at them. And so at some point, Hipchat was left relatively alone for a while inside Atlassian. You're doing something good, so keep going after it. But with Slack, we now had to try to go bigger, so we started this thing called HipChat Go Big, the team, they recruited-

Lenny Rachitsky (00:15:44):
That was the name of the project? HipChat Go Big?

Tanguy Crusson (00:15:46):
Yeah, HipChat Go Big. And then it was HipChat Next Gen, there was a few different. Anyway, yeah.

Lenny Rachitsky (00:15:51):
Very clear. HipChat Go Big, I love it.

Tanguy Crusson (00:15:55):
Go big. But it was really a go big, lots of new developers, lots of new product managers, designers, the full company behind this product kind of thing. We tried to grow it very aggressively for a product that did not change that fast before it had reached good product market fit already, hundreds of thousands of users on a daily basis, and all of a sudden that you get a lot of people who want to make changes to it, to compete against this new threat. The platform is not so ready for so many people to work on it. And so we got to the inevitable, okay, it's too much tech, we can't do much about it so we made the decision to rewrite it. There's lots of literature around there around should you do rewrite? Should you not do rewrite? You ask me now, I tell you never. Trust me.

Lenny Rachitsky (00:16:44):
That's what most of the advice is, never do a rewrite, and people still do it.

Tanguy Crusson (00:16:46):
Never do a rewrite, and there's good reasons for that. But basically we did that and out of it came up actually a new product called Stride, which was initially "HipChat next gen." The problem is that the product was great, but by the time we were done, Slack was just miles ahead of us. At that point, Microsoft launched Teams. I don't know if you remember this moment where Slack put an ad in the, I think it was The New York Times, copying the Apple versus Microsoft thing from ages before going, "Welcome to the game, welcome to the party, we'll welcome you competitors," and stuff like that and Slack got pretty much destroyed by Teams. We started coming because it was like Microsoft distribution advantage. Everyone in Office is going to get it. They're giving it for free as part of Office, it was unbundled I think a few months ago.

Lenny Rachitsky (00:17:38):
Which is ironic because in theory, Atlassian also has that same advantage, right? You have all these products, you could bundle it.

Tanguy Crusson (00:17:46):
We are going to talk about that actually in a minute.

Lenny Rachitsky (00:17:50):
Okay, great.

Tanguy Crusson (00:17:51):
Because that was what helped us, how we thought we would win, and it was how I think we lost.

Lenny Rachitsky (00:17:59):
Amazing. Let's get in.

Tanguy Crusson (00:18:00):
So anyway, this all happened, and in the end we executed the market. We sold HipChat and Stride to Slack and basically exited the enterprise communications market.

Lenny Rachitsky (00:18:10):
Just to double down that, but you sold that to Slack and now Salesforce basically, that's the word ended. I don't know if people know that.

Tanguy Crusson (00:18:19):
Yeah, actually, it was noticed by the market in that as soon as we did that, our stock price went up. I think it was $60 back then and it went up to 70. I mean, that really sucked for us, the team working on it. First, no one tells you, but failure, everyone tells you failure is great because you learn so many things, but failure to start with really sucks. None of us here were really happy about this on the team because we had spent years, on my part, it was three years, but the people who were before that on HipChat was longer than that. Obsessing over it, obsessing over every detail, every customer conversation, every solution, should we rewrite, should we this, should we do that?

(00:19:07):
So many intense conversations, and from one day to the next, it didn't matter anymore. We had worked on something and that's it, that's the end. I'm sure many startups have been through that before. For me it was the first time it felt that personal, and the market the next day went, "Oh, you're stopping doing what you're doing? Awesome. Yes, 10 more dollars to your stock price." So yeah, there's a personal side to all the stories. For us, there was a bit like the seven stages of grief after we shut down HipChat.

Lenny Rachitsky (00:19:38):
How long was that period of mourning and stages for you and the team?

Tanguy Crusson (00:19:42):
It lasted a few months. I was not part of the decision making team for shutting down HipChat. I was one of the product managers on the team leading one of the three pillars. I got brought in, I think it was a month or two, a month before it was announced for the team to go, "Hey, Tanguy, by the way, just so you know, HipChat is no more, and now your mission is to find a new mission for the team after that."

(00:20:11):
We basically spend the next two, three months trying to make sure that the squads were created to fully own what they do there, to make sure that they're the ones talking to the customers, they're the other ones trying to come up with strategies, trying to come up with solutions and everything in that area. As long as it was people interacting with Atlassian products on other surfaces, everything was fair game, and so there was a lot of ups and downs and everything. I think it took about two, three months before we got back to a new rhythm. And some people, when we talk about it, were still scarred by it basically.

Lenny Rachitsky (00:20:49):
What are some lessons from that experience?

Tanguy Crusson (00:20:51):
Yeah, so the main one that I personally got from this, and it's back to the hypothesis that you talked about, which we have all these successful products, we can expand into this one which is, and I quote it, but it's just myself, don't eat your own bullshit, which is a mix of two things. We've got a company value that says open company, no bullshit. So we need to be able to talk about the things like they are, and we don't try to make things sound smarter than they are. We don't try to hide the truth, we go after that truth, and we don't hide stuff from each other. We share with everyone, we are open by default. So that's one of the values and we do a lot of dogfooding, so eat your own dog food. We do test our own software a lot.

(00:21:36):
I've noticed that sometimes there are things that we do while we tend to believe stuff because it's worked for us before, and we have this assumption that it's going to keep working for us forever. The founders keep telling us what took us here won't take us there. That's a thing we keep hearing over and over again. But it's very easy for teams when they see success of something to think that it's successful because of X, but X is not validated. That's where we go back to the topic we've got today, which is why is doing this in a successful company harder sometimes. Well, Atlassian was successful with the playbook, and the playbook was we've got people in developers or tech or IT. They choose Atlassian apps, they love them. They start to recommend them to people in the business, and we start to see adoption, bottom-up adoption across the company before people decide to standardize on Atlassian.

(00:22:43):
We made the bet that we can apply this playbook to this market, which is basically we can, from people to use Jira, introduce HipChat, and then people will go into HipChat first in tech teams, and then it will expand into business teams, and it'll go world to world basically from that. The thing is we didn't, in my opinion, do enough to validate that assumption early enough. We did a lot of work, a lot of work even on other things, even when faced with signals that this might not work. I do remember talking with a lot of customers who were like, "Well, we've got, the IT is on HipChat, but the business prefer Slack." And then we started to see those businesses choosing Slack, which is the, initially it was like the developers try things and they like it and then everyone starts to adopt. In that case, the Slack managed to create a very strong fund base in roles that were not tech and IT.

(00:23:48):
It was the moment where the consumerization of apps, that trend was starting to get really high. Slack really rode that and they focused everything in their experience to catch that. They gamified onboarding, they focused a lot more on the look and feel. They try to make it pleasant, modern, functional to use. There's a lot of stuff that we learned since then from what they did, we had missed that part. The part that I took personally from that is that there's a lot of assumptions in what made us successful, it doesn't mean that it's going to work.

Lenny Rachitsky (00:24:23):
Just I understand what you're saying, which is really interesting that Atlassian was really successful selling basically to the buyer within the org, the IT team because they had everything they needed. They checked all the checkboxes, but it turned out in the Slack case, it was the users that ended up having the most influence over what tool they'd opted.

Tanguy Crusson (00:24:42):
I'd actually phrase it more as both were going after the users. Atlassian was going after the users in tech teams, Slack was going after the users in business teams. And in both cases, what happened was a bottom-up adoption. The people on the other side, the business would prefer Slack, the developers, they prefer the HipChat. We did a lot of work in the streams I was working on. We're integrating with every developer tooling out there to make sure that every tool that they use goes into HipChat and from HipChat back to those tools. And basically, they can do a lot of work by seeing an activity stream in HipChat. Business? Eh, not so excited by this. Emojis, a lot of other things that may at some point I remember we were thinking those things were trivial. No, they were not trivial. It was just a different approach for using the tool by a different set of users that we did not talk enough to.

Lenny Rachitsky (00:25:36):
So is the lesson here, don't underestimate the challenge you'll have convincing a new segment to buy your thing. You may think they're close or similar, but they're probably not.

Tanguy Crusson (00:25:46):
Yeah, that's one of them. The other one is what took you here is not going to take you there. And so go back and try to explain why you are successful today, and then if you think you can use the same thing on the next thing, find ways to validate it, find ways to test it. Don't just go and build on those assumptions. That's the main thing I got out of this ordeal basically for the stuff I did after.

Lenny Rachitsky (00:26:15):
How would you do that? How would you go about and test it? Is it use research? Is it the PMs talking to potential users? What would you have done there?

Tanguy Crusson (00:26:22):
For example, when we started Jira for the Discovery, which is, so maybe I should introduce this for a second. It's a product for product managers, which is mainly used for prioritization and roadmap. People use Jira to plan and track work when it's committed. We wanted to create a space before that so people debate priorities with everyone that should be involved in that prioritization process, whether it be the developers, designers, so people in the product team or people outside of it, customer success, salespeople, support, leadership and so on and so forth. When we started, that we thought, okay, the product managers are already in Jira. You know what? We can reach them. So we create the tool, and then we'll distribute it from Jira. We could have gone down the path of building that and then started to start to distribute it.

(00:27:15):
Instead, we did things like before we brought a single line of code, put an ad inside a Jira newsletter going, "Hey, we've got this thing for product managers coming up." And then we had a website that before we had any line of code written that said, "Hey, product managers, your job is hard. We want to help, put your name here if you want to join us on the journey," that kind of thing. And that's when we saw, I think it was in two weeks, we got more than 3000 signups to that waitlist. We're like, "Okay, cool. Validation of demand." We are talking to people who are interested and we can reach them. That's one examples of the things that I tried later, just to make sure that we validate the hypothesis that we've got much earlier on in the game basically, and not once it's too late.

Lenny Rachitsky (00:28:06):
Awesome. That's an awesome, very tactical example.

Tanguy Crusson (00:28:09):
Yeah, most of those are, none of what I'm going to talk about today is revolutionary. A lot of it is just trying to apply, asking the right question at the right time, and trying to go by whatever means to answer it really.

Lenny Rachitsky (00:28:22):
Any other lessons from the HipChat experience before we shift to a different product?

Tanguy Crusson (00:28:26):
I've got two, I'm going to do them quickly. The first one is competitive myopia, don't fall for it. At some point, the Slack was really gaining round and gaining round and capturing more of the mindshare. And everyone on Twitter was always loving them. Even when they had outrages, they were getting congratulated. I was like, "This is working mad." But the love was so strong, and the way we tended to revert back is to our functional side of the brain going, okay, we just need this one more feature. We just need this one more feature, we just need this one more feature. And we ended up reacting to whatever.

Tanguy Crusson (00:29:00):
... more feature. We just need this one more feature. And we ended up reacting to whatever the competitor was doing, which I think is really, really bad because that's when we lost basically what made HipChat successful so far, which is to serve some users really well. And instead we ended up fast following based on what the competitor was doing, which is super bad because your competitor, if you think of what they do as an iceberg, the top side, what comes out of the water is what they've shipped in terms of features, but it's based on all this stuff that they've built in terms of research and understanding of their customer base and everything else. And so you're just seeing the manifestation of what they were thinking maybe a year ago, based on what they're shipping now. But we got there.

(00:29:44):
And now whenever I work, I tend to try and ignore competition other than watching every three months or so, seeing what came out, if there's anything we should be worried about, afraid of, stuff like that. But really just try to disconnect all the creative process and the research process from what competitors do, because you can't compare. The market is huge. There are hundreds of thousands of companies out there. Not everyone has the same needs. We serve a particular set of segments. We would do better learning from them to then expand to the others than watching what competition is doing.

Lenny Rachitsky (00:30:21):
And this is advice you give to your teams, just ignore the competition, maybe pay attention at big announcements and things like that?

Tanguy Crusson (00:30:26):
We always see in the Slack Channels team sharing, okay, they just did this with AI, they just did that. So it keeps coming up, and so we often have discussions to go back, to okay, let's watch again the user interviews that we did over the past three weeks. Let's watch them all together now and remember who we are building this for. So there's a lot of trying to anchor back on what we know and how, basically building our own journey on it. And I think it's much richer for everyone to be involved.

Lenny Rachitsky (00:30:58):
I love that. So you're finding that when there's a big announcement and everyone's like, "Oh my God, look what Slack's doing," or "Look what this company's doing." It's like, "Okay, now let's spend a little time reminding ourselves what our customers have been asking us to do and let's watch a couple of user interviews."

Tanguy Crusson (00:31:11):
And even when there is something that competitors do that is right, remember, we're playing the long run and we don't always need to be first and shinier. We need to make sure that people have a problem, we solve this problem. They tell us, we solve this problem for them. They are delighted when we solve these problems for them. And so that's the stuff we should be obsessing about.

Lenny Rachitsky (00:31:32):
I love that. And you said you had one more lesson from this experience.

Tanguy Crusson (00:31:37):
Yeah, the last one, startups have the benefit of starving. Right? We're a big company, we can throw a lot of resources at something that we're excited about. So this notion of we rebuild the HipChat, was coupled with we rebuild the HipChat and we'll do this on a new platform, which is microservices and everything that we built can be reused across all the other products. So the chat text box that you've got, it's an editor that can be open full screen and it's a Confluence editor with everything that you can do there. It's built as a platform component, which is amazing when the platform is there when you start building the product. Where it's really difficult is when you try to do the two at the same time. So I think that part, if I were to work on HipChat again and say I was leading that thing, that's the part I would go, okay, we need to win the problem space first, and if the platform is there, let's use it. If it's not there, we'll hack it, test it, iterate on it with customers, and then whatever is good there, let's platformize it later.

(00:32:44):
But that's where you see what makes us super powerful as a bigger company, can also slow us down and make us focus on the wrong assumptions. So in that case, I think we thought we will win. Interestingly, I think we were convinced that we had a great shot at this market. And at the same time we thought that we could tackle the rewrite and we could tackle the platformization. All these things were necessary, but all of them at the same time was probably a bit too much to bite. Now I'm saying that, but today the editor you see in Confluence started with what we did in HipChat back then. So I would say that in terms of code, purely in terms of code, 70% of what we wrote for HipChat is probably still in the Atlassian platform today. But for a new bet, local Optima, that was really bad.

Lenny Rachitsky (00:33:37):
Yeah. Just thinking about the fact that Atlassian could have had this $30 billion business if this worked out, and I could see why people would be frustrated that it didn't work out. So thank you for sharing that story. Let's talk about Statuspage, another journey that you were a part of, that also didn't quite work out the way folks had hoped. Our therapy session continues. Talk about what that product was and what happened there.

Tanguy Crusson (00:34:04):
Yeah, so this one is actually a success story, but became a success story after I was gone [inaudible 00:34:08]

Lenny Rachitsky (00:34:10):
Okay.

Tanguy Crusson (00:34:10):
That's more like a story of big companies can play the long run and for you individually inside that process, it might look like a loss and you might feel like you're going nowhere, yet the company stays on the opportunity for long enough to make it happen. So what we're going to talk about here are my own challenges working through it for something that ended up being very successful in the end, but I felt as a failure personally back then. So Statuspage at some point... So Jira is used by developers, right? And back then, I think it was back in 2016 or even before that, 2015, everyone was moving to the cloud, everyone was adopting DevOps, you build it, you run it. So basically developers would implement the software and then they would put it to production. And after they put it to production, they don't throw it over the wall to operations people. It's the same developers who operate the software in production. They go on call, yada yada.

(00:35:12):
So back then I did market research to see whether Atlassian should play there, whether we had a crack at going after all the jobs around IT operations. So Jira was basically Jira software to build software. Could we have Jira for operations? So for operating this software. And so I did market research, found a few companies that were doing super interesting things there, like [inaudible 00:35:37], Opsgenie, New Relic. BigPanda was a small startup doing lots of cool stuff there, and Statuspage. Now I discovered Statuspage and found their offering super interesting, in that Atlassian is not an operations... We don't really build super deep operations tooling, what we focus on a lot is the collaborative aspects around everything. And when I was watching teams in incidents, I realized that there's a lot of chicken without a head syndrome, headless chicken, people running around like bunch of headless chicken.

(00:36:14):
Shit hits the fan, and then what you see is teams just scrambling and everything gets mixed up all together in trying to fix the problem straight away, but at the same time questioning what happened, arguing over why we got there. Your boss is pinging you to go, "Hey, what's going on? I've been hearing that the app is down. We're losing money." Customers are emailing you and asking you what's going... Your support channels get blown up. Sales people are worried because their customers are calling them. So basically, it ends up being a super stressful experience for everyone.

(00:36:48):
And what Statuspage was offering is something seemingly super simple, which is, well, what you should have is a status page for your services and you tell your customers about it and you can subscribe to your status page. Over there, you've got your services, and for those services you can publish an incident whenever there is one, and your customers will be notified, which means that they're not going to get in touch with support because they know you're on it. It's going to build trust with them because basically you are open in your communication with them. They're more likely to empathize with your position and be supportive as opposed to, "Oh, that stuff is done again." So there was just so many benefits of that.

Lenny Rachitsky (00:37:31):
I'm going to share a quick story while you're on this topic.

Tanguy Crusson (00:37:34):
Yeah, of course.

Lenny Rachitsky (00:37:35):
Funny enough, a decade ago, I used to work at a website performance monitoring company and I started a blog called Transparent Uptime. And my whole blog was about the power of being transparent about being down, telling people the status of things are broken right now, here's when things are going to return. It was a whole thing I was really obsessed with, and I was deep into this space. So when I saw Statuspage back in the day and Atlassian working, I was like, "I love this." And I actually chatted with the founders a bit, because they were fans of that work I was doing back in the day. Completely unrelated to anything else I've done in my life. But I was really passionate about this very strange topic and I love that companies are embracing it.

Tanguy Crusson (00:38:21):
I really loved diving deep into it for a few years, it's an amazing topic. And so anyway, there's so many fascinating things about this particular domain, but back then... So find Statuspage and we invited a few of those companies to work with us for a week to go, hey, so we're at Atlassian, we're basically the collaboration hub for everything that happens for developing teams. What would an experience look like that puts everything together and where [inaudible 00:38:48] could actually help you get the right information to the right team so they can act on it?

(00:38:52):
And so we did a week of hackathon in San Francisco all together. So people from New Relic, Statuspage and a few other companies. And out of that came really interesting concepts and there was really something there and I was like, "Okay, I should start to work on a business case for Atlassian for basically IT tool/operations." Now, big companies like Atlassian, we've got money. So in every strategy that we've got, we've got cash in the bank, we always look at should we build, should we buy, should we partner? Acquisitions can be really powerful to accelerate you. We've got quite a few success stories there. Can't remember how many we did, but Trello is one of the good examples of that, for example. So we decided to buy Statuspage and I was running the integration of the Statuspage business inside the Atlassian business.

Lenny Rachitsky (00:39:49):
Thanks for sharing all that context. What are some of the things that you learned from going through this experience? It sounds like basically it was really painful when you were a part of it and then it ended up being really successful. What are some lessons from the pain?

Tanguy Crusson (00:40:02):
My learnings from it were on the acquisition side. So big company, we've got cash, we can buy a company, it will make us go faster, is not always the case. In my case, there were quite a few things that were not as easy as I would've thought. The first one is the culture shock of a startup that joins your company. So imagine you're a startup, you've got, I don't know, 20, 30 staff or something and things are going well, and you are in full control of your destiny. And then a company buys you to accelerate you, but then you stop owning all the decisions. So the CEO, maybe you become a product person. The person who was running GTM but was also doing a bunch of product stuff, and was also doing a bunch of maybe engineering stuff, all of a sudden is just working in marketing.

(00:40:52):
There are decisions that are made above your head. For example, portfolio fit, which should be part of your product, which is things that should be used from the platform that we've got. So there's a lot of decisions that we're able to make on the day-to-day basis, that start to escape you. Big companies look much further out in the future. So Atlassian would look at the long game. And so I remember with Statuspage when they first joined, we asked about the roadmaps and they were like, well, for the next three months we're working on that and for the following three months we're thinking about potentially X, Y or Z. And so when we're like, "Okay, so what's the three-year plan?" They're like, "What do you mean the three-year plan? I don't know, we'll survive, I guess." Which is what startups do. And they were very penciled ideas about the future, but not to the extent of what a big company would expect. And so that's a really big culture shock.

(00:41:53):
And what you end up with as well, and that's for companies who are looking to get acquired out there or buying other companies, before, you had a startup and everyone was one team, depending on how the buying company is organized, you might land with silos from within your team. So the way Atlassian is organized is like many Atlassian companies, we've got a product organization, we've got an engineering organization, we've got a marketing organization, design organization, and they each roll up to a different leader which may then roll up to the same person, but still by and large different organizations that are then assembled into squads and those squads operate together. But there are rituals that are part of the squad and there are rituals that ladder up to where you are in terms of craft. So I do remember how daunting it was for the Statuspage team when they joined, to understand how to navigate that.

(00:42:47):
If I want to hire a new designer, I'm not talking to the Statuspage CEO anymore, I need to talk to the head of design for this area, which has pretty much nothing to do with the Statuspage business up until the acquisition. So that is the things that people told me when I started working on the integration, which is, hey, remember, you don't know yet, but integrations are mostly about people. They're not about technology as much or product vision. All of that stuff is the easy stuff. The hard part is the people. And I didn't quite understand at first and then I really got it by the end of it.

(00:43:27):
Because what we tell those companies is we can accelerate by buying, but in reality they are going to be faced with more internal processes around how they manage staff, performance reviews, this concept of engineering allocation, revenue forecasts, OKRs, long-term roadmaps, all that stuff comes in very new to them. So one part of the company top-down says, we bought you because you are successful, keep doing what you're doing. While many other teams without meaning to, basically end up constantly interacting so that the right processes are followed, so that the right things are done.

Lenny Rachitsky (00:44:03):
That's a really interesting point, that one group is keep doing what you're doing. We're going to leave you alone, you're the experts. And then other people that are on the ground actually building it are like, "Hey, build with this component. Hey, we need this process, we need this document."

Tanguy Crusson (00:44:15):
And it's the things that you used to be able to focus 90% of your time working on your product, and all of a sudden all of that stuff may seem parasitical but comes in and interrupts you all the time. And often the new joiners, they don't know that they basically are not only being acquired, they've been hired by the company. So they basically are joining a different company with different sets of rituals, with a different culture. All of that is very different, basically. It's not going to be the same for every acquisition. Like I said, we had some acquisitions that were great. Statuspage ended up being a huge success inside Atlassian, but when I was there, I basically worked through the difficult parts of it, where I was like, "It's not as simple as people may think." So one warning, if you're planning to do acquisitions, make sure you factor all of that in and think about the integration plans to compensate for these aspects. So you don't expect the business to join and keep running at exactly the same pace, because going to be a big slowdown before it accelerates again.

Lenny Rachitsky (00:45:17):
So maybe as a last question here, is just say you were to do an acquisition again and I don't know if you've gone through more, what's one thing you would change? What's one thing you'd recommend of let's make sure to do this thing very differently?

Tanguy Crusson (00:45:27):
One aspect that I'm going to talk about to then go there, but one aspect we didn't talk about which is we bought a product, how does that product fit with the rest? And so we had different types of acquisitions that we did. One is we buy the company and we keep the product running and then we try to integrate it with our tech stack. And then the other acquisition is we buy the company and then we kind of rebuild on our platform, or we buy with this huge synergy with our platform. And so we call that the frankenstack, otherwise. Which is, you get one tech stack here, one tech stack there and they can't quite talk to each other, identity is different, integrating is different. And so it looks like a patchwork of products and that's not what our customers want from us.

(00:46:09):
So the next time I try personally, I would treat it like hiring over treating it like buying business only. So there would be a huge component which is to both educate and tease out what it means to actually hire the team inside the company. At the same time I'm saying that because I don't want to do a big one. The next one I want to do is relatively small. Find a company that has amazing product that we can bring in as a tech-in, shut down the product, rebuild it on our platform and so it's basically the equivalent of an acqui-hire, because basically what we'll be buying is the acceleration of our roadmap.

(00:46:51):
We could try and form a team to do what they did, but they've been successful so they know what they're doing. We could probably get there one year faster. What does that mean for our revenue at the scale of Atlassian, if we can enter a market one year earlier? It's probably going to pay the acquisition back on its own. So my learnings from it were basically that it needs to be treated like hiring and what I would like to do next time is more doing it like that, basically.

Lenny Rachitsky (00:47:24):
What about in the case of HipChat, where it feels like it was a mistake to rebuild a thing. Is there for this kind of startup, don't rebuild for this kind of startup? Start again. Do you have a thought of how you separate those two?

Tanguy Crusson (00:47:36):
There's actually a big difference. There's a big difference. Which is in one case what you try to do is.... So when you rebuild, you've got a successful business, you've got hundreds of thousands of customers, for example, and you're trying to rebuild the same thing or a different thing, but for the same customers that have got expectations about your current product. In the other one is you buy a company that's got some traction, not too much, so you can shut down the business and then rebuild on your platform to reach your customer base. So it's not the same as trying to rebuild the plane mid flight, it's delaying takeoff. It's like, "Yeah, we did a trial run, the plane landed. Okay, cool. Switch to another plane, takeoff again."

Lenny Rachitsky (00:48:17):
Got it. I love that. Any other key insights and lessons from this experience before we get to your product discovery?

Tanguy Crusson (00:48:25):
One last one and then I'm going to stop with the therapy session, thank you very much for offering.

Lenny Rachitsky (00:48:30):
No, no, we got to keep it going. I got to rack up the bill on this therapy session.

Tanguy Crusson (00:48:35):
Which is, remember I mentioned I was working on a business case for... Basically going bigger in IT operations. And so there was as Statuspage as part of it, but there was a lot of stuff that I wanted to be able to do inside Jira and a whole bunch of other products to basically go big in that area, IT operations, before Jira service management, which is a very successful product we've got around that. Before it was really entering that part of the market. Everyone was excited. It was before we had an incubator internally. And so I was trying to pitch it like let's build a new product that's centered around that thing. It's on Jira and it integrates with these tools that we discussed and we can put in Statuspage there and that's actually how we could accelerate them as well, and so on and so forth. Everyone was excited, thought it made sense, lots of encouragement. I pitched it to every level of the organization from business leaders, to the CTO that we had at the time, to the CEOs. No one said no, no one said yes. For months.

(00:49:44):
For months, I was in this limbo of, I think everyone's excited about this, everyone wants this to happen, but it's not happening. And so I remember talking with my boss at the time going, what's going on? When do I stop pushing? Because at some point I'm sure I'm going to start pissing people off. And he was like, "Well, basically when you lose the passion for it. Keep going up until you feel like it's not worth pushing anymore." And I remember looking at this advice and going, wow, that was not helpful at all, based on the situation that I was in. But basically at some point I basically gave up. What happens though, and I understood that after because the company ended up going there just a year later, was that I misread the appetite and sense of urgency around that topic and the fact that Atlassian being Atlassian, we invest in so many markets, we have many opportunities like this that sit on a shelf.

(00:50:45):
Someone did the analysis, someone created a business case, that thing makes sense. There may not be a trigger for the why now. So we need a very strong trigger for why now to go after it. And I did not do a good enough job at articulating this. Why now? Why do we have to do this now versus in a year's time, in two years time? And the next team that came in afterwards did a much better job at that. But for me, that was a great learning, which is great work can get parked and [inaudible 00:51:20]. And yeah, that's just what happens, which is because we have so many opportunities and there's many companies out there that are probably faced with that, doesn't mean that we have to go after all of them. But it does make sense to explore them, and then decide when to pull the trigger, and that rationale for the sense of urgency needs to be there. It needs to be beautiful to the business days.

Lenny Rachitsky (00:51:42):
This reminds me of my chat with Mihika, who does similar work at Figma where she works a lot of zero to one stuff. And she described it as your job is to keep the flame alive and help it spread throughout the entire business if you're trying to get everyone on board with a new idea. And I like this very tactical piece of advice you're sharing here of how to do that, is make it clear why this is.... I think of it as why is it perishable? Why is this opportunity perishable? Why is it going to disappear if we don't act on it now? And you could think of it as why do we have to do this now? It's not just like "This is a huge opportunity." But we also need to do it right now to give people motivation.

Tanguy Crusson (00:52:15):
Yeah, that was a huge learning for me. I wasted months on it, but like with every failure, learnings came out of it in the painful way. So product managers are often biased towards action, or at least that's my case. I want to go and do stuff and build stuff, and try stuff with customers. And so being idle, waiting for a confirmation is not a great spot to be, but sometimes you need to recognize when you're there and it's good to step back.

Lenny Rachitsky (00:52:40):
This episode is brought to you by Coda and I mean that literally. I use Coda every day to help me plan each episode of this very podcast. It's where I keep my content calendar, my guest research, and also the questions that I plan to ask each guest. Also, during the recording itself, I have a Coda page up to remind myself what I want to talk about. Coda is an all-in-one platform that combines the best of documents, spreadsheets, and apps to help you and your team get more done. Now is the perfect time to get started with Coda, especially its extensive planning capabilities. With Coda, you can stay aligned and ship faster by managing your planning cycles in one location. You can set and measure OKRs with full visibility across teams and stakeholders. You can map dependencies, create progress visualizations, and identify risk areas. Plus you can access hundreds of pressure-tested templates for everything from roadmap strategy to final decision-making, to PRDs.

(00:53:36):
If you want a platform that empowers your team to strategize, plan and track goals together, you can get started with Coda today for free. And if you want to see for yourself why product teams at high-growth companies like Pinterest, Figma and Qualtrics run on Coda, take advantage of the special limited-time offer just for startups. Head over to coda.io/lenny to sign up and get $1,000 in credit. That's C- O-D-A.io/lenny, to sign up and get $1,000 in credit. Coda.io/lenny.

(00:54:09):
Let's try to summarize some of the biggest lessons so far that you've shared before we get to product discovery. So a few things I noted here, just how to be successful, building zero to one at a large company. One is be very clear, are the users you're going to be building this new product to actually the same users you're already selling to? And it may feel like they are close enough, but in the case of HipChat, you learned maybe not, and it's a lot harder than you expected.

(00:54:33):
Two is be careful when you rewrite. In some cases, shut it down, rewrite it immediately, accelerate this new idea internally. In other cases and you shared, and so you could rewind if you want to get the actual details of when it makes sense to go one or the other. Sometimes doesn't make sense to rewrite, just keep what you're doing and focus on the user problems and don't slow down. Another tip I wrote down is ignore the competition. Don't be obsessed with what they're doing. Focus on what your users are asking you for. And then this idea of paying attention to the why now, that's a really good one. Just like when you're trying to make a case, make it clear why it has to happen now. Is there anything else that comes to mind as I try to summarize some of the advice so far?

Tanguy Crusson (00:55:12):
No, that seems like a good one. The main one I'm getting also out of this, is if you try to start new things, it's going to be coming from your drive and your passion, and that's what pushes stuff forward. So don't give up. Because I try really hard before getting to one that worked. So I guess that's probably a testament for it's possible.

Lenny Rachitsky (00:55:36):
And a testament to your grit and desire to make something work. So on that note, let's talk about your product discovery. I know this is a success at this point. I know there was also a lot of pain that went into this and things that didn't work. So I'd love to hear both sides of it, just like what was hard about getting this off the ground and then also just what worked, what allowed you to make this work? So start wherever you want to start.

Tanguy Crusson (00:56:00):
Yeah, cool. So let's start with the good stuff before we go back into therapy. Some of the good stuff here is Atlassian at that point had recognized we are innovating in our big successful products all by doing acquisitions, we have to correct that and start building new products ourselves as well. And so there was a huge push from the founders to go, "Hey, we need to restart that." Out of it came Point A, which was an internal incubator program that was meant to fix that. And the way they framed it was that innovation is like a muscle. Unless you exercise it, it becomes weak, and what we have to do now is to work on it again. And so out of that thing, Point A and Jira Product Discovery was one of the... I think it was one of the 100 pitches that went through that innovation program. There were 100 pitches and out of it came out three products that basically went through all the different stages of it. And so it started with Jira Product Discovery was actually made possible because of that and because we're inside Atlassian. So we started with a lot of, I could take time to focus on this stuff with nothing else to do it. It was a full-time job, because of this incubator. I was able to form a team easier because there was budget allocated. I was able to form a team that was not worried about losing their job because the program was made so that technically speaking, you would borrow people from other departments. If that thing doesn't work out, they go back to your department. So there's no fear of losing your job, basically.

(00:57:34):
We were able to tap into all the research that was done by our research and insights team internally. We were able to have the corporate development team working with us. I met with probably 20 companies that played in things around product management before forming a view that, hey, maybe we should play there. And all those teams are willing to talk to us because Atlassian is a big player in this market. And so there's always the opportunity of integrating, being bought, partnering that can...

Tanguy Crusson (00:58:00):
The opportunity of integrating, being bought, partnering, that kind of stuff. I was able to meet with analysts to say, "Hey, so what do you think about the product management market?"

Lenny Rachitsky (00:58:11):
This was all part of the Point A structure?

Tanguy Crusson (00:58:14):
So the Point A structure, not all of it was formalized in Point A, remember Point A back then was created alongside the first bets that went through it, and ours was one bet as part of that. So we forged the path for all the ones that came afterwards. But basically, it gave us the crags to go in and ask for help from everyone, and everyone knew it was important. Because everyone knew the company priorities and the new products were top company priority. And so Atlassian, playing the long game, had decided that it was okay to invest in these bets and to reassess them into every three to six months to understand whether we should put more chips in it.

(00:58:52):
And so the psychological safety of everyone's job was safe, coupled with access to all the resources from the company. That part was just invaluable to the success of what JPD is today.

(00:59:03):
So to give you a bit of context, Jira Product Discovery started four years ago with some research. I was alone back then, and then we were three. The first line of code was written three years before we launched officially, as generally available. Which means that for three years we were dogfooding alpha or beta and able to do that with the full support of the company. So when I mention the long game, I mean it. It's something that's very hard to get in most companies out there.

(00:59:36):
And when people ask me about how to stop incubators, it's like think about it with when you're going to get your dollars back and forget about it for a while. What you need to see is how the teams are answering the right questions that they ask along the way, and seeing whether you are still excited about the bets as they do that.

(00:59:57):
Anyway, so we launched a year ago. Fast-forward to today, we've got 8,000 customers, amazing CSAT, great traction. It's one of the fastest growing products in Atlassian history, which is great. So what was hard though, the first one was reminding everyone that failure is the most likely outcome. And I will die on that hill to explain to people when they want to stop things internally, frame it like that, remind everyone. There's a [inaudible 01:00:28] 70% chance, [inaudible 01:00:30] completely pulled out of thin air that whatever you're working on is not going to exist in six months.

(01:00:35):
We're trying to launch a new product, enter a new market. Our goal is to get to $100 million businesses. So there's not that many of them out there. We have tried and we have failed. And a few of them are Atlassian. And so remember that, and it's super important to remember that because otherwise the company has a tendency to over invest, not the company top-down, parts of the company have the tendency to come and try to help.

(01:01:07):
So for example, "Here, we want to build this." "Oh, if you want we could change this service to be able to XYZ for you." "No, we are a bet, which is seven people. Let's not drag the rest of the company into it. The appetite that the company has right now is these seven people. We'll see what we can do with these seven people," was what I was telling everyone.

(01:01:26):
The reason I was saying that is that, otherwise, yes, you get the help, but the help always comes with condition and the condition is usually things slow down. So what we try to do is remind everyone, things are going to fail, so that we could basically buy the opportunity to hack shit together that is not going to scale, that is not going to respect our design guidelines, that is not going to fit with the JIRA target architecture. But we're going to test this with customers and see if the concepts make sense, if the prototypes make sense, whether they get value out of those before we tell you, "Hey, you know what? That thing is a thing and by the way, now we're a proper business. We should build that thing into the platform."

Lenny Rachitsky (01:02:08):
This is really interesting because it's counterintuitive to think that you should position your new bets as, this is most likely going to fail. This is just the thing we're trying, don't worry, don't commit too much this yet, don't worry about giving us all these resources. Why do you think that's so important? Because I don't think most companies position new incubations that way. Why do you think that's so effective and more effective?

Tanguy Crusson (01:02:29):
Yeah. So the thing that we're trying to do when starting new products is to basically emulate a startup in an environment that is not hungry, is not starving. And so you need to create scarcity. What I wanted with my team is to make sure that they feel the urgency. That thing needs to move. I also needed the rest of the company to go away, so we could get the autonomy to test the things that we needed to know whether this thing is even going to work or not.

(01:02:57):
We could not go into a planning session for the next six months to negotiate something with a platform service so we can build a feature to then test with users. I said, "Now, we're rebuilding this component and we're testing this with customers next week. It's not perfect. It's not perfect." And so that helped us a lot, but otherwise there's always this tendency of the process that works for everything else is going to work for this and we do need to keep reminding them, "Hey, we might not exist in six months. Do you really care that much about this process right now? The product might not exist anymore." The process goes away usually.

Lenny Rachitsky (01:03:29):
So it's basically a trick to keep everyone else within the org away and not worry about what you're building? Because you just tell them, "Don't worry, this is not going to work out. We're just going to try this thing just to see." So it's not for your team to feel like, "This is probably not going to work out." I imagine the team is like, "Oh, we got to make this work. It's such a good idea." It's more as a trick to keep the org from swallowing you up and pushing you around?

Tanguy Crusson (01:03:52):
So there's a part of that, but there's also really a need from... We need to respect Atlassian's dollars here, and if we don't know whether this thing is going to work... I do not want to drag a team of 50 people into this. I want to know that this thing is worth the investment of a team of 50 people. So it's a bit of both, actually. Now, it's of course, easier said than done. And so that's where, again, Point A helped. We had four stages called Wonder, Explore, Make and Impact, where in the first stage it was all about proving that there was a problem area we could go into, there was a market.

(01:04:27):
We could answer very clearly, articulate why Atlassian should move there. We could articulate why now that stuff that [inaudible 01:04:35] struggled with before, and have enough data to validate all those claims. Explore was about exploring solutions, which doesn't mean build it and throw it out there and see what sticks. It's about if you get a bunch of customers raising a problem, can you get them to play back to the solution, [inaudible 01:04:53] address that problem?

(01:04:54):
And so in the case of Jira Product Discovery, because we were not building, we didn't need any new technology, it was mainly new UX and new workflows, we basically validated a lot of that with Figma in dozens of Zooms. But it's basically coming back saying, "Here's how those companies are framing it. Here's their problems, here's how this thing would be solving it for them."

(01:05:18):
So that's part of Explore, which is validating that it's worth investing in in terms of solution. We don't only have the right problem, we've got the right solutions. Then Make is about making it happen in stages, starting with an alpha, then a beta, and then going out there. And Impact is that stuff is actually ready to go [inaudible 01:05:37]. And now let's see the impact it has on Atlassian's business and keep monitoring it from there.

(01:05:42):
And it turns into a real business from that point onwards. But everyone at Atlassian knew these four stages, Wonder, Explore, Make, Impact. Whenever we were talking with teams, we were telling them we're currently in Explore. And we started doing that with the full bet itself. Then we started doing that to talk about the different features that we were working on or problem areas we were going after. Which means that now every time we go into conversation with other teams and we'll mention, "We're in Wonder," or, "We're in Explore," they know what to expect. When we go to someone in the leadership team and we say, "We want to go from Explore to Make," they know they're going to [inaudible 01:06:22] because they need developers now.

(01:06:23):
So all that vocabulary and clear expectations set for every stage of the process really helped us to facilitate all the conversations that we had with everyone in the organization. And really protected us again from all those, basically, teams that felt like they had to chime in. Now, we're in Explore, we don't have anything ready that's been validated. Let's not have opinions about how the architecture is done before we have validated that customers want something.

Lenny Rachitsky (01:06:52):
This is super cool. I feel like we could do a whole podcast just on the structure of Point A and how you all do this. But just one question, what does the gate look like when you move from Explore to Make, Make to Impact? Is there a group of people that sit in a room and decide thumbs up, thumbs down? How does that decision work?

Tanguy Crusson (01:07:08):
So we basically write a six pager that looks at all the different aspects of all the questions that we're going to answer. And then we are in a meeting with the Point A stakeholders and the founders of Atlassian. And everyone reads that page for about 15 minutes and then question, answers, comments, and [inaudible 01:07:31] of that, by the end of this meeting, we know whether we are clear to go to the next stage.

(01:07:35):
We got booted back one time when we were like, "Hey, we're ready to go anywhere from alpha to beta as part of Make." And they're like, "No, you're not." And I was like, "No, we're not." And so we stayed and we basically got more time than what was initially allocated to us. But basically, the founders and the leadership of Point A as well as heads from the different lines of businesses at Atlassian were participating in those sessions, which-

Lenny Rachitsky (01:08:01):
That is super cool.

Tanguy Crusson (01:08:02):
Basically, visibility all the way up.

Lenny Rachitsky (01:08:05):
And they might also just decide, "Let's kill this thing, it's not working," at one of these meetings.

Tanguy Crusson (01:08:10):
So it might be, "Let's kill this thing," which happened to a number of bets that we did, or it might be, "Let's roll this thing into something else." So for example, our new whiteboards product. I say product, whiteboards feature part of Confluence initially came out of Point A. And was eventually rolled into Confluence instead because [inaudible 01:08:32] made more sense there.

Lenny Rachitsky (01:08:33):
That's so interesting. So you said there's 100 projects that went through Point A. So there's this funnel. Is there a meeting for all 100 of these that the founders go to for all these incubations or did they come join later down the funnel?

Tanguy Crusson (01:08:46):
Not the full 100 of them.

Lenny Rachitsky (01:08:47):
Okay, good.

Tanguy Crusson (01:08:50):
And I'm saying 100, it's over a few different quarters of teams coming in and [inaudible 01:08:53], but not for the initial stage of entering Point A.

Lenny Rachitsky (01:08:50):
I see.

Tanguy Crusson (01:08:58):
It's usually when they've been accepted.

Lenny Rachitsky (01:09:01):
I interrupted you and took us on a tangent, you were sharing essentially the things that went well and how this all came together.

Tanguy Crusson (01:09:08):
So failure as the most likely outcome. It's the one thing I would stand behind in everything because I've seen before what happens when we get too complacent with it's going to work. Lessons from the previous things I was talking about. So this one really key. Second one, this one is much harder, which is if you're starting something like this, your teams will need to break a lot of rules that are established. But they need to be able to do that without breaking the trust of everyone in the organization.

(01:09:39):
The rules were created to support the business at the stage where it was successful, and it just so happens that they might not work for new bets. So the trick here for me has been to... The way I pictured it is, I've got a bunch of chips. Since I joined my class, I've been accumulating chips and those chips are-

Lenny Rachitsky (01:10:03):
Like social capital.

Tanguy Crusson (01:10:04):
Yeah. It's like trust I've built with the founders, with the different business leaders, with succeeding on stuff or failing and explaining why and trying to do better next time. And all that stuff gave me, like you said capital. I've got these chips and I decided on this bet, "You know what, I'm going to go all in." So I always said, "If it works, it works. If it doesn't work, I'm probably out of here, but I'm going to go all in."

(01:10:27):
So if I see something that's not going to work, I'm going to say it. We're not going to do it. And so I knew I was going to put myself in tough conversations because people are here to protect things that need to be protected. They just don't make sense for the stuff I was working on. So one example, breaking rules without breaking trust where it was tricky.

(01:10:48):
We have a lot of rules in a company like Atlassian, and this is how it works in engineering. I mean, engineers are the biggest part of our workforce. Basically, shit gets done because engineers work on it. And what I needed was to be able to hire the right team, only principal levels, people who have a lot of internal credits so that they can commit to any team's repo, no questions asked. People who are not looking for the next promotion, but they want to make a splash. And when that's not possible, I wanted to be able to hire contractors to fill in the gaps and stuff like that. And I was like, "A lot of the rules that I need to be able to break is basically in engineering." So I decided not to have an engineering leader in the team, and to do it myself.

(01:11:36):
So I was the product leader and the engineering leader. I was technical enough to be able to have these conversations, but mainly I was just working with amazing engineers who just could self-drive themselves. So they were able to make changes in areas that were not owned by them. They were able to do changes that do not respect any of our standards. They were able to hack their way around rebuilding services and whatnot. We are now not in the position where we need to do stuff like that, but at that time I needed to take a position like that so we could actually go and move fast with basically the equivalent of being a startup inside Atlassian.

(01:12:13):
That's not comfortable to do stuff like that. And I would not recommend that in many environments. Atlassian was very forgiving throughout the whole thing. It doesn't mean that I didn't [inaudible 01:12:27] on that.

(01:12:28):
That was not simple. For example, one of the rules is, at that time we didn't want to have a footprint in Europe back then for more engineering teams. It's different today, but back then it was like that. I was like, "Shit. I'm based in France, I'm trying to start this stuff. I don't want to move to the US or move back to Australia just for this right now." So I hired contractors, lots of contractors when we started, or not lots because we're not a big team, but contractors to build this stuff.

(01:12:57):
And again, contractors, they don't fall into the same rules as the rest of engineering staff. So basically, all the rules around you need to contribute to... For example, the engineering team could say, "[inaudible 01:13:10] to the next, leadership could say, "You need to invest 15% of your time in reliability."

(01:13:15):
And for us it's like, "We're not there yet. We don't even have a prototype out." Yeah. But that's the company rule, all right. Again, no engineering manager and contractors, boom, none of these rules applied. So it was people who were looking at it from the outside who were like, "Wow, dude, are you sure you're okay with all this?" And it felt super uncomfortable, but we have the support of leadership from it. It's just a tough transition for Atlassian from the, "We only invest in the big ones for acquisitions," to "Let's invest in [inaudible 01:13:46]."

Lenny Rachitsky (01:13:45):
This is a crazy story you're telling me. So you're leading this team, you hired a team of contractors to build this product. You're in a whole different country from the rest of Atlassian, basically. And the whole idea here was just to do stuff that wouldn't be necessarily allowed at Atlassian. They wouldn't let you work this way. And you found that to make the thing you needed to make, the thing that you were betting your career on, it sounded like, you're just going to be this pirate working on this thing in France and it worked out?

Tanguy Crusson (01:14:18):
So the Point A emoji and Atlassian is a [inaudible 01:14:24]. I was not the only one. There were quite a few of us working on new bets, basically operating like that. Each questioning different rules. The end goal was not to question the rules, the end goal was to get to the stuff that we needed to do, which is we just need to clean this space, to work with users to test prototypes up until it works and progressively get to, as I said, a product that's going to be enough to launch. So we never intended to break the rules, which is the things that we were going to choose the ones that were going to work to support us on this mission and say no to the others.

(01:14:58):
You mentioned Europe. At the time, a lot of other Point A founders were struggling with the fact that they were operating from their mothership in Sydney because they're still with everyone else. You were talking about doing all this stuff, but remember that we've got this OKR thing, we've got this vision for GR that we're building, you need to participate in all this. And so I was in Europe going, "Fine, schedule it at your time."

(01:15:28):
And I think a lot of teams were like, "We don't care enough about this test. They're telling us it's not going to exist in six months. I don't care enough about this to stay up late or wake up super early every day to disagree with them." And so there was a lot of the early success that we had in being able to move super fast that came from being so far, that people just did not engage to stop us.

(01:15:58):
And that's why we were initially the group with the fastest speed. Then it was possible to institutionalize those things into Point A to then make it possible to do it from within Atlassian. But at first, we just needed to blaze our way through. So that's what we did.

Lenny Rachitsky (01:16:16):
So it sounds like one of the biggest lessons and things that work well for something like this is a super silo sort of team, as much as you can disconnect from the core business and let them just do what you think you need to do?

Tanguy Crusson (01:16:30):
You've interviewed Megan on the show before.

Lenny Rachitsky (01:16:30):
Yeah.

Tanguy Crusson (01:16:33):
And I listened again to the way she pitched Point A, and yes, that's exactly what came out of what she was saying. Which is, we gave the space for those teams to be able to do this with a lot of autonomy. And that was the outcome of all that work, basically, which is the program was then set up so new teams could do it and fitting within the mothership, basically.

Lenny Rachitsky (01:16:55):
And I think people hear that, like yeah, okay, of course. [inaudible 01:16:59] incubations, silo, separate, they do their own thing. People hear and they try to do that, but I imagine it's not actually what they need to do. And what I'm hearing is you went to a pretty far extreme of making that happen, not basically breaking the rules to allow for a silo to actually exist. And I love that. What else was key to the success of making this work out?

Tanguy Crusson (01:17:22):
So the one that I'm most passionate about is how we work with customers is very different in a super early stage bet versus to what you do in a very established product like Jira. So the first part is, how can we innovate in a way that doesn't fuck up existing customers? Jira, 120,000 customers, Atlassian, 300,000 customers. We can't just go in there, start experimenting, breaking a whole bunch of shit that millions of people experience and go, "What are you doing, Atlassian?" So what we needed is to create this area where we could experiment that's away from Jira while being inside Jira.

(01:18:06):
That part was a bit tough. It's possible to do. In fact, I came across an article from Ben Weiss. No, sorry, Noah Weiss, it's from many years ago now. Where he was basically talking about innovating in a successful material product and talked about three stages of incubate, iterate, integrate. And as part of that he gave the examples of Instagram, Twitter, and Foursquare. Where basically he was explaining, at the beginning, for example, Instagram was a feed that was chronological. And then the team started to experiment with a popular tab that was on the side that was not integrated into the core of the product that everyone uses.

(01:18:47):
They iterated on that for a while. That became the explore tab and then the explore tab became the main feed. The feed is not chronological anymore, it's based on your interests. And that part really resonated with me where I was like, "You know what? We're going to try to apply that to Jira, which is we're going to build it in Jira, but we're going to extract ourselves from a lot of the core components of the core base to rebuild the UX that would work for the audience we're going after."

(01:19:17):
Our audience is product managers. They have no patience for spinners, things need to be visual. They need to be able to quickly move things around to visualize the potential options they've got on their roadmaps and stuff like that. It needs to be snappy, it needs to get out of the way, but also something that they can feel proud to present to their stakeholders to have discussions around that.

(01:19:39):
It can be bogged down into the details. It can go to very, very deep [inaudible 01:19:43]. It needs to be an area, a space where you feel like you can breathe and have creative conversations. And Jira's UI was not exactly known for that. And in fact, most of the product managers I talked to were like, "I don't want to do this in Jira. It's too strict, there's too many workflows, it's owned by IT," yada, yada. And so we said, "That's fine. We're going to experiment with an experience that's going to be detached from Jira still on the same platform."

(01:20:09):
And that's what we did, basically. And so this concept of incubate by working on something on the site, iterate until you've got it right and then integrate it back into the main product is something I would definitely do again. We're currently in the middle of the integration phase for Jira product discovery.

Lenny Rachitsky (01:20:28):
So the lesson there is don't force yourself to be a part of the broader product, initially. First, figure out what it could be if it's its own thing, and then eventually you can integrate?

Tanguy Crusson (01:20:40):
It depends who you're doing it for and the programs that they've got. Don't feel limited by your platform to answer the core things that are necessary for your product to work, basically. So if the platform is good enough for us, if the UX was good enough for the product managers, we would not have done that. And we would've had a hard time justifying it, but because it was not, we basically gave ourselves the stamp to be able to do it. So still in don't fuck existing customers, something I read from a site, from Reforge that talk about the Safety Funnel.

(01:21:16):
So they have this thing where the typical growth funnel goes from acquisition all the way to revenue and there's a whole bunch of different stages in between. Your goal is to maximize the number of people who go through this funnel successfully.

(01:21:29):
And I was trying to explain to people what we were trying to do with Jira Product Discovery, and I was struggling to put a name on it. And it was we're going to work with a few, small number of customers up until it's right for them and then we're going to expose it to progressively more people. And I know it's very common sense, but that's basically what we decided to do instead of the Atlassian way, which was more, "Hey, we measure our success based on..." For example, at that time, I think it was still before all those projects, "... monthly active users." If that was a measure of success, we would've been pushed very quickly to go and expose it to as many people as we could. We didn't want to do that because if they would have a bad experience, it would've been very hard to claim them back afterwards.

(01:22:11):
So someone in Reforge put the name on Safety Funnel. So the Safety Funnel is amazing. People don't understand that. You basically put a hard stop and you limit the number of people who had bad experiences. And you do that for a while, up until you can prove it's amazing and then you invite more people. So we did a lot of that. So we basically created that pocket away from Jira to reimagine what Jira could be for product managers. And we only exposed that to a very small number of customers at first. So that's don't fuck existing customers' first principle.

Lenny Rachitsky (01:22:45):
And the reason that's important, just to put a point there, is the business will start to get upset if you're making many customers upset.

Tanguy Crusson (01:22:53):
That would've been it if we had triggered an incident that brought down Jira for millions of users. And first time might have been okay. I mean, by the third time we would've been asked to pack up and go home, I think.

Lenny Rachitsky (01:23:05):
Got it. So the advice there is just limit how many people get exposed to your very early product, even if it's going to hurt your numbers. You don't want to cause people to be like, "What the hell are you doing over there, man? [inaudible 01:23:17]."

Tanguy Crusson (01:23:16):
So [inaudible 01:23:17] your numbers is now the interesting one. So how do you frame success and how do you define metrics when your goal is basically to work with a small number of customers for a super long time? So that's what I ended up defining for this, is based on a term that was used at Atlassian that I tried to formalize it into something that everyone could refer to, which is the Lighthouse Users Program. And so the principle for it is it's a program, so it's an official thing. We have hundreds of thousands of customers at Atlassian, but we would only build the experience for a small number of them. And so there are stages to it.

(01:23:56):
The first stage is we work with 10 and we prove that the problems that they had are the things that we solved and where we spend most of the time for the first 10 Lighthouse Users is to explain why they are the Lighthouse Users.

(01:24:13):
Everything that explains why we believe they are a proxy for every customer that we serve afterwards. We then have this stage from 10 to 100 where we recruit more customers, but we're still not in the fully self-service, don't need a lot of onboarding stuff. We're still testing out the value, but we're testing the different variations in the scenarios that people face to make sure that the core solution that we've got can cater for those. So there's a lot of different options and different security needs. There's a lot of subtleties that you catch between 10 and 100.

(01:24:44):
Then we get to a stage where we're like, "You know what? It's good. It solves people's problems, but it's not self-service. We just need to explain stuff. We need to work with people on Slack. We need to work with them and answer a lot of support tickets or do a lot of Zoom calls to explain stuff."

(01:24:58):
Now we need to get from 100 to 1,000, and by getting there we basically need to solve all of that and after that we graduate. So basically by detailing that and explaining all the success criteria in between, it helps to define success in that in the make phase, we've got 10, 100, 1,000, and then people can understand exactly where we're at there, and the types of questions we're trying to answer. In the 10, we're answering every question with a user, snippet of a video call with them, either talking about their problem and solution but showing the product and how they solve with it.

(01:25:34):
That's how we wanted our stakeholders to view it, which is it's very qualitative, but have it felt from the user's perspective. It's different when we go from 10 to 100, from 100 to 1,000, but for each of those there's a playbook for how you go from one to the other. That helped us because we could then clean the space to do the right thing and we will not ask to hit, for example, a multi-active user's number or number of customers' number or percentage of users who use this number. Because it's very qualitative still when we're at that stage.

Lenny Rachitsky (01:26:09):
That is super cool and super interesting. And it's along the lines of the gates. It aligns with, at each gate, here's how many users we're looking for. Basically, it sets expectations for what success is, keeps you from having to scale things too early. It's such a cool idea. And you call it Lighthouse Users, like the Lighthouse Users Program?

Tanguy Crusson (01:26:25):
Lighthouse Users, and there's two sides to it. We just talked about the stakeholder facing side. The one I love is the team facing side of this, which is I've seen a lot of teams, Atlassian and other companies as the products grow, you tend to leverage a lot more user research, formal user research or CSAT service. And the way I call it, it's hiding behind research and not being close enough to the ground with customers. And what I want to do in the teams I work with is to create a direct feedback loop with customers, but not like someone gives you feedback and you do it. We talk...

Tanguy Crusson (01:27:00):
... with customers, but not like someone gives you feedback and you do it. We talk to those customers, we build stuff for them. So there's something I've seen which is climate change. It's a thing. Everyone knows it's a thing. We all read reports about it. We're all like ... Every time we read an IPCC report we're like, "Shit." Do we change anything? Not enough.

(01:27:23):
What makes people want to change and actually gives them a trigger to change? I've seen is a lot more empathizing with individual people's experience. If I know someone that's impacted by climate change, it's going to make me relate a lot more strongly to the concept of climate change and want to change myself. Sorry for the power note here. I'm-

Lenny Rachitsky (01:27:48):
No, that's such a good example. Such a good way of making that point very clear of just the power of talking to a small number of users versus thinking that the more data you have, looking at data, CSAT scores, NPS retention will tell you what you need.

Tanguy Crusson (01:28:02):
So what we do with that is we recruit 10 people and we put these people in front of the whole team, not just the PMs, PM, designer, engineering. We meet on Zoom, we chat, we work with the same ones over months to build a product. They are with us on Slack. We have regular things.

(01:28:20):
What we've seen, what I've seen going fast is that the engineers would go into a planning meeting and the PM would say, "So we should work on X," and the engineer will go, "Wait a minute. We've had a talk with this customer and they struggle with this so I think we should work on that instead and fix that part of the experience," and so on and so forth.

(01:28:35):
So all of a sudden you're not talking about a product manager, you're talking about a product team with product engineers. So there was this thing at Atlassian where we called some engineers were more like system engineers, some were more product engineers.

(01:28:49):
In my opinion everyone can be a product engineer. They just need to be exposed to the right user context. The right user context, what is it? It's 10 customers you know by name, you know their context, you know their problems. You can empathize with it. This empathy makes you want to act to change your product to solve their problem and you get really huge pride coming back out of it. 

(01:29:11):
It can seem counterintuitive in a company like Atlassian. 300,000 customers, right? We should build for them. Well, you can't, right? We're limited in our ability to make changes that will work for the vast majority so might as well embrace that. Embrace that we are indeed biased, that we are indeed reacting based on feelings, like wanting to help or not wanting to help or reacting strongly to what you've seen, but we are embracing that to try and build the best product possible. I've actually seen that the outcome is, so far on this product it's worked.

Lenny Rachitsky (01:29:51):
If you actually think about this from the perspective of how would a startup approach this? This is exactly how a company that's just starting out would approach it. So it makes tons of sense to think of it this way. It's just people don't actually do this. It's hard to do.

(01:30:04):
This is a segue to a question I wanted to ask. So it took probably a long time for you to show real success, real progress, real like, "This is going to work." First of all how long was that period of just like, "This is probably not going to work too. Oh wow, maybe this is going to work"? And along the same lines, how does Atlassian slash ... What have you learned about how to protect this, Pixar people call it an ugly baby? When an idea is new they call this an ugly baby. People don't want it. It's just like, "Get rid of this thing."

(01:30:36):
Man, that sounds mean to say, but that's the way they talk about it. That's the term in creativity.

Tanguy Crusson (01:30:44):
That's a good one.

Lenny Rachitsky (01:30:46):
How do you protect that because that's the biggest challenge I think a lot of companies have is just like, "It's been six months. No one wants this. We're going to kill it." How do you protect it? So how long did it take for it to show success and what have you learned about how to protect?

Tanguy Crusson (01:30:58):
Yeah. So basically, internal comms is everything there. The way I saw my job as, a large part as being very clear on where we were, on what we were learning on, how fast we were learning, how fast we were moving. Being super honest every step of the way, not try to make shit up and try to make it bigger than it is, more successful than it is.

(01:31:18):
On the contrary, be very clear about what we're testing, where we're testing it. Doing that with data, doing that with personal customer stories because we all can constantly relate to the heart and to the mind. So that's what I always try to weave into comms that I then send weekly.

(01:31:36):
So we've got this product internally called Atlas, which have a project on Atlas. People can subscribe to this project and then weekly you send a tweet-sized update about your project. I was using that as a platform to communicate internally about this product and there were actually hundreds of people who ended up subscribing to this thing.

(01:31:54):
Every week when we were at the stage where we were trying to get the first version out to customers it was a weekly demo of the product and everything that we built. Show the momentum as much as possible. I was even saving features for one week to the next just to ... When I knew we were going to be on vacation, for example, just to have something to show this train that keeps moving, it keeps moving. You don't want to get in front of it.

(01:32:17):
But then what I needed to do is to balance that out with all the customer side of things. So when we started to put it in front of customers then it was snippets from customer conversations. No one is going to read a research report that takes 30 minutes to read. Everyone is happy to watch a three-minute snippet with four customers talking about something. So I was using that a lot every week by posting those out there and then sharing them widely on Slack to go, "This is what we learned. This is what this customer is facing in terms of problem with Jira. This is how we're solving it. This is them talking about it," that kind of stuff.

(01:32:48):
So I was publishing that there and then sending that everywhere on Slack. Those kinds of things are what give people a sense of velocity and speed, and no one wants to fuck with a high-speed train. You don't get in front of it. That doesn't help and you're going to look bad by doing that. So basically that ended up buying us the time that we needed to get out of this, I don't know how you call it, the ugly baby phase.

Lenny Rachitsky (01:33:13):
An ugly baby phase.

Tanguy Crusson (01:33:16):
So basically it helped us get out of this phase where we don't have anything to show for yet because what we're showing is based on the learnings we're trying to get and we're trying to do that with, "Here's some numbers, here's some demos, here's some user snippets." Doing that every week because people can consume bite-sized content every week. They just struggle with the stuff where you come in three, four months later and go, "This is what we have to show for."

Lenny Rachitsky (01:33:43):
Right. How long was that period before it got out of this ugly baby phase for you? When did people start to get like, "Oh wow, this might work"?

Tanguy Crusson (01:33:49):
Honestly, we had something dogfooding within two months, in the hands of the first lighthouse user within five months. We iterated on the alpha for maybe six months. We then entered a beta that lasted close to a year.

(01:34:06):
So I think at every step of the way people could see us going somewhere, and I think initially they judged, not the outcome. They judged the team a lot more than the outcome.

(01:34:22):
So there's all this talk of founder market fit and I think really that's what you need to be teasing out, which is, is it the right thing, going after the right problems? Then if they can answer yes in ways that you haven't thought about asking consistently week over week, it's enough. I think that's where we were up until the stage where we were able to give something to customers, but the first lighthouse user was five months in. So it didn't even matter whether it looked good or not because people could see, "Okay, that's what ... Oh, there's something there," right?

(01:34:51):
So I'm not sure if there's one precise moment where it happened. However, there was this one moment where we were like, "Okay, that's it. We're ready to go GA." One of the founders, Mike went, "No, you're not. That thing is ugly. I do not want to look at it. It needs to level up with the rest of the Atlassian design standards. Our customers have expectations from us on that front. Your stuff is functional, but it's way too early."

(01:35:19):
So we went and fixed it. Took us two, three months and then we were okay to go. But yeah, no, because we had point A, because we had this expectation set that it would take a while to get there and because we were able to show progress every week, we basically didn't really feel that moment where we don't know what to do with this because it's too early.

Lenny Rachitsky (01:35:42):
This design improvement phase, what I'm visualizing is you're this pirate that is invited to a nice dinner and you have to start cleaning up. You have to start looking good and become inter-society. It makes a lot of sense. 

(01:35:54):
Also, what you're describing makes me think again of this concept of, it's your job to keep the flame alive and help it spread within the organization. So you have this idea and you're just like, keep momentum going, keep the flame growing by sharing constant updates, sharing progress, make it very easy to consume with little snippets and videos. So there's a lot of great advice here.

(01:36:13):
So timeline-wise, interestingly what I'm hearing is it basically took a year from idea to alpha, something like that. Is that roughly right?

Tanguy Crusson (01:36:21):
Just like seven months ... No, five months to first alpha1 customer.

Lenny Rachitsky (01:36:26):
Okay.

Tanguy Crusson (01:36:27):
We stayed in alpha for six months.

Lenny Rachitsky (01:36:30):
Okay, got it. So through alpha about a year total. Many people are hearing this. On the one hand it would be like, "Of course, Atlassian has all these resources. They're going to spend a year on this idea that who knows is going to work out. It's so easy for them."

(01:36:43):
I imagine there was much pain and suffering and challenge along the way that happened that makes it not so easy. Is there something you could share by just the struggle to actually make this real just as a way to wrap up conversation, go back to therapy if there's anything you want to share?

Tanguy Crusson (01:36:58):
Yeah. Basically, it's pretty much what we talked about earlier with lots of processes that were not changed yet because we're at the very beginning of point A, and people still wanting us to chime in on the things that were important for their part of the organization where we would play a part later if we become successful.

(01:37:19):
So none of that stuff was just solved once and for all. It was just a constant process to play with that, but I think we managed to get out of these things pretty gracefully in the end and I think we gained some level of admiration for some teams from that and some found it a bit ... It's always interesting to see someone breaking the rules and getting away with it. I think it inspired some of the other founders to try and do that, which was pretty cool to see.

(01:37:46):
It's actually something I'd love to see more, hearing back from the customers I've been talking to about this in their company, rather than feel suffocated by the current processes and they don't feel like they can break the chains. So I'm hoping it inspires a few more teams to give it a go, really.

Lenny Rachitsky (01:38:09):
There's clearly more I want to learn about point A and how other companies do this incubation stuff. So this is a really good inspiration to dig deeper into those sorts of programs.

(01:38:18):
We've covered a lot of ground. We've talked about things that have worked and haven't worked, all kinds of therapy and pain, but also things that help you succeed and build amazing products. Is there anything else you want to share or leave listeners with before we get to a very exciting lightning round?

Tanguy Crusson (01:38:32):
Yeah. I would try to balance the point I just gave, which is it's hard so someone has to try. Always feel like you can push. I'd like to balance that a bit with be careful for yourself as well and make sure that you're doing this in an environment that's ready to welcome it.

(01:38:54):
So as I mentioned, I worked at Atlassian now for the past 10 years. Before that I used to work in banks, in heavily regulated industries, in a whole bunch of different areas where that kind of stuff was not okay. I could have tried to push, it would have not gone well at all. 

(01:39:15):
So I think I'm deeply convinced by the fact that we don't need so much top-down leadership. What we need is a lot of autonomous leaders, regardless of their position within the org, able to push for change, fighting for the right things, but you need to do that in an environment that's safe for you to do so. If it's not, I think it's okay to consider alternatives.

(01:39:37):
So in other words, don't feel like you're trapped. Right? You only have one work life. Do it in places where you really believe you can do amazing work and surrounded by people that you're excited to work with. Otherwise, I've been there before where it's possible to become cynical by the weight of the things that are not possible and ending up doubting your own ability to do stuff really. So it's a bit of a balance of push for the right things, but also watch after yourself and if the environment is not right, it's okay to change.

Lenny Rachitsky (01:40:09):
This is a really hot topic and common question in product management and I imagine other functions in product of just how much can actually change as an IC at a company. I hear all this advice about making change, changing culture, incubating stuff, innovating. How much can you actually make an impact versus, "Nothing's going to change. I should go work somewhere else"? Do you have any advice there? It sounds like basically you're saying there's oftentimes you have no impact on how the business and culture's going to work and you probably should go find a company like Atlassian that does learn how to incubate and innovate and think differently.

Tanguy Crusson (01:40:44):
Yeah. This one is a ... I'm not sure how to answer that really because I've worked with, consulted, worked for close to 50 companies. Atlassian is the first company I joined where I was at home from day one, challenged in the right way, but fuck, I can really choose my battles and go after them. Things are hard, but it's okay.

(01:41:09):
So I joined Atlassian. [inaudible 01:41:13] found the trampoline like that, but yeah, I would just go, not settle for status quo because you cannot be the only sane person in a room. At some point you will go insane. The environment will permeate on you. You are not this entity that is absolutely permeable to everything that happens around you. Everything around you will affect you and will change you as a person. I really believe that.

(01:41:36):
So you need to surround yourself with people and environments that can help bring out the best in you, otherwise you can turn bad. I myself have been cynical in the past working in environments that were cynical and I then decided it's not me. I do not want it to be me. It was me back then. I do not want it to be me.

(01:41:55):
So yeah, that's my only advice, which is have the courage to ask yourselves those questions because otherwise it might change you in ways you don't want to.

Lenny Rachitsky (01:42:07):
Amazing advice. Really important advice. With that we've reached our very exciting lightning round. Are you ready?

Tanguy Crusson (01:42:15):
I am, looking forward to it.

Lenny Rachitsky (01:42:17):
All right, here we go. First question, what are two or three books that you've recommended most to other people?

Tanguy Crusson (01:42:23):
Yeah, the first one was a book that was recommended to me by Scott Farquhar, founder of Atlassian co-founder. Who: A Method for Hiring is basically a book about how to do the thing that I for a while was really bad at, which is try to interview to understand who's going to be a good person, not a good person to join your team.

(01:42:44):
Second one, so that's one book about work. Two other books that are not about work. Highly recommend reading Hakim's Odyssey. It's the story of a Syrian refugee moving out of Syria, trying to move into Europe. We hear a lot of these stats and numbers about people trying to cross the Med Sea or basically become refugees in other countries and it's very easy to look at it complacently up until you meet a personal story. This personal story of Hakim that was told very beautifully by this illustrator is well worth a read on that front.

(01:43:19):
The last one is a book that I'm not sure has been translated from French. It's called Vivre avec la Terre, To Live with the Earth and it's about how we could build a different agricultural system to the one that we have today that might have better ways to feed us into the future that doesn't require large monoculture of vegetables that may not be as sustainable.

(01:43:47):
They managed to create a really efficient structure on very small parcels of land with a lot of species working together to control and not need the use of any pesticides and stuff like that. They've been always surrounded by teams of researchers from the, I think it's called the Inria. It's one of the French research centers, have got really amazing results, but I don't think many know that this stuff exists and that it could actually be used out there and I think that's a shame.

Lenny Rachitsky (01:44:14):
I think it's the first book that sounds recommended that's only in a different language, but may not be translated.

Tanguy Crusson (01:44:20):
It might be translated. I hope it is. It's pretty thick though and it's very technical. So I've read the principles bit and I would get lost in all the technical aspects of growing food, to be honest.

Lenny Rachitsky (01:44:26):
Okay, love it. So let's ask you your favorite interview question. What's your favorite interview question?

Tanguy Crusson (01:44:32):
Yeah. So I struggled a lot with interviewing and I've read all the standard interview questions there is out there and I've heard them in your podcast as well. There is one that came from this book that Scott Farquhar also told me was working really well for him is when people describe an experience, you ask them the name of the person that they worked with back then. And you ask them, "So when I call this person after our call, what do you think they're going to say about that?"

(01:45:02):
Apparently this does something and I've seen it happen where people are unable to project and invent on the spot something from the lens of another person talking about them. So they might be able to talk about, "I did this, I did that, I did that. So when I talk ... "Who was your boss? My boss was ... So when I ask this person, what do you think they're going to say?" It's like, "Ah, well actually, I was only leading a part of it and maybe you shouldn't call them because XYZ."

(01:45:33):
That part makes people all of a sudden go out of this scripted version they give of themselves and become more real for a second. You get a bit of the authenticity coming out, which often is very hard to get to for me in interview questions. I've seen it happen. I find that very funny to do now because people get really uneasy for a second and then you get to something real.

Lenny Rachitsky (01:45:57):
That is genius. Makes so much sense. Makes me wonder how I can integrate this tip into my podcast interviews. Really good tip. Next question, do you have a favorite product you've recently discovered that you really love?

Tanguy Crusson (01:46:08):
Yeah, it's got nothing with tech, nothing to do with tech. I'm kite surfing a lot at the moment and I came across hydrofoils, which is basically these things where there's an airplane underneath you on a mast which is connected to a board. You're on the board with your kite and you basically just fly over the water.

(01:46:32):
That invention is just brilliant. It's relatively easy to learn and I can spend basically, parts of my weekend flying over water in as much as a breeze of wind because there's absolutely zero friction between the board and the water. So that's, technically speaking I think is genius the way they created that and inspiring themselves from airplanes.

Lenny Rachitsky (01:46:52):
Is that the thing that Zuck was riding with his sunscreen with the flag or is that something else? I don't know if you saw that photo. Don't worry about it.

Tanguy Crusson (01:47:00):
No, I didn't see that.

Lenny Rachitsky (01:47:01):
I like that you say it's relatively easy to learn even though there's a kite on you pulling you in the water on this thing that's above the water. I don't know if I believe you.

Tanguy Crusson (01:47:11):
Yeah. I mean, there's sports and crafts that are difficult to learn. This one you can get comfortable in 18 months to two years, which is really, really short. It could be a sport that you would have done before.

Lenny Rachitsky (01:47:24):
Just a couple of years. Okay. I like your bar for ... I'm going to ask a question along these lines, but before we get there, do you have a favorite life motto that you often come back to, find useful in work or in life, maybe share with friends and family?

Tanguy Crusson (01:47:37):
I've got two, one for work and one for everything in life. The one for work is initially a quote from Obama. I can't remember the exact quote. I'm going to paraphrase, but let's keep it about the work. So there's going to be moments in your career where you don't feel valued and you wonder, "Am I doing the right thing? Am I being recognized? Am I valued? Am I at the right place?" Whenever that happens, a lot of parasitic thoughts may come in. You may face imposter syndrome and stuff like that. Happens to me super regularly. 

(01:48:09):
Whenever that happens, what I do is I remind myself, "Keep it about the work," because as long as you make it about the work there's always work to be done and there's always a path that emerges from that work. It's a bit of the same of this, you've got this thing in yoga where once you're committed good things will happen. Well, that's exactly what I've seen and that's helped me every time. I reread this quote whenever I'm in these moments of turmoil around me.

(01:48:37):
Now when I face those moments I also remind myself of the other one, which I invented, but I don't think I'm the only one who has invented that one, which is, "Remember that in 100 years we'll all be dead and forgotten. So don't take yourself too seriously. You're not that important. You're probably not that important, as important as you think for the people that you are arguing with."

(01:49:01):
That's also the beauty in all things, which is it has an end. In the end it probably doesn't matter so might as well give it your best shot. That's what the existentialists back in France many generations ago were talking about. This point is close to Albert Camus' thesis, right? "If it doesn't make sense might as well go for it."

Lenny Rachitsky (01:49:24):
Really good points, really good lessons, really good mottos. Final question, you were ranked number four worldwide in a form of free diving. First of all, can you briefly describe what is free diving and then can you share one thing that might surprise someone about the sport and the skill?

Tanguy Crusson (01:49:43):
Yeah. So yes, that's my claim to fame. I was ranked number four in basically, the distance you can swim in a swimming pool without fins with 167 meters, which is 550 feet.

Lenny Rachitsky (01:49:57):
And underwater?

Tanguy Crusson (01:49:59):
Underwater breaststroke. I went further with the monofin, the thing you see back there, but breaststroke was one meter away from the French record and ranking number four worldwide that year. The one I'm most proud of is I actually went to 300 feet underwater deep, came back in one piece and I really enjoyed the whole thing.

Lenny Rachitsky (01:50:20):
300 feet. That's like-

Tanguy Crusson (01:50:23):
92 meters.

Lenny Rachitsky (01:50:25):
Oh, geez. I'm trying to imagine what that is like compared to a Statue of Liberty or something like that, but I'll look that up later.

Tanguy Crusson (01:50:38):
I look at buildings one. Buildings can be as little as 20, 30 meters and can go super higher, but 90 meters is pretty high, yeah. Last time I looked at a building like that, I can't remember which one it was, but it's pretty high. So it's take one breath, go down, touch the bottom plate on the rope and then come back up.

(01:50:54):
One thing that may surprise people with this is that everyone is much more gifted at it than they think. So I used to give courses on the weekend for free diving and most people when I ask them, "Hey, how long do you think you can be underwater?" And they tell me something like 30 seconds, maybe a minute. "How deep you think can you go? Ah, maybe five meters."

(01:51:15):
At the end of the weekend most people were able to hold their breath for two to three minutes and to go to 20 meters deep. So it's one of those things where it looks absolutely impressive and crazy and amazing and in fact we're naturally gifted to it. There's a lot of physiological changes that happen when we dive that make it possible, but I think it's fascinating how little we know about our bodies.

Lenny Rachitsky (01:51:38):
I'm looking up what is 300 feet compared to real-life objects on perplexity. So what is 300 feet compared to real-life objects? Here we go, 300 feet. The length of a football field. Okay, yeah. I should have realized that. Close to the length of a Boeing 737.

Tanguy Crusson (01:52:00):
Yeah. You need to look at it this way to get some perspective. 

Lenny Rachitsky (01:52:01):
Yeah, and a football field-

Tanguy Crusson (01:52:01):
You go underwater in that-

Lenny Rachitsky (01:52:10):
... Jesus Christ. Oh, my God. But I love your advice that people can do much better at the skill than they think.

Tanguy Crusson (01:52:14):
Yeah. Everyone from kids to adults are really amazing at it actually.

Lenny Rachitsky (01:52:20):
Tanguy, we've covered so much ground. I think this is going to help a lot of people that are trying to get better at free diving, but also at building zero to one within large companies. I am so thankful that you made time for this and that you shared some into this real talk and as you called it, therapy.

(01:52:37):
Two final questions. Where can folks find you online if they want to reach out, maybe follow up on some of the stuff you talked about and how can listeners be useful to you?

Tanguy Crusson (01:52:44):
Yeah, so you can find me on LinkedIn if you know how to ... You don't need to know how to pronounce my name. You just need to know how to write it. I'm not super active on social media to be honest. I'm very much in the trenches building this product so I don't do much in terms of networking to be fair, but if you are using this product for example, and you have ideas for how we can improve it for you or you'd like to share some stories about how that's helped you or how it's not helping you, I'd love to connect because I spend a large part of my days talking to users, responding to support tickets and stuff like that. So, yeah.

Lenny Rachitsky (01:53:20):
Amazing. Tanguy, thank you so much for being here.

Tanguy Crusson (01:53:24):
Thank you, Lenny. Honestly, it's been amazing and I hope some of my gibberish is useful to people.

Lenny Rachitsky (01:53:31):
Definitely not gibberish. I think it's going to help a lot of people. With that, I'll let you go. Bye, everyone.

Tanguy Crusson (01:53:37):
Bye-bye.

Lenny Rachitsky (01:53:39):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

