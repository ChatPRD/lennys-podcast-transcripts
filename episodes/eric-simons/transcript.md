---
guest: Eric Simons
title: 'Inside Bolt: From near-death to one of the fastest-growing products in history
  | Eric Simons'
youtube_url: https://www.youtube.com/watch?v=L22DtAHLmzs
video_id: L22DtAHLmzs
description: 'Eric Simons is the founder and CEO of StackBlitz, the company behind
  Bolt—the #1 web-based AI coding agent and one of the fastest-growing products in
  history. After nearly shutting down,...

  '
duration_seconds: 5331.0
duration: '1:28:51'
view_count: 25333
channel: Lenny's Podcast
keywords:
- growth
- acquisition
- churn
- kpis
- roadmap
- prioritization
- experimentation
- analytics
- pricing
- monetization
- subscription
- revenue
- hiring
- management
- strategy
---

# Inside Bolt: From near-death to one of the fastest-growing products in history | Eric Simons

## Transcript

Lenny Rachitsky (00:00:00):
The rate you're growing is absurd. You're in this cohort of companies that are just growing at rates that we've never seen in the history of startups.

Eric Simons (00:00:05):
The company was on the verge of going under when we launched Bolt, and what ended up happening is, in the first two months it went from zero to 20 million of ARR. And we've already crossed 30 million of ARR, with the current rate we're on, our forecast for the year is we want to get to 100 million of ARR.

Lenny Rachitsky (00:00:22):
This is just non-stop wild shit. How is this possible? What has allowed you to grow this much, this fast, with such a small team?

Eric Simons (00:00:30):
Most importantly, it's been the people. It's rare to find startups where you have the core group of five, six, seven people that have been there for five years plus.

Lenny Rachitsky (00:00:38):
You basically were building a tech first, and then looking for a problem to solve later, which is often what people tell you not to do.

Eric Simons (00:00:44):
I think that's the hard thing about being an entrepreneur. There are periods of time where you have to make judgment calls that are not going to be the consensus view. You got to have confidence in your convictions on how to best play the hand.

Lenny Rachitsky (00:00:54):
A lot of people see these stats, and they sometimes don't see that there was also years and years of work before that.

Eric Simons (00:00:59):
It was kind of like, Bolt's this overnight success, seven years in the making.

Lenny Rachitsky (00:01:05):
Today my guest is Eric Simons. Eric is co-founder and CEO of StackBlitz, which makes a product called Bolt, which is currently neck and neck with Cursor for being the fastest growing product in history. They're currently the number one most popular web AI code app with over three million registered users. Two months after launching last October, they hit 20 million ARR. At the time of this recording, they're approaching 40 million ARR. The story of Bolt is wild. They actually started the company seven years ago, and were about to run out of money and shut down. But they realized the tech that they'd been building for the past seven years, called WebContainer, was perfectly suited for building AI products in a browser. So they launched the product with a tweet, and as Eric describes it, it was an overnight success seven years in the making. If you'd like to better understand the cutting edge of AI coding apps, and where things are going with AI and product building, this episode is a must listen.

(00:02:02):
If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. Also, if you become a yearly subscriber of my newsletter, you now get a year free of Perplexity Pro, Notion, Linear Granola, and Superhuman. Check it out at lennysnewsletter.com.

(00:02:18):
With that, I bring you Eric Simons.

(00:02:22):
This episode is brought to you by Eppo. Eppo is a next generation A-B testing and feature management platform built by alums of Airbnb and Snowflake for modern growth teams. Companies like Twitch, Miro, ClickUp, and DraftKings rely on Eppo to power their experiments. Experimentation is increasingly essential for driving growth, and for understanding the performance of new features, and Eppo helps you increase experimentation velocity while unlocking rigorous deep analysis, in a way that no other commercial tool does.

(00:02:52):
When I was at Airbnb, one of the things that I loved most was our experimentation platform where I could set up experiments, easily troubleshoot issues, and analyze performance all on my own. Eppo does all that and more, with advanced statistical methods that can help you shave weeks off experiment time, and accessible UI for diving deeper into performance, and out-of-the-box reporting that helps you avoid annoying, prolonged analytics cycles. Eppo also makes it easy for you to share experiment insights with your team, sparking new ideas for the A-B testing flywheel.

(00:03:21):
Eppo powers experimentation across every use case, including product, growth, machine learning, monetization, and email marketing. Check out Eppo at geteppo.com/lenny and 10x your experiment velocity. That's get E-P-P-O, .com slash lenny.

(00:03:41):
This episode is brought to you by the Fundrise Flagship fund. Full disclosure, real estate investing is boring. Prediction markets are exciting, meme coins are a thrill ride, even the stock market can swing wildly on a headline. Hello, Deep Zeke. But with real estate investing, there's no drama, or adrenaline, or excuses to refresh your portfolio every few minutes. Just bland and boring stuff like diversification and dividends, so you won't be surprised to learn that the Fundrise Flagship Real Estate Fund is a complete snooze fest. The fund holds $1.1 billion worth of institutional caliber real estate, managed by team of pros focused on steadily growing your net worth for decades to come. See? Boring.

(00:04:24):
That's the point. You can start investing in minutes, and with as little as $10 by visiting fundrise.com/lenny. Carefully consider the investment objectives, risks, charges, and expenses of the Fundrise Flagship Fund before investing. Find this information and more in the fund's prospectus at fundrise.com/flagship. This is a paid ad.

(00:04:49):
Eric, thank you so much for being here and welcome to the podcast.

Eric Simons (00:04:52):
Thank you for having me. Yeah, I'm stoked to be here.

Lenny Rachitsky (00:04:54):
For folks that are not super familiar with Bolt, what is Bolt?

Eric Simons (00:04:58):
It's really simple. You go there, there's a text box, and you tell it what you want to build. Whether it's a web or a mobile app, and so, it's kind of one of these text to app building tools that have become pretty popular over the past few months here. And it's not just building a static site, or something like that, but you can actually build full stack, real software with databases, and hosting and et cetera, just from prompting. And in a ridiculously short period of time, it's not like you're spending hours and hours or days, putting this together. You can get results in like, a minute.

Lenny Rachitsky (00:05:36):
Let's just share some numbers about the scale of what you're building. The rate you're growing is absurd. You're kind in this cohort of companies that are just growing at rates that we've never seen in the history of startups, and you guys are at the edge of that. Share some numbers about how things went when you launched, and where they're at today.

Eric Simons (00:05:53):
Yeah, when we launched, the company was on the verge of going under when we launched Bolt, our company StackBlitz. We'd been around for seven years building web-based development, environment stuff. And so when we launched this we were like, "This would be amazing if this added a 100K of ARR over the next couple of months." And what ended up happening is, in the first two months, we went from zero to 20 million of ARR. And I think we're on month four, or four and a half or something like that at this point, and we've already crossed 30 million of ARR, and we're on the verge of crossing 40. By the time this comes out, it appears that we're going to be at 40 million ARR. So it's just, the scale of the growth of the revenue has been nuts.

(00:06:41):
And of course, that correlates with insane user growth, as well. We've added three million registered users just in the past few months here, and monthly active users is around a million, I think at this point, per month. So it's just been... I've never seen anything, I've been doing startups for 15 years, I've never seen anything like this. Everyone I've talked to, our investors, or et cetera, there's not a lot of corollaries to what's going on here. And it's kind of extraordinary, because our company wasn't doing AI stuff six months ago. We had no AI products, and just out of nowhere we, from almost death of the company to being the number one buy traffic revenue, et cetera, like AI Cogen app, that's totally web-based, in the world. I think the only other startup ahead of us is for Cogen, just in general, would be Cursor, and the option revenue at this point.

(00:07:45):
And so anyways, it's been a heck of a ride. And our team's like 15, 20 people, so it's just dealing with, we're going to be closing on 100,000 customers, and our support team's like three people. So we're trying to scale as fast as we can. So it's just kind of mind-boggling, just the scale of the demand, and how we've had to turn things around to match the demand as best as we can.

Lenny Rachitsky (00:08:14):
Mind-boggling is an excellent way to describe what you just shared. A million monthly active users, you're at 40 million annual recurring revenue, five months into the business. Is that right?

Eric Simons (00:08:26):
Yeah, single digit. Yeah, single digit weeks. That's the current track rate that we're seeing for the thing. Yeah.

Lenny Rachitsky (00:08:33):
I think, are you guys are the fastest growing startup in history?

Eric Simons (00:08:37):
I mean, I think it depends on probably where you peg the number. Because yeah, we're here to just build great products, and just push the limits of what's possible with the technology. And I think that we do our jobs well, kind of crazy things can happen, but I mean, the current track rate we have, we're going to be exceeding the forecast for Q1 with the current rate we're on, and our forecast for the year is we want to get to 100 million of ARR. And now, I think there's been a couple, that would either be on par with Cursor, or ahead of them, or something like that.

(00:09:19):
And I think there's going to be more things like this, too. I don't think that... It just, there's something really, I think a lot of people are in disbelief about it too, where they're like, "This is, okay." And this is from when we were at, got to four million ARR, five million ARR in the first month. I would talk with people and they're like, "Okay, yeah, but that could go to zero." And then it went to 20 the next, "Ah, it could go to zero," but now we're closing on 40.

(00:09:40):
So from my view, I was also very skeptical, as this. I've never seen anything grow like this, right? And so part of me, for like a month I was kind of waking up waiting for the day where it just was like, "Okay, it's over." You know what I mean? This crazy thing happened, and now it's not. But that data just hasn't come. And you see this happening with Cursor, you see this with a lot of these other AI startups. And the value proposition is real. The free market is filled with rational actors. People are coming to these tools because it is solving problems, they're able to do way more for way less cost, than it would otherwise. And that's why I said, I think we're going to see more of this, whether it's in coding or other verticals, or whatever. In a sense, it's almost like maybe the new normal, as AI just continues to get better. But, anyways.

Lenny Rachitsky (00:10:41):
Let's get to a demo of Bolt, so people can actually see what this looks like in action. And as you go through it, if you can even point out stuff that is different from other products in the space, say Lovable, VZERO, Replit, that other folks have heard about, that'd be useful.

Eric Simons (00:10:57):
Awesome. Cool. Yeah, so this is Bolt, you just go to bolt.new. Things that I think are really interesting about Bolt. One is, it's just dead simple. Whether you're logged in or logged out, it's the same UI, it's extremely simple, it's just a text box. And I think that the biggest difference between Bolt and the other stuff out there, it's actually subtle. It's not like something you'd necessarily see in the UI, but it's how fast it is, and how reliable it is.

(00:11:23):
And this is because of how we are actually doing the compute, because what's going on here is when you type into, whether it's Bolt or another product, it has to spin up a dev environment to actually make that application. So there needs to be some operating system somewhere that's running it. Everyone else runs those things on cloud servers, which those can take minutes to boot up, and they often will run into issues, and then you can end up literally stuck and have to contact support to get it done, and get it unstuck.

(00:11:49):
With Bolt, and for the past seven years, what our company's been doing has been building an operating system that runs inside of your browser locally, using your CPU. So we have a very permissive free tier, and it's insanely fast, and it's insanely reliable.

(00:12:02):
So if I want to, just as a quick example of this say, "Make a clone of Spotify," and just hit enter. This thing's already getting to work, and already, on the right here, this is a full dev environment. This is an actual operating system, running inside of my browser. And I can run commands on it, et cetera. And really, what you're seeing down here, this terminal and kind of what's backing it, this is what took us really five, six, seven years to build, and make so reliable. There would not be a Bolt without this technology called WebContainer, that allows us to run an operating system in the browser.

(00:12:38):
Because what's going on here is, our AI agent for Bolt has bidirectional communication with this operating system. It's writing code, it's running the dev server for this thing, it's going to go ahead and spin this up. You can see how fast this is, in a matter of 60 seconds I said, "Make me a Spotify clone," and now we have one. And it looks pretty darn good.

Lenny Rachitsky (00:12:55):
That looks really good.

Eric Simons (00:12:58):
And that's one of the other aspects around Bolt is, this technology we made for the operating system side, the guys that have been working with us for the past five-plus years on it, before this they were actually doing machine learning AI stuff. And so when it came time to write the agent for Bolt, we had just an incredible amount of in-house expertise on how to actually merge these two different technology sets, to have this really reliable experience that produces really beautiful, really functional stuff. So that's based on what's really cool about the Bolt experience.

(00:13:32):
The other thing is, a lot of these products it's like, you can make something, but often you want to actually have a URL where you can share this. Having, maybe even attach a domain to it, or whatever have you. So with Bolt, we actually have built-in integrations with production grade hosting providers like Netlify, and for databases with Supabase.

(00:13:53):
So if I go and just click the deploy button here, this is actually going to run a production build of this project we made here. And again, this is doing this entirely inside of my browser, so it doesn't cost us anything to do this. So again, you can do this for free, and it has gone ahead and deployed this on a real URL, on Netlify. This is live, I can share this with anyone, and if I want to buy the domain spotifyclone.com, and point it at this, I can click this link here. That will kick me into Netlify, I can attach this to my account, buy a domain, point at that thing. And then from there on out, whenever I'm prompting Bolt to make changes to this application and hit deploy, that goes live on my public website.

(00:14:36):
So this is the simplest way to build a web app that's ever existed. That was one of the key realizations I had, a couple of weeks into the thing, I was seeing people use this for personal use cases. Like medical donation sites, or weddings, or whatever. And I was like, "Don't these people know that Wix or Squarespace exists? Should I tell them?" And then it hit me. Those things are so complicated to use. I don't know if you've ever seen just the UI of these things, but they're crazy complicated, and that's just for building a static website. There's no way you could actually build a functional app. And that's like, with Bolt, if we were to sit here for another 30 minutes, we would have streaming. You'd be able to make playlists of different MP3 files, or whatever. You can just keep prompting this thing to keep adding functionality.

(00:15:25):
So that's, I think, some of the cool core experience of both here. I can show you something cool that we just launched, if that would be of interest.

Lenny Rachitsky (00:15:32):
Let's do it.

Eric Simons (00:15:32):
So this is like web apps, right? Web apps are amazing, but often you want to have a native app. And it's hard to build web apps, it's even harder to build native apps, that can actually, that you can then go put in the app store. And so we partnered up with a company called Expo, and their entire business is making, basically, React Native tooling and this ecosystem that makes it super easy to build beautiful apps, and actually get them in the app store.

(00:15:57):
And so right here, I'll zoom in a little bit, we have this little, "Build a mobile app with Expo." So if you click that, we kind of instruct you on how to just prompt mobile apps into existence. So yeah, let's make another Spotify clone that's an actual native mobile app. Let's say, "Make a Spotify clone," go ahead and hit enter. And what this thing's going to do is actually, again, spin up a operating system here, where it's going to boot up the Expo tool chain and actually go and make a mobile app for us.

(00:16:28):
And what's cool about this is, we could actually preview it just in the browser here, but once this thing's done and it boots up, it's going to show a QR code, we're going to be able to scan it, and in real time actually basically have a test flight of this native application that we can try it on our phones, and as we keep prompting you'll see it making changes and stuff. This is kind of the first time that, you don't have to be technical to make production grade web, full-stack web and mobile apps. At this point I've done nothing that requires developer knowledge to do any of this stuff.

(00:17:10):
And I think that's what a lot of people are really excited about with this, and you know, the majority of our audience are people that are not developers, that are using this. They're PMs, they're designers, they're entrepreneurs. Because these are people that have always been great at building products, but previously, the only way that they could get their ideas into coded software was through a developer's fingertips. And now, they can deal with their own, through prompting.

(00:17:37):
So you can see here, we've got this little QR code. I'm going to go ahead and scan the thing.

Lenny Rachitsky (00:17:43):
I'm going to do it, too.

Eric Simons (00:17:43):
Cool.

Lenny Rachitsky (00:17:44):
By the way, I love that you had just enough things to say until it finished. That was pro.

Eric Simons (00:17:50):
Just as I planned, you know? So on my screen it's booting up, it's bundling the JavaScript of this thing, and it's beta. We just launched this last week, by the way. So if you can kind of see on my screen here, I actually have this Spotify looking app, right?

Lenny Rachitsky (00:18:07):
Wow.

Eric Simons (00:18:07):
That, you know.

Lenny Rachitsky (00:18:09):
That looks like, exactly like Spotify.

Eric Simons (00:18:11):
It looks exactly like Spotify, right?

Lenny Rachitsky (00:18:11):
It's good.

Eric Simons (00:18:11):
Yeah.

Lenny Rachitsky (00:18:14):
We're going to be sued right now, so let's be... You're doing too good a job with this. No, that's amazing.

Eric Simons (00:18:24):
Yeah. So it's pretty cool, right? And so what's cool is that, and as you keep prompting on your device, it'll just keep reloading. Without you having to kill the app, you can actually see the functionality getting added. And so, in this use case that you and I have right now, it's like if you and I were building an app together, we could be on other sides of the planet and you could actually be not just seeing a screenshot of the thing, but actually touching it and feeling it, and putting it through its paces.

(00:18:47):
And so a lot of product teams, I mean, this is just changing how people do product development. It's faster to do this than design a whole bunch of Figma frames, necessarily. Right? So.

Lenny Rachitsky (00:18:59):
We're going to spend a lot of time on that. Okay, this is incredible, this whole episode so far is you just blowing my mind and I imagine listeners' minds, just over and over and over. I don't even know where to go with all this, sometimes.

(00:19:09):
You made a really important point, that you worked on this for seven years before you launched Bolt. A lot of people see these stats, zero to 40 million ARR in five-ish months, and they sometimes don't see that there was also years and years of work before that. And the reason that you guys have been so successful is all the work you did that allowed, that built this WebContainer technology, it sounds like. Is there anything there that's worth sharing, you think, of just that part of the journey? I know we'll go through the origin that all, where Bolt came from, but I guess just that WebContainer component specifically. That feels like a huge deal.

Eric Simons (00:19:44):
A hundred percent it is, yeah. And I would say this is, surprisingly to me, it's still one of the contrarian viewpoints of our company. Because over the years it was like, when we first... And that, the WebContainer was the bet, that we made the company on. Just to be clear. StackBlitz was a browser-based, deep technology play on, "Can we make a web assembly based operating system that can boot in a browser, in like a hundred milliseconds, and run full on development tool chains?" That was really it.

(00:20:21):
And we'd gotten the idea for this, and the insight that this might be possible, because back when my co-founder and I came out to the Valley, he and I grew up down the street from each other in Chicago, we wrote code together at 13, and been building stuff ever since. And we came out to the Valley in 2012, and we just had the good fortune of bumping into Dylan Field and Evan Wallace when they were building Figma, in the early days. And that was, I don't think a lot of people know that Figma was also a browser-based deep technology play. Their first pitch for Figma, they didn't have a design tool. Their first pitch was this 3D ball dropping into water, inside of a browser town.

(00:21:00):
And the pitch basically was, "Browsers have this new capability called WebGL," the predecessor to WebAssembly, "and with these things, for the first time, you could actually create a graphics rendering engine, that you could then build a design tool on top of. But you're going to have to write that rendering engine from scratch, because nothing exists that can just compile into WebGL, or whatever. And if you want the performance you need, et cetera, it's going to take us years to do, but if we do it, we think this will change everything for design."

(00:21:35):
And obviously, we know how that story has panned out now. And back in 2017, 2016, 2017, Albert, my co-founder and I, saw the same sort of story begin to play out, but for web development and development environments. And specifically there was some stuff that landed in browsers like WebAssembly, shared memory, service workers, these different APIs. And we were like, "Oh, wow. It should be possible, theoretically, to write an operating system in WebAssembly that could run Node.js, and NPM and all the tool chains on top of it, that you need to do web development."

(00:22:12):
And that would be huge, because setting up developer environments, it's a pain for beginners. A lot of people churn out. The first thing you do when you learn how to code is not even learning how to code, it's how to set up your computer to even start writing the code. If you go join Netflix, or any of these other fan companies, the first month or two is you being onboarded, to run that stuff on your computer and set up your environment. And we're like, "If we could just have that be something, you click a link and it just boots in your browser, that'd be huge."

(00:22:42):
It's also, if you look at the other productivity apps that have really worked on the web, they've all had this compute model, right? Figma, when you open a Figma document, there's not like some cloud VM that gets spun up for you to render the documents. You're dragging things around. It's using your CPU and your memory to do the work. Same thing with Google Docs. That's the only model that's ever scaled to a billion users. And so, when you look at Cloud IDEs, like Cloud 9 was the first one, back in 2009 or so. The way these have always worked is that your browser's basically doing nothing, when you go to that. Every user that gets connected, there has to be a cloud VM that gets spun up for them, and then your browser's just taking your keystrokes, sending it to the server, and then sending back the results of it. And that's how all these other AI code, text to app sort of tools work. They're all using cloud VMs.

(00:23:34):
And the problem is, on a small scale it can work, but as you scale it up, I mean there's not even a 100 million VMs to rent, on the planet. But there are a billion devices that you can run this stuff on. Because that's kind of what we've seen with Bolt where, if you want to build a product that's going to be able to scale to that size, you have to look at all factors and go, "We have to build, make sure the technology provides the best experience, zero latency, transient cost." There's a permissive free tier, because the other problem with the server is, you end up, if you have a free tier, people are mining Bitcoin on it, they're DDoSing people using your servers. So inevitably, you have to nerf these things and roll them back. But if it's all done on the end device, it doesn't matter.

(00:24:18):
So anyways, WebContainer was the key piece, and what we struggled with, it took us four or five years or something, to build WebContainer. What we struggled with for the years after that was just how to build a product around it, because developers loved it, but they weren't using it in ways that they would pay money for. And as much as the nerd side of me wished that that would be enough, that it was like, building cool technology was enough. It's like, "It's not. We're here to build a venture scale company." And so that was kind of why we were high at the end of the journey, where it was like, we're taking shots on goal. And at some point, this got a connected bat, right?

Lenny Rachitsky (00:25:04):
There's a lot of really interesting lessons from this journey, that I think are counterintuitive. One is, you basically were building a tech first, and then looking for a problem to solve later. Which is often what people tell you not to do. And it worked out, in this case.

(00:25:19):
The other interesting takeaway here is, it feels like it's a similar moment to when AJAX came out and then everyone's just like, "Wow, you can build new things here." So it feels like there's a lesson here of just, "If there's a new technology that has enabled, something big that we think may, let's just work there for a while, and see if something comes up."

(00:25:35):
And then I think the other lesson here is just, as a founder, just survive as long as you can. Because you may find something that works.

Eric Simons (00:25:43):
All great points, all great points. Because you're dead right. And fortunately, my co-founder and I had, we had built a lot of unsuccessful stars before this. We spend most of the, or 20 times, churning through ideas on things. So when we had conviction, I was like, "This seems like a technology that will be important." It seems like, the web is the most ubiquitous... The pitch or the theory in our head was like, "The web is the most ubiquitous platform in the world, but yet it has no, you can't use the web to build the web."

(00:26:08):
Every other platform, Mac has Xcode. Windows has Visual Studio. The web had nothing. And we were like, "At a minimum, Google should probably buy this thing from us. It seems like it should probably be part of Chrome," at a minimum. And we thought, "Hey, this could be a huge enabler." The vision of just making it as easy to build full stack applications as using Canva, it just seemed really compelling.

(00:26:43):
But when you do that sort of risky deep technology play, you need to... And we were very good about this, like the previous company Albert and I did, we bootstrapped it all the way through to acquisition, so we understood and we were living hand-to-mouth, to bootstrap that thing. So we understood out of it how to have a low burn rate, and take a lot of shots on goal, and make every dollar stretch beyond what anyone would think is reasonable or possible. And that's how we played our hands with StackBlitz. We didn't raise money for the first two or three years of the company's life. We were bootstrapping it. When we did raise money, we barely spent it. Largely because it was like, "We need to just take a lot of smart bets, and it doesn't make sense."

(00:27:32):
And I would just say generally, until you see pull, just people pulling the product out of your hands, you don't want to be spending money. You should be like, default, no. And when you go and buy software, you should be going, "We're a tiny startup. Can you sell it for half?" Everything you buy, just keep the burn rate as low as possible, because you need as many shots on goal as you can possibly get. Because you have no idea. I think just generally, for startups, that's the right way in my view, to approach it. Unless you're seeing, again, immediate demand and pull, or whatever.

(00:28:02):
But yeah, I think that'd be, maybe the extra context I'd add on top is, I think that we ended up doing a good job of being extremely conservative. During a time in which, during 2020, through 2020 and 2021, which were times where exuberance and growing headcount was like, KPIs of companies. And were things that were being... With lot of emotional force of like, "Hey, you guys ought to be doing this." And I'm glad that we didn't heed the advice, because if we had tripled the company and kicked up the burn rate, there would be no Bolt. We would've gone out of business a lot of time ago.

(00:28:48):
So I think that's the hard thing about being an entrepreneur, I think is you kind of have to... There are periods of time where you have to make judgment calls that are not going to be the consensus view. Maybe years later, it'll become the consensus view, but you got to have confidence in your convictions on how to best play the hand.

Lenny Rachitsky (00:29:15):
There's so many great lessons here, I think just this idea of just staying alive. Dalton came on the podcast, he's a partner at YC Ones, and he just had this phrase, "Just don't die." And that's exactly what you guys did, seven years of just trying it until something worked, and I love that you actually were planning to shut down the company right before you launched Bolt. And I know you launched it with just a tweet, right? That was the launch moment?

Eric Simons (00:29:35):
Yep. Yeah.

Lenny Rachitsky (00:29:37):
Maybe talk about that moment of just, after launch, signs that, "Okay, this is working. Something's different."

Eric Simons (00:29:43):
Yeah, yeah. So day one it was like, there's great reception to the tweet. We were like, "Wow, this is one of the biggest things, launch day reception we've ever seen." And I think on the first day, I think we added 60K of ARR, or something. Which was like, I mean, crazy. Again, we were at 600, so we added 10% in a day. And I remember our dev ops engineer, he was the one who would flag me. He was like, "Guys, we got 60K today. This is crazy." And I was like, "Yeah, yeah. But this is launch day."

(00:30:12):
There's the tech crunch, peak of initiation, in the classic startup-

Lenny Rachitsky (00:30:17):
[Inaudible 00:30:17]-

Eric Simons (00:30:17):
... star, yeah. I was like, "Listen, guys." I'm trying to temper enthusiasm for the team. I'm like, "This is great. Got a lot of work to do." And then the next day we added 80K, or whatever it was, and it just kind of kept going. And all the while, the product we put out, we built a thing in 90 days. We built Bolt in 90. So there's a lot of things that were missing in the product. Like, basic stuff, basic stuff. And which, again, we cut the right corners on the thing to get it online, but we had this just growing influx of people using it, going, "How is there not a mobile responsive view? How are chat messages not," we got to 20 million of ARR without a mobile responsive view, by the way. Just throwing that out there. It was like the iPhone not having copy and paste until iPhone 5, or whatever. That was that, this was that for us, it was like, no mobile. You looked at it on mobile, it was terrible.

(00:31:13):
But there was stuff like that, so we had to just... And then, we're a small team and so, we were completely unprepared for just the growing traffic. And there was a whole bunch, I mean, the list of problems that were happening every single day was nuts. I mean, to start, we had never had a plan on stackblitz.com for more than $9.00. We had one price, nine bucks. And so when we launched Bolt we were like, "Again, we don't think, hopefully people like this, but nine bucks doesn't get you a lot of inference." And so people burn through nine bucks in 48 hours. And they're like, "I want to buy more. How do I buy more? Why won't you take my money?"

(00:31:56):
So it was like, within the week we rolled out just completely new pricing plans, where you could upgrade, which ended up, has kind of now become the standard. All the other guys in the space have copied this. Where prior to Bolt going online, Copilot, all these previous AI things, everyone wanted this Netflix model where there's one price, it's like all you can eat, or whatever. And the problem is, if you do that, you want the inference cost to be kind of low, because you're expecting people to use it a lot. And so you can't do these agentic experience things, it would be too expensive.

(00:32:29):
And what we ended up stumbling into is that, "Okay, actually, people are willing to pay more. People want to pay for more inference, because we've crossed this threshold where you can get a very tangible ROI." You know that this is providing a tremendous amount of value to you. So anyways, that was one thing, and the servers were just melting. Anthropic ran out of GPUs for us. Dario emailed me, he was like, "Listen, we don't have anything more to give you." At the times, where we're like, "How do we deal with..." It was just bananas, for weeks. It felt like in 300, when they're surrounded by 10,000 people, and our team is just doing everything. There's 15, 20 people, just doing everything. My chief of staff and I were doing customer support 95% of the day. Anyways.

(00:33:22):
So yeah, it was a crazy wild time. I mean, it still is. We've had a little bit more time to grow into this. And usually, I mean as a company, to grow into even 20 million ARR, you get a year at least or something, to kind of staff up.

Lenny Rachitsky (00:33:39):
Often, decades.

Eric Simons (00:33:40):
Yeah. So that was as hard, we'd go to people and kind of be like, "What do we do?" And the playbooks we get back are, take six months, or a year, or something. It's like, "This isn't going to work." Which is funny, this is what it's all about. I mean this is, at least for me, that level of intensity, it's challenging. Fun challenges, you know?

Lenny Rachitsky (00:34:08):
Wow, okay. This is just nonstop wild, wild shit. So you mentioned that your team was about 20 people through all of this, you guys are growing at this insane rate, 20 people. How was this possible? What has allowed you to grow this much, this fast, with such a small team? And this 300 visual is interesting, I imagine having these Spartans is a big part of it. Just what has allowed you to do this?

Eric Simons (00:34:40):
Yeah, I think a lot of it again, I mean if you kind of look at where a lot of the other folks, like the Cogen types of app space, have really been struggling, a lot of it has been scaling their servers with stuff. And it was kind of like both this overnight success, seven years in the making. All of this stuff, there's no way, if you rewind to year two, there's no way we could have, we would not be at the growth on DAUs, and revenue, or whatever. There's just no way. And so a lot of it is the technology we made, and most importantly, it's been the people.

(00:35:19):
The people... It's rare to find startups where you have the core group of five, six, seven people, that have been there for five years, plus. That's a pretty rare thing to see in Silicon Valley. It is usually, folks are at a startup for a year or two, they kind of go to another one. You know what I mean? And the problem with the turnover like that is that you can't take really long bets like the one we did. And so we've had, kind of from the get-go, again, this comes back from bootstrapping the previous company. Just having less people, and more context per head. That's just been how we do it, and we feel very strongly about it.

(00:36:00):
And the reason for that is, one, that you can have high levels of trust with anyone you're talking to, because you know that they have a lot of context. It's not like this person's completely in the dark, in some corner of the company that doesn't... You know what I mean? The second thing, everyone has agency to actually get stuff done, front to back. And there's no political community to get stuff approved by, there's no... So when you look at what happened with Bolt, I mean, we had engineers that were, front to back, were on a call with someone running into an issue, going and fixing it. Cooking up the UI on the spot, and landing this thing. Without involving anyone else on the team.

(00:36:41):
So I think it was the culmination of just high trust, and people, we all just have enjoyed working together in the past. Maybe that's why, that's the only reason that anyone would ever stay at a company for that long, or whatever. And so those sorts of stressful situations, I think, are make or break. Those are make or break for any team. And so, I think that what's happened is really, it is a direct reflection of the strength and the bonds of the people that are making this thing, and supporting the thing.

Lenny Rachitsky (00:37:22):
Yeah, I think that's such an important point, that you guys have been working together for many years. Most people won't have that benefit. When you're hiring people, when you hire this initial team, is there anything you look for that you think maybe people aren't looking for enough? Anything you prioritize when you're hiring new folks? Is it this idea that they can do a lot? They can do customer calls, they can do design, they can do engineering?

Eric Simons (00:37:42):
Yeah, for us, and even if the folks were hiring us, hiring people that don't care about the titles, and they don't care about... It's not like they're... People, of course it's people have a career trajectory, and that sort of thing, but they really are motivated by just working on cool things, and are chucking their ego at the door. And they're there to collectively build something great, not just kind of follow, and be the brilliant jerk. Most of the people that we've hired have been in Europe. We're a fully remote company. My co-founder and I are in the Bay Area. It's funny, back in 2018, we rented an office and stuff, and we were commuting into it. Because we thought we'd hire people here, and like a year into it we were like, "What are we doing? You and I are coming to an office for 10 people, we've hired, the people working for us are in Europe, or across the US." And we have one or two other people we've hired that are in the Bay Area at this point.

(00:38:51):
But yeah, I think we kind of look for folks that are intrinsically just trying to build great stuff, and are interested. And then the first people that we hired, the reason that we found them is that they were users of StackBlitz. A lot of people, the majority of people we've hired at the company have been people that actually came from our community, basically. So when we want to hire people, we put out a tweet and say, "Hey, we're hiring an engineer," and then we get DMs or whatever.

(00:39:22):
But yeah, those are the general kind of qualities we look for, though.

Lenny Rachitsky (00:39:28):
I'm excited to chat with Christina Gilbert, the founder of OneSchema, one of our long-time podcast sponsors. Hi, Christina.

Christina Gilbert (00:39:35):
Yes. Thank you for having me on, Lenny.

Lenny Rachitsky (00:39:37):
What is the latest with OneSchema? I know you now work with some of my favorite companies like Ramp, Vanta, Scale and Watershed. I heard that you just launched a new product to help product teams import CSVs from especially tricky systems like ERPs?

Christina Gilbert (00:39:53):
Yes, so we just launched OneSchema FileFeeds, which allows you to build an integration with any system in 15 minutes, as long as you can export a CSV to an SFTP folder. We see our customers all the time getting stuck with hacks, and workarounds, and the product teams that we work with don't have to turn down prospects because their systems are too hard to integrate with. We allow our customers to offer thousands of integrations without involving their engineering team at all.

Lenny Rachitsky (00:40:15):
I can tell you that if my team had to build integrations like this, how nice would it be to be able to take this off my roadmap, and instead use something like OneSchema. And not just to build it, but also to maintain it forever.

Christina Gilbert (00:40:26):
Absolutely, Lenny. We've heard so many horror stories of multi-day outages, from even just a handful of bad records. We are laser focused on integration reliability to help teams end all of those distractions that come up with integrations. We have a built-in validation layer that stops any bad data from entering your system, and OneSchema will notify your team immediately of any data that looks incorrect.

Lenny Rachitsky (00:40:46):
I know that importing incorrect data can cause all kinds of pain for your customers, and quickly lose their trust. Christina, thank you for joining us, and if you want to learn more head on over to oneschema.co, that's oneschema.co.

(00:41:01):
I want to ask a couple more questions about Bolt, and then I want to zoom out, and talk about where things are heading in the future. Let's talk about prioritization. I imagine you guys are just barraged with, as you described, after you launched, you're just barraged with requests. Like you said, there's a million monthly active users. I can't even imagine the feature requests you guys are getting, plus all the stuff you know want to build. Just how do you go about deciding what to prioritize, and what to actually build?

Eric Simons (00:41:28):
There's a lot of things that you just don't even know are possible to do, and so, people aren't going to be necessarily explicitly asking for them. And so there's been kind of a couple of these, where we use our gut instinct on like, "Hey, no one's asking for this, in meaningful numbers at least. But we think this is going to be a big deal."

(00:41:47):
Best example was last week with native mobile app support. That's, by reception, the biggest thing we've ever launched. And it was something that, even internally at the company, some folks were like, "This, I don't know. People are yelling about these other things." And it is, it's always this balance of how much are we just triaging various things, versus that new capabilities, but it was like, "This strikes me as an important one," where we put some chips into the middle of the table on. And had it dead right. It's just this mind-blowing experience, and now, there's just thousands of mobile apps being created a day, that weren't before. And how does that change things? I mean, now there's small businesses that, they would've never made an iPhone app before. It made no sense. It's super expensive. Now, that's not the case.

(00:42:43):
So there's kind of these things where it's like, "Hey, we should go and take bets here." But there's kind of this, I think the best analogy would be like, it's kind of like working at a restaurant, being like a chef. There's some amount of, there's feedback from the customers of, "This thing didn't taste good." And then there's like, "Hey, we've been cooking something interesting, and this tastes... I don't know. This, I think you're going to like this. I think this is a killer dish." And so you kind of have to balance those things.

(00:43:15):
And I think it's actually, largely, a function of just years of experience doing it. I think if you kind of rewound 10 years ago, I would have had really no, I wouldn't have had just the years of getting my butt kicked by the free market, to have cultivated a sense of this stuff. You kind of have to build your own gun and stick for it, I guess is the best way of putting it.

Lenny Rachitsky (00:43:39):
To unpack this a little bit further, do you have a cadence you guys work through to decide what to build, and ship? Do you have a weekly meeting every week? Because I know the answer is probably, really, "It's just chaos constantly, and fires we're putting out constantly." I know that's a lot of it, but is there some kind of process that you guys have for deciding what to build, and how to share it, and just work with the team?

Eric Simons (00:44:02):
We all meet every day. Pretty much the entire team gets on a call, and we just kind of front to back-

Lenny Rachitsky (00:44:07):
You meet, like a Zoom?

Eric Simons (00:44:08):
Yeah, every day at 8:00 AM Pacific, we're on a Zoom for at least an hour-

Lenny Rachitsky (00:44:12):
Every day? The whole company?

Eric Simons (00:44:13):
Pretty much the entire company. Yeah.

Lenny Rachitsky (00:44:14):
Wow. For an hour. Okay.

Eric Simons (00:44:16):
Yeah. And we just go over everything and I think we're going to probably start, as the team's kind of growing, we're going to start splintering off into different syncs, or whatever. But the thing about just having everyone in the same room every day is that, a lot of people will complain that it's... On Twitter, you'll see people say, "Oh, it's the most expensive use of everyone's time," but it's like, "Yep. But there's 0% fidelity loss in that. Everything, every day, is being audited front to back, and being discussed front to back."

(00:44:47):
So when you're in these times of just extreme growth, you want as close to 0% loss, on communications. And so that's how we've been doing it, especially since Bolt went online, and I think it was the week after Bolt went online we were like, "Every day, until we're through this or whatever, we're all getting on a phone call every day, and we're front to back doing this." And again, another reason why more context and less heads, every person at the company is aware of everything else going on at the company. So people can independently be making decisions that are generally, by default, more often correct than not.

Lenny Rachitsky (00:45:33):
That is so interesting. I've never heard that before. Especially for company growing, that is like yours. That is super interesting, that that's what you do.

Eric Simons (00:45:42):
I don't think we're going to do that forever.

Lenny Rachitsky (00:45:44):
Yeah, yeah. Of course.

Eric Simons (00:45:45):
But, yeah.

Lenny Rachitsky (00:45:47):
No, but I think that's a really cool thing to note, that that works. And has worked for you. Where do you, so say you talk about stuff, then where do you put stuff? Where do you put your roadmap? Where do you plan? Just, what tools are kind of in the stack of the company's toolset?

Eric Simons (00:46:01):
Yeah, on the engineering side, we use Linear heavily. On kind of product roadmapping, we're using Notion, and kind of making PRD type stuff in Notion. And we use Figma for design. No, actually, we use Bolt for a lot of design and prototyping at this point, as you can imagine. But yeah, I think that the tooling is nothing crazy. There's nothing crazy sophisticated. I think we'll be investing a lot more, and especially as you start splintering people out of being on the same call every day, so that's where this stuff really starts to matter. Because you don't have a time where you're able to dynamically catch things that weren't going to be brought up.

Lenny Rachitsky (00:46:45):
I love that you guys use PRDs. I love that you even used that term. There's a lot of talk of just like, "Oh, we got Bolt now we got all these tools, we don't need PRDs. We're just going to create a prototype immediately, and that's it." Talk about just why you still find that useful, and just what you put into your PRD, whatever that is for you.

Eric Simons (00:47:01):
Unless there's something that's very sophisticated that we're working on, we tend to keep them pretty light. I like to just have the minimal amount of context possible, that just ensures everyone's on the same page and that the key outcomes for whatever feature that we're working on, are going to be present when we get there. Because the things that, when these arguments get really beefy, you're looking at it at, "God, there's so much stuff to decipher." The problem is, a lot of people are going to gloss over it when it gets kicked to development, or design, or whatever. It's just going to start snowballing into a lot of stuff. It's just better to keep it as simple as you possibly can. At least, that's our approach to the thing. And often it's some of these things are like, "Here's a link to a Bolt."

Lenny Rachitsky (00:47:46):
"And here's what it might look like."

Eric Simons (00:47:51):
Yeah. And not just look like, "Here's kind of a working demo of what it will effectively feel like." And then, be. Because that just, if a picture is worth a thousand words, a live actual demo is worth millions. You can feel it. It's real. And that's what we're seeing, a lot of the businesses that are adopting Bolt now, that's the use case that they're using this for. Is high fidelity prototyping, because it's now faster to make real prototypes using Bolt. Before, it was too expensive. The idea of, "And let's prototype it, the engineers' code a proto..." It's like, that, it would take forever. It would be expensive. And now it's faster to do this with Bolt, in code, and have a real working software product, than dragging around frames and Figma to actually make a static version of it.

Lenny Rachitsky (00:48:43):
So let's actually talk about that. Just how far have companies gotten with Bolt? Prototypes is where everyone's kind of imagining these tools are at. I know that the goal isn't just to make prototypes, it's to build full scale. I imagine, long-term, Salesforce, Atlassian style companies, at scale. What are some examples of products people have built with Bolt that maybe would surprise people, in just how far they've gotten?

Eric Simons (00:49:08):
Yeah, I mean, especially... When you're starting greenfield stuff, you can use Bolt to build... you know. Like Salesforce, as an example. One of the first people that signed up for Bolt was this guy named Paul, and he's an entrepreneur, and doesn't know how to code. Built a CRM in three weeks, that has AI built into it and Stripe for billing, et cetera. He had gotten a quote from an agency for this, it was going to be 30 grand, and take six months. He had done in three weeks, and I think he spent 300 bucks on Bolt for the thing. So it's like, this is... And he's making money off of this. This is his start. Right?

Lenny Rachitsky (00:49:45):
Okay, so he built this, and he's selling it. People are paying to use it.

Eric Simons (00:49:48):
Yeah. Yeah.

Lenny Rachitsky (00:49:48):
Wow.

Eric Simons (00:49:50):
And there's many such cases of this. If you're looking at greenfield projects, 100%. Today with this current state of frontier models, you could absolutely build production grade software. You're not going to get a zero shot, but you're going to spend a couple of days, weeks, whatever. But the cost reduction there, 30 grand versus $300. It's 99% cheaper. Six months versus three weeks. I mean, it's like order of magnitude sort of fashioned delivery on the thing. And those numbers have helped, for the people that we talk to, that are building these full stack apps. People, they go to Upwork, work, they get a quote for five grand. They have it within 50 bucks. It's just nuts, what you're able to do with this thing.

(00:50:35):
And so I think on the flip side, a lot of the existing companies, there are very legitimate use cases where things are greenfield, spun up. A good example is public websites. Marketing pages, landing pages, whatever have you. Folks are adopting Bolt to just power those instead of using Webflow, for example. Because it's like, this is simpler to use than Webflow. And it integrates with the existing design system of the company, and et cetera. And the marketers can update it without knowing how to code, whatever. But then for product development teams, this is most commonly for, again, existing software businesses. They're using this to just accelerate the product development process, and in a way where it's not just like a Greenfield wholesale, "Hey, we're building the entire thing in Bolt," or whatever.

Lenny Rachitsky (00:51:20):
Can Bolt integrate with your existing code base, or not yet?

Eric Simons (00:51:23):
So yeah, we can actually open up repos in Bolt. You can go and use Bolt on your code base. It kind of depends on your setup. And we do have companies, again, that have marketing sites they're using this on, or their admin panel or whatever. And I think it's going to be a use case that we see a lot more people orienting towards. These LLMs are not great, depending on how big your application is, though. These things are not quite there, where if you have something that's a thousand files or something, or more, where you're going to be able to have a really reliable, super reliable experience per se. Within a year, we'll chat a year from now, I suspect the answer is going to be different. So it kind of depends on the size of the app, the scale of the app, and if it's too big, you're looking at the prototyping, just pure acceleration of product development. And if it's not, then you can just do it entirely from Bolt.

Lenny Rachitsky (00:52:24):
So this is useful. So what would you say are the major limitations of Bolt today, where people should just know, "Okay, it's not going to get you here yet. Maybe in the future it will." So it sounds like, if you have a really large existing code base, probably not the best tool yet. What else should people know?

Eric Simons (00:52:39):
I would say that's probably the main one, because I think if you have a large existing code base, you're going to need something like Cursor. And you're going to need to be a developer, meaningfully, to be editing that stuff. I think outside of that, there's a, just like using any other productivity tool, like Photoshop or Figma, or like a DSLR or whatever. There's some level of education, and using the tool, and learning how to use it, that's required to really unlock a lot of the maximum capabilities of the thing.

(00:53:10):
And the people that we see that are most successful with Bolt, outside of developers, the people we see that are most successful are people that are amazing PMs, for example. Because these are people that understand enough about how the technology works, typically, and their job is to direct developers on how to go and improve the product. And go and look into how to actually spec this thing out in a way that's executable, without lossiness in the communication. And when you think about, "Okay, how would you best interact with an AI developer agent?" It's basically that. You really want to be good at defining scope, and helping it go and debug various things, or whatever have you. There's a huge overlap of the skill set of being a rock star PM, and being really good at using, frankly, any of these text to apps or Cogen tools.

Lenny Rachitsky (00:54:08):
I love that you made that point. That's exactly the point I've been trying to make, I have a newsletter post about this. Because when all these tools came out, there was so many people saying, "Okay, PMs are dead. We don't need them anymore. We can just build things so quickly and easily, what's the point?" But I completely see the world the way you see it. The hard part now is, now it's easy to build the thing. Now it's, "What the hell should we build? Can we clearly articulate what it is we want to build?" And then, "Can we just have the taste to know, is this right, is this correct? Is this good? Is this going to solve the problem?" And then it's like, grow it, which is something also PMs think about. So, I completely agree. Basically it feels like PMs are, and a lot of PMs listen to this, so they'll love hearing this. To me, it feels like PMs are the best positioned role to thrive in this world.

Eric Simons (00:54:54):
Zero question. I mean that was, as Bolt was growing and we were like... Because we were a developer product before this, and so we expected the audience to be 100% developers that were using this. And we just kept seeing more and more and more people that were not developers using it, to the point where it's like, 67% of our users are not developers, at this point. And when I started talking to these folks, at first I was just weird, or whatever. It was like, "Well, what's going on here?" But then it just kind of clicked as like, "Oh, well, this is going to change everything. The entire software world order is going to get rewritten, here."

(00:55:30):
Because the way that companies are organized to build software today, totally going to change. The idea that again, PMs are the people that really understand, to the pixel level, what matters into making a great product experience. And often they're having... And listen, I'm a developer, myself. They have to go and harangue the developers to get things to be how they really ought to be, to the smallest levels. And now, how this is going to work, if you fast-forward one, two, five years, whatever. PMs, they're going to be "writing code", quote, unquote, instead of just writing a JIRA ticket and waiting for a developer to do it. The developers are going to be able to work on intellectually challenging tasks that LLMs are not well suited for, and still being augmented by LLMs to do it. But PMs are going to be able to go in and just make the changes themselves.

(00:56:24):
And what blew my mind is, it's not priced in, to any of these companies out there. And it's not reflected in the org charts of all the software companies in the world right now. That is going to completely change. The winners, at least, their org charts are going to completely change, and how they approach building products and shipping products. Completely. And it's starting, this is the beginning.

Lenny Rachitsky (00:56:50):
I want to follow that thread, but first of all, I want to also add, and correct me if you disagree with this. I think when we talk about PMs, that also applies to founders, like product thinking founders-

Eric Simons (00:56:58):
One hundred percent.

Lenny Rachitsky (00:56:59):
... very similar. And then, I think it's also important to note, if you also have engineering skills and design skills, you will be at an advantage. That only helps you. But if you're looking at this triangle of the triad of product, engineering, PM, it feels like the PME skills are the ones that will be most important and valuable. Although it'd be great if you can also be in code, and if you could also design really well.

Eric Simons (00:57:23):
Absolutely. And to me, it's the most exciting mix. I think PMs, designers and entrepreneurs that are non-technical, that's the most exciting thing to me, just because it's a brand new market that's being unlocked here. For the first time ever, these folks can directly code and build the product, themselves. Their vision, directly into the software itself. That's going to change everything. That is changing everything.

Lenny Rachitsky (00:57:48):
So when you talk about how org charts are going to change, what are you imagining there? Is it just fewer engineers, mostly, or what do the future org charts look like?

Eric Simons (00:57:57):
Good question. And I bet you there's going to be some Gartner analysis someday, years from now or whatever that's like, "Here's how the best," some term is applied to how the best companies are organizing. But yeah, I think that we're going to see developers probably being pulled off of a lot of the, generally speaking, pulled off of a lot of user interface type work. I would imagine. Except for the most complicated of those things. And you're going to see designers and PMs really, really leading the charge, and being responsible for crafting those experiences. And perhaps having a developer attached to be reviewing the code and making sure the guiding, the code that they're writing, reviewing those pull requests and et cetera. And I think maybe even the engineers are... Like you pointed out, having engineering skills is not going to hurt you. It's going to make you way more effective.

(00:58:58):
But I do think there's going to be, the leverage that the front engineer is going to have is, it is now insane, it's only going to get more so. And so I could see there just being fewer front engineers attached to, I'm seeing more product and design folks, with one or two engineers or something. And really having a larger matching of pods like that. Something like that strikes me as probably how this is going to start trending towards.

Lenny Rachitsky (00:59:34):
This touches on, we had a researcher from OpenAI in the podcast. She actually started her career, she worked at Anthropic first, as a front-end engineer. And said that once she saw what Clyde could do, for front-end engineering, she's like, "I need to move to a different function." And so she moved into research, because she saw that role disappearing, potentially. And that's exactly what you're saying.

Eric Simons (00:59:57):
Yep.

Lenny Rachitsky (00:59:57):
So let me ask you this, I don't know if you have a clear thesis on this yet, but say, you just had a kid. Say your kid is, in the future, starting school. Let's say your kid was starting college soon. Do you have thoughts on just what skills slash areas you think they should go into, versus avoid, that maybe are popular now and are going to be less popular?

Eric Simons (01:00:19):
Understanding how to leverage these AI tools is key. I wouldn't necessarily, I think maybe getting a basic understanding of how programming works, et cetera, is great.

Lenny Rachitsky (01:00:31):
It's like technical foundations, just understanding how systems work, how coding works.

Eric Simons (01:00:41):
Exactly. But it doesn't have to be, because I think back to if Bolt existed, like Albert and I say this to each other all the time. Since the get-go, StackBlitz, we've been building the thing that we wish we had when we were 13. And heck, for everything we built since then. And especially with Bolt. I mean, I don't know if I would've gone as deep as I did on learning how to code, and being an engineer, if that had been around then. The whole reason we got into it is we had ideas for products, and businesses, that we wanted to build. And coding was just a necessary requirement in order to do that.

(01:01:21):
And that said, I think people need to follow their intrinsic interests. If folks are really interested in really getting in the nitty-gritty of how computers work, and program leaders, or spark and compilers, or whatever, go for it. I think that stuff is still going to be relevant. I don't know if we're going to really have, we'll see, but to the degree that there's AGI where it's like, we don't have to think about anything ever again.

Lenny Rachitsky (01:01:47):
Yeah, that's always the answer here. Do we sell anything?

Eric Simons (01:01:50):
Yeah, it's like if we're at that point, it's kind of... I don't know, I'm not sure. But I think from, at least what I feel like seems like the next at least five years of what we're looking at, I think people are still going to, there's still going to be places to specialize, and really go deep. But I think you want to go into it with the idea, not like, "I'm going to go and learn computer science because I'm going to get a job for sure out of it."

(01:02:18):
I just think that's generally not a good... This is like, my co-founder and I, we didn't go to college. My co-founder dropped out of college after a semester or something, but I didn't go, because I was like, "We're coding," we were doing contracting at the time, making money. And it was like, "This is a lot of," you know, it would've been like a hundred grand of debt by the end of the thing, just for four years of in-state tuition, at U of I. 120 grand, I think, at that time.

(01:02:49):
And lo and behold, I mean there's a huge issue with this. Where people are kind of... There was a prevailing thought by society that going to college in the early 2010s or late two 2000s, that you're going to get a job on the other side. That's going to be high paying. And that just has not been the case for a lot of people. And I think that's just going to continue to be the case. But again, not to deter people from doing it, but you have to go into it being like, "I for sure, this is what I want, and I want to go and be the best that I can possibly be at this thing." You know what I mean?

Lenny Rachitsky (01:03:30):
I like the transfer to your kid is going to be like, "Don't even go to college," potentially.

Eric Simons (01:03:35):
Only if they want to. I think at 18, it's a huge ask. I mean, it's a huge ask, not even at 18. It's like at 17, because you could go apply for colleges. It's just such a huge... Like, a six figure debt commitment to someone who's making $0, or negative dollars, and that young. Unless you really have conviction, it costs nothing to go and explore and learn for free, online.

Lenny Rachitsky (01:04:03):
I want to come back to the skills that you think are going to be most important, and let me try to mirror back a few things you said, that I very much agree with.

(01:04:11):
So it feels like if you want to be successful in the world where AI can build things for you, more and more, what I'm hearing is get good at figuring out what people need and want, what problems they need solved. Get good at articulating it really well to the AI tools. And there's this talk, "You don't need to be a great prompt engineer. You don't need to work on prompting," but it feels like it's more and more important, because you tell it something and it goes off and builds a thing. If you're clear about it, it'll save you a lot of time.

(01:04:42):
So it's be good at figuring out problems people need solved, figure out how to articulate that problem well, and ask for a clear solution. Figure out how to grow the thing, feels like that's still going to be a need, because Bolt's not going to go and find every... I could see that still running paid ads, and stuff like that. But it feels like that's going to be ongoing need.

(01:05:03):
And then I feel like there's this kind of unstuck step, like helping AI get unstuck, and it feels like that's where maybe engineering skills will come in more and more. Thoughts on just that skill?

Eric Simons (01:05:13):
Oh, totally. Yeah. So we actually, two weeks ago I think, we announced this program called Bolt Builders. And it's basically the genius bar at the Apple Store, where as folks are building on Bolt that are not developers, they'll run into some nook or cranny where the AI just cannot figure it out, or whatever. And I think that's just going to continue to be the case for the time to come. That's our position, and that's why we spun up this program.

Lenny Rachitsky (01:05:38):
And these are humans, that help you out.

Eric Simons (01:05:41):
These are humans. And people that we're certifying. And so, in Bolt in the coming weeks or whatever, there's going to be a button where you can just say, "Hey, connect me with a certified expert." And you can chat with them live, and they'll help you get unstuck, and you pay I don't know, 50 bucks an hour. Whatever it is. And then you get unjammed and you keep prompting. And again, I just think this stuff is, it just all seems like gravy to me. Engineers get to focus on difficult challenges, not like cookie cutter, "Let's make another CRUD app," stuff. They get to, debugging is challenging, and fun. And going and working on intellectually stimulating tasks, and all this stuff that's just copy pasta, over and over, all this, error app. It's just like, let the AI do all that kind of crap.

Lenny Rachitsky (01:06:29):
This is a potentially new job, for now at least, just unstuck the AI. Which I think over time, it'll get better and better, and we maybe won't need these people. But I love that it's now AI first, and person second. Versus person building the thing, and then AI. Like when Copilot launched, it was just like, "Cool, here's a little suggestion for this function," and now it's flipped. "Here's everything." And then, "Oh, I don't know what to do here. Help us here." And then, it's like a human suggestion. Isn't that interesting? It's like, human Copilot is flipping it.

Eric Simons (01:06:58):
Totally. Yeah. That's what's wild is, I think Sonnet was really the first model that flipped the equation, because that was really us, and old Cursor, and all these other things. The rapid growth started the second Sonnet went online. We actually tried building Bolt almost exactly a year ago, with the frontier models at the time. Spent a week or two building it. It just didn't work. The output, the code output was not reliable enough. It would constantly, it would be a broken app, or it would look ugly, or whatever. And then we got a sneak peek of the Sonnet stuff in May and we were like, "Oh. Okay, we should take that project back off the shelf and green line it, because this might be it."

(01:07:36):
And lo and behold, that's exactly what has happened. But yeah, that's the big deal that is, kind of under the hood, this is... What's going on here is, a very critical threshold has been passed with LLM's ability to write production grade code and apps that actually look beautiful, and actually function well. It's not perfect, but there's kind of this zero to one moment that's happened where it's like, "Okay, so now, yeah. Now the AI is the first thing," and then you're kind of popping a developer in every now and then, versus the other way around.

Lenny Rachitsky (01:08:11):
I did not know that. I didn't realize that so much of this was unlocked with, like it's sitting on top of Anthropix work, and specifically Sonnet. That was the first model, you're saying, that could code well enough.

Eric Simons (01:08:22):
Yeah, zero question.

Lenny Rachitsky (01:08:24):
Wow.

Eric Simons (01:08:25):
Zero question. Absolutely.

Lenny Rachitsky (01:08:25):
That is fascinating. Just the amount of, I don't know, revenue and business and ecommerce that that one model has unlocked, is insane. I did not realize that.

Eric Simons (01:08:39):
It is. And in retrospect, I'd mentioned, we'd never done an AI product at StackBlitz, and it's tempting. Like when of ChatGPT went online, everyone started adding AI to their products. We just didn't see a clear place for a really added value. So I was not super bullish on, you know, a lot of people were like, "AGI is going to be here in 2023." You know what I mean? There's all this stuff that was being said, and I was like, "I just don't know if I necessarily buy how fast people say that it's going to move." And to a certain degree, that was the correct view.

(01:09:13):
What I didn't really think about though, is if AI, if LLMs are going to get better at a specific vertical, which are going to be the things that it would be. And if you look at law, for example, you want to make the best LLM for looking at case law. The problem with that stuff is, it's not deterministic. The judge's ruling is dependent on society's view of things at the time, political stuff going on, the jury. There's a ton of things, that it's not deterministic. And so you can't really create a lot of training data that's going to be super reliable, and produce really good results. And you can't just make up cases and say, "Theoretically, the judge would say this." Because, I mean, it just doesn't work.

(01:09:57):
Software is deterministic. When you write code and you hit run, it either runs or it doesn't. And that's the key insight Anthropic really had. They just went deep. And then, this is what they're doing, is just reinforcement learning on basically permutating every type of app you could ever build, and just spinning up tens of thousands of cores or whatever to do that. Just building tons of training data, and doing reinforcement learning, and making their LLMs the best in the world at building beautiful, reliable applications. I'm extremely bullish. It makes technical sense why, of anything, LLMs are going to get insanely better at writing code than probably most other types of applications for LLMs. Simply because it's something that can be extremely deterministic, and permutated thousands and thousands and thousands of times per second.

(01:10:54):
And so I think the broader trend here is... And Sonnet has woken everyone up. Google, and Open AI, all the... Everyone is now gunning for coding because, how big is the market opportunity to rewrite the software world order? It's trillions of dollars, or something, right? The world runs on software. So I think that just in a macro, the highest macro view, and why we went and raised money for Bolt. This seems like an extremely clear shot, there's this, you can kind of separate the hype of what people say and blah, blah, blah. When you break it down technically, this makes sense. It makes sense what's going to happen here. And for us, we're like, we are so happy to be well positioned to go and enable people to kind of ride this wave of the innovation that is here in LLMs, and is going to just keep coming, and therefore enable more people to build even crazier amazing software. So that's our world view, at least, of what's going on here at the macro.

Lenny Rachitsky (01:12:05):
And when did Sonnet even come out? It's been a while, right?

Eric Simons (01:12:08):
I think they officially, I think it was in June, when they officially put it online.

Lenny Rachitsky (01:12:12):
So since June, this is the worst it will ever be, the state of AI coding. And it's already this good. And there hasn't been anything, like they haven't launched their new model, since last June. So this tells us just how quickly things are going to start moving once they launch their next model. And as you said, everyone's gunning now for this, because they realized "We're behind on the coding piece." So, wow. This is going to get crazy.

Eric Simons (01:12:40):
I agree. Yeah, it's been, again, there was no blog post that laid all of this out for us. It's just been kind of this-

Lenny Rachitsky (01:12:48):
You just noticed the code was really good, basically.

Eric Simons (01:12:50):
And from there, it's just, we've been piecing together all this other stuff. So it's been kind of the thrill of a murder mystery of, "What is going on here?"

Lenny Rachitsky (01:12:59):
Oh, really.

Eric Simons (01:13:00):
Yeah. You know what I mean?

Lenny Rachitsky (01:13:01):
Just piecing together what you've seen on Anthropic releasing, is that what you mean? What have you been noticing, murder mystery-wise?

Eric Simons (01:13:06):
Well, and then the impacts of Bolt, where we have people that are not technical using this. How are they using it? Why are they doing this? And then, all the stuff we've talked about in this podcast has been the result of nine months of just R&D and seeing the results of it, and then going, "What?" And then digging in, doing another thing and then going, "What," again. And then it just keeps happening, because there's no charted course for this.

Lenny Rachitsky (01:13:31):
It's like an anthropology, if that's the right term, of just watching. It's like an emergent discovery, it sounds like. Versus you had the strategy, "Here, we're going to do this," where a persona to launch this thing will happen?

Eric Simons (01:13:42):
Yeah, a hundred percent. Yeah. I think that that's the best way to put it. It's the best way to put it. It's exactly that. And so it's very interesting to just-

Lenny Rachitsky (01:13:54):
To watch, and be a part of it, I imagine.

Eric Simons (01:13:56):
Yeah, yeah.

Lenny Rachitsky (01:13:57):
And I think as people say, "Okay, these are just toys, they're prototypes, it's not going to work with your existing code, it's not going to scale." It's important to note just what we talked about. This is a model from last June that this is possible on, and everybody's working on the next cutting edge model that will make this even better, and that's going to come real soon. Okay. Amazing.

(01:14:20):
I just have a few more questions to close out this conversation. One is just, what is coming next for Bolt? What are some of the cool new features that'll be launching before this comes out? Maybe right after this comes out, maybe in mid-March?

Eric Simons (01:14:33):
Yeah. Okay. So by the time, and I'm going to go back and tell our engineers, "I said this on this podcast-"

Lenny Rachitsky (01:14:33):
"I've committed. Sorry, guys."

Eric Simons (01:14:40):
This is, I found actually being a leaky faucet on talking on podcasts and stuff, my engineer is like, "How could you tell them..." "You just have to ship it faster, now. You got to make it real," right?

Lenny Rachitsky (01:14:49):
Or we'll get AI on it.

Eric Simons (01:14:52):
No, no. Yeah. But I think for us it's like, again, we've seen a lot of PMs, designers, entrepreneurs, et cetera, using Bolt. And so, we're really looking at better fitting with the tools that folks are using to do those things today. Bolt's not going to replace them, or something. And if you're working at a company, how do you integrate this stuff with your existing business, or your existing product and code base? Because that's the question we often get from people is, "How do I open my," like we're talking to one of the fan companies the other day, and like, "How do we open our production code base in this, that's like 20 years old?" I'm like, "You don't. None of this stuff. That's not what you do. This is for rapid product development in your use case."

(01:15:41):
So the features that we're going to be shipping, I'm pretty stoked about this one, so we've been working on this for a while and we've partnered up with a company called Anima to do this. But basically, so on any Figma URL, when you're looking at a design that you've made, if you just put bolt.new in front of that URL and hit enter, it's going to suck that design into Bolt, and turn it into a full stack app or mobile app, just out of the box.

Lenny Rachitsky (01:16:08):
That is genius.

Eric Simons (01:16:09):
Yeah. It's-

Lenny Rachitsky (01:16:09):
Amazing.

Eric Simons (01:16:10):
It's going to be nuts. Yeah, I mean, it's really fun to use. Because whether you're a developer or designer, or whatever, going and taking that and turning it into an actual coded app. And the thing is, once it's in Bolt, you can just keep prompting from there. You're like, "Yeah, well, add another page here." So you can have things that, where you want pixel perfect design, you can have it, and it'll translate one to one. And it's splitting out the assets. Anima's been doing this since 2017, Figma to code. They've got the best agent in the world for, they're the number one Figma plug-in, or whatever. And so in Bolt, it's going to just work. It's just deeply integrated

Lenny Rachitsky (01:16:53):
So it's bolt.new slash, the Figma URL, to the design.

Eric Simons (01:16:56):
Yep. That's all you got to do.

Lenny Rachitsky (01:16:56):
Amazing.

Eric Simons (01:16:57):
And in Bolt, we're going to also have a little Figma icon in the chat thing. So if you go to Bolt itself, you can click it and then paste the URL, or whatever. But yeah, but it's like that. It's from Figma to full stack app in a click. Literally. That's crazy. So that one's pretty cool.

(01:17:15):
And then the other one that we're working on is an integration with Slack, because often when you're talking about Figmas, like Figma links or whatever, at a company, you're in Slack or whatever. So you're having conversations about, "Hey, we should really add a page to this that does da-da-da." And so we're actually creating a Bolt Slack bot whose job is to basically act like a developer on your team. And so you can be, in a thread, you can be like, "Hey, I think we should a homepage." "Yeah, okay. @Bolt, can you whip this up real quick?" And it'll go and just suck down the entire conversation history so far in your Slack, on the thread or whatever.

(01:17:54):
You'll be like, "Okay, cool. So you kind of want me to take this Figma URL, which I can convert automatically," thanks to the future I just mentioned right before this. "I can just go and convert that thing out of the box, and then you want me to add a page to it, and then do this thing. Got it. I'm going to go do that. Oh, here's the URL where you can open it up and keep prompting." You know what I mean? So it's like having a developer or somebody to kind of kick this thing out. And you're just like, "Go make this thing real quick."

(01:18:15):
So those two things, I think it's, again. You start think about how our company's going to change how they're currently doing product development. And even just like, "Hey, we need to spin up a marketing site. Here's the thing." We're like, "Can you do that, Bolt?" "Yep. Let me go do that." You know what I mean? And that's why I'm kind of excited about those two, in particular, because I think it's going to be well received, and folks are going to be stoked about it. I hope. Knock on wood.

Lenny Rachitsky (01:18:40):
Those are awesome features. I love the Slack piece, because when I think about agents, there's always talk about agents. To me the simplest way to understand it is just a Slack bot, just that AI can talk to you like they're a person in Slack. And I love that's exactly what you're doing. And this is this gigantic feature of just like, "Hey, you just have this engineer now that can go build stuff for you."

(01:18:59):
Let me actually ask you a question along these lines, that I was meaning to ask, but I forgot. Is just, your engineering team, what are they using to build Bolt? I imagine it's a lot of Cursor. How much is Bolt, at this point, involved in building Bolt? And is there any other tools that they found useful, find useful, that are worth highlighting?

Eric Simons (01:19:18):
Yeah, good question. Yeah, we definitely use Cursor. Our folks use Cursor a lot. We use Bolt a lot for the product development process, like a ton, we're using it. And we're doing basically the flow that I described, where if things that need to be Pixel perfect, we're going to Figma for. And often we're taking that and we're pulling that into Bolt, because we've got access to the integration today. So pull that into Bolt and we're saying, "Hey, go add these things or whatever." Or just saying, "Hey, here's a screenshot of our UI, go do da-da-da."

(01:19:47):
Other AI tools that the developers are using. I think those are the primary ones. I mean, I think we've got a subscription to Claude, and ChatGPT, and things like that. But I think for development, Cursor is the main thing,

Lenny Rachitsky (01:20:03):
Yeah, it's cool how few tools, like there's so many AI tools, and it's interesting how few people actually end up using. It's like Cursor, Claude, ChatGPT, and then maybe another tool. Like Bolt.

Eric Simons (01:20:13):
Yeah. Totally.

Lenny Rachitsky (01:20:14):
Okay. Final-ish question. Say somebody is opening up Bolt for the first time. What's something that, imagine you could sit next to every new user that's just trying Bolt for the first time, and you could whisper a tip in their ear to be successful with Bolt. What would that tip be?

Eric Simons (01:20:33):
And this is like, because we have a lot of different types of users. I imagine you're talking about PMs or designers, and that sort of-

Lenny Rachitsky (01:20:39):
Let's do PMs. That's a good one. That's a lot of the audience here.

Eric Simons (01:20:41):
I would say, talk to this thing like you do a Linear ticket, or a JIRA ticket. That would be my advice. And talk to this like you would, like you're talking to one of the developers on your team. And what that means is, be specific on things that matter. And on things where, also, you can let it be creative. You can go to and just say, "Hey, make it prettier." And it does a good job, it actually does a really good job, when you give it just, vibes. So anyway, I think for PMs it's like, you have the skillset. You know how to do this. This is, just think of this as your coworker, your developer coworker.

Lenny Rachitsky (01:21:24):
I love that. Because these tools are so easy, you just go in and it's like tell it a thing, and then, cool. You have a website. It's coded, boom, done. And what I'm hearing here is, take a little time to craft your ask. It may be tempting to just start, "Cool. Build me a serum," and then you're stuck with that first version. And then you're like, "Oh, well, okay. I didn't mean that." So it sounds like your advice is take some time to craft the ask, and be clear about what you want.

Eric Simons (01:21:49):
Yeah, totally. Especially if you have a clear vision of what you're trying to build. And something reasonably sophisticated. And what I recommend everyone to do, if it's your first time trying Bolt and you're like, "What should I have it do, and I don't have an idea"? Tell it to build you a personal website. There's something like magic. You take your LinkedIn copy, and paste your LinkedIn bio and work experience, just like select text, copy, paste it. "I need a website, my name is so-and-so, here's my LinkedIn history. My favorite color is blue, and I like dogs." And then hit paste, right?

Lenny Rachitsky (01:21:49):
"Make it prettier."

Eric Simons (01:22:24):
[inaudible 01:22:24] actor. Yeah. And then, you know what I mean? And then you can hit deploy. And if you don't have a .com yet, now you can. Right? I mean, now you have a real, personalized service. I think there's kind of a moment around that where it's like, "Oh, okay, wow. This," it's zero shot, zero shot 99.999% of the time. You're getting a beautiful personal website that you didn't have before, that would've taken you an hour, on Wix. If not more. And that gives you the taste of, "Oh, okay, cool. So if I really take the time to think this through, and make a PRD, and then put that in piece by piece into this thing, the sky's the limit."

Lenny Rachitsky (01:22:55):
Eric, this has been just insane on so many levels. I have so much to process, I think a lot of listeners do too. Maybe as an actual final question, I saw this story about how when you were starting StackBlitz, or maybe even before StackBlitz, you squatted in the AOL office. Because you had some badge that still worked. Maybe just tell that story.

Eric Simons (01:23:18):
Yeah, that was the thing I was most known for. That happened like 2012, and I was 19 years old, so it's been a very long time. I think I'm 33, now or something.

Lenny Rachitsky (01:23:27):
The statutes of limitations are expended.

Eric Simons (01:23:30):
Yeah, yeah, exactly. But yeah, for a while I was like, "I have to do something more notable than living at AOL. This can't be what I'm known for." But now people are like, "Oh, wait. You're the StackBlitz guy, and you're the AOL guy?"

(01:23:43):
So when I first came out to Silicon Valley, we got into a, I was building a K12 education startup at the time, and this is back during the days where Y Combinator, they only gave you like 20 grand, and so there was this offshoot of Y Combinator called Imagine K12, it was Jeff Ralston who, I think he was CEO of YC a couple of years back. And then Imagine K12 merged into Y Combinator a couple of years after Rob went through it, but anyways, they had an office space at AOL. At the time, AOL was trying to reinvigorate the company and they were like, "Hey, we should get young startup blood in here, so let's rent out office space to teenagers," basically.

(01:24:24):
So I was there, and we ended up running out of money. 20 grand doesn't go very far in the Valley, so three or four months in, we were like, "Oh God, what do we do?" And I was going to the AOL office multiple times a week, because we had access cards to get in to get to the investors' offices. And I realized, I was like, "You know, they have couches here, and they have food. There's ramen that you can microwave, and there's a gym where there's a shower, and even you can do laundry." And then, so I was like, "I don't know, maybe while I figure this out, I'll just live out of here." And so that's what I ended up doing for, I think, four or five months. I was living out of this headquarters over on Page Mill in El Camino, in Palo Alto.

(01:25:12):
And then, I got away with it for a while just because the guards, the security guards, they worked 12-hour shifts. And so the guys that, when I was there at night... And I was coding, all day every day, basically. So the guys at night just were like, "Dang, this guy works really hard." And then in the morning they'd be like, "Wow, this guy is working really hard." And I became friends with some of them, and then eventually, I think there were also a whole bunch of Stanford students that I think they put bunks in one of the aisles. It was just started getting out control, so I think they started cracking down. And then one morning, at like 4:00 in the morning, a guard came in and threw me out.

(01:25:52):
I'm from Chicago. I don't know anyone. At that point I'm like, "I know no one in the Bay Area." So I went to a Starbucks, which was not open. I slept on the table outside of the thing. And I think I hit up one of the other entrepreneurs that was in the program. I was like, "Do you have a couch? I think I kind of need it, at this point." Yeah, the press got wind of it, and it was this worldwide story. But I lived on a dollar a day. That was the crazy thing. My burn rate was a dollar a day, at that time.

Lenny Rachitsky (01:26:22):
What did you use that dollar for?

Eric Simons (01:26:25):
This is back when McDonald's had the Dollar Menu. Literally. So it was like, I occasionally would go and get a cheeseburger or whatever. Yeah, it was ultimate scrappiness.

Lenny Rachitsky (01:26:41):
You're technically homeless. From homeless, to one of the fastest growing startups in history. Eric, what a journey. This is such an interesting point in time of your life, and of just tech. No matter what happens, I'm sure you'll be extremely successful, but it's such an interesting just point in that journey. And I'm thankful that you made time to share it with us.

Eric Simons (01:27:01):
It's always good to just have the perspective of, you should start companies to keep the mindset that you're doing it to have fun. So, stoked to see where this goes, one way or the other. It's going to be interesting.

Lenny Rachitsky (01:27:16):
Eric, final questions. Where can folks find online if they want to reach out, maybe follow up on some stuff you shared, and how can listeners be useful to you?

Eric Simons (01:27:23):
Yeah, totally. I mean, yeah, so bolt.new is the website, over on Twitter, I'm @ericsimons40 on Twitter, and I think our Twitter account is @boltdotnew, not with a period. It's like, B-O-L-T-D-O-T-N-E-W. And yeah, I'm curious to hear what folks think. I mean, this is, again, we are learning so much from the people that are coming and trying this thing out and giving their feedback. And within the first meeting of it going online, we were not the experts on how use the tool anymore, and it's been that way ever since. And so, I love hearing from folks on what they want to see next, and how this is helping them. And where they run into problems, like where we need to go and fix things. So my email address is Eric@stackblitz.com. That's Eric with a C. So I'd love to hear from anyone, whether it's a DM on Twitter, or an email.

Lenny Rachitsky (01:28:18):
Amazing. Eric, thank you so much for being here.

Eric Simons (01:28:21):
Awesome. Thank you so much for having me. This is a blast.

Lenny Rachitsky (01:28:23):
Bye, everyone.

(01:28:26):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review, as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com.

(01:28:46):
See you in the next episode.

