Conrad Woltge  [3:38 PM]
@gknob thanks for putting together the great view on use cases and success rates for EPA.
epa-status-report-latest
3 asks to you, gilles:

please make the report accessible for everyone in p42 (atm access seems to be quite tight)
start reaching out to customers on our customer slack to understand their use cases and look for potential co-inno
help other agent teams to setup the same report
2 asks to @agent-owners

create a similar report for your agent
start reaching out to customers on our customer slack to understand their use cases and look for potential co-inno
cc: @lebescon @eckersle
3 repliesBertrand de Coatpont  [3:43 PM]
@pedrofer :up-arrow:
Gilles Knobloch  [6:56 PM]
@conradw, thanks for the feedback

please make the report accessible for everyone in p42 (atm access seems to be quite tight)https://adobe.sharepoint.com/:u:/s/ExperienceProductionAgent/IQDlssqLun_GTKlWHTW9R6uzATVcCyF51geTS7jmPfhan90 is a link I shared earlier that should work for All Adobe

start reaching out to customers on our customer slack to understand their use cases and look for potential co-innoYes, this is something we started to do

When they reached what we call success (in case of content updater, they accepted the change - found 2 customers today)
When they dropped after being presented a preview, that they didn't accept
As you know, not always easy to extract their email addresses nor have them engage on Slack/Teams - I wonder if anyone ever looked at value realization of our communication channels (Gut feeling is <10% of customers engage - of course when they do, they get a lot of value)

help other agent teams to setup the same reportI have a Claude skill for that - aem-agent-report.skill
Honestly, started a bit with the idea that "a report is better than no report", now digging a bit more into what's the right structure and how do we leverage it
Talked with @cdulimba today about what it could be, looking for feedback

Executive Summary
Some key KPIs for last week, how they evolved compared to previous week - focus on external customers (internal comes later in the report)
External Interactions
External Customers
External Users
% having Value Realization (instead of Technical Success today)
New users
Repeated users - used the tool in last 4(?) weeks

A section like today with key insights - Good... but need to define what makes sense there, adding some hints in the skill
Signals
Watch
Action Needed


Split by Capabilities/Job, for last week
Pie chart with # of interactions
Pie chart with # of customers
Pie chart with # of users

Funnels per Capability
Capability = Content Update, Content Creation, Forms Creation, etc.
Different funnels
# of interactions (?), # of customers, # of users
Split Internal vs. External
Evolution compared to previous week

How many used
How many had technical success
Analyze of the drop

How many had value realization
Analyze of the drop


Customer Journeys per Capability
What did they try to do (for instance update page, update fragment, etc.)
Extract patterns
Show sample prompts (collapsed)
Focus on Top 10 customers


Weekly trends
Might move to monthly later, could focus on last 6 weeks
From a table today to bar/line charts
# of interactions - internal vs. external
# of customers - internal vs. external
# of users - internal vs. external
users retention
technical success rate
value realization rate


Other sections could be removed for now
External Customers Spotlight - would already be part of Customer Journeys / Top 10
Overview & KPIs - key stuff is reported in exec summary
Failure Analysis - part of analysis of the drop in funnel
Insights & Plan Forward - part of exec summary

(edited)
Gilles Knobloch  [6:57 PM]
I'll try to iterate on this before Monday's call
cc @fdelval