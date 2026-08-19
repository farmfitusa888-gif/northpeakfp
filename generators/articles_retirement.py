#!/usr/bin/env python3
"""
Self-employed retirement cluster.

WHY THIS CLUSTER, AND WHY THESE EIGHT TOPICS
The Search Console export for the three months to 2026-08-16 shows the firm
picking up impressions across twelve distinct retirement queries -- and all of
them landing on ONE page, /articles/retirement-plans-self-employed, which sits
at position 80.4 with 106 impressions and zero clicks. The demand is real and
the coverage is a single thin page.

Every topic below is taken from a query that actually appeared in that report:

    self employed ira ................................. 9 impressions
    self employed sep ................................. 6
    ira for self employed ............................. 5
    self employment retirement plans .................. 5
    sep ira alternatives .............................. 4
    sep ira self employed ............................. 4
    traditional ira vs sep ............................ 4
    sep retirement account self employed .............. 3
    403b vs sep ira ................................... 2
    self employment ira ............................... 2
    self employment retirement savings ................ 2
    self-employed ira ................................. 2

NO DOLLAR FIGURES ANYWHERE, DELIBERATELY
Contribution limits, phase-out ranges and compensation caps are indexed and
change annually. Hard-coding them means every article silently becomes wrong
each January, on a site giving tax guidance, under a named author. Every one of
these explains the MECHANISM -- which is stable -- and links to the IRS page
that carries the current number. That is also why none of them state deadlines.

LICENCE BOUNDARY
Chaudhry Ahmad is not a CPA and is not a registered investment adviser. These
explain how the account types work and what the choice costs or saves in tax
terms. None of them recommend an investment, and none say what any individual
should do. That line is stated in the copy, not just in the footer disclaimer.

SOURCE
IRS Simplified Employee Pension (SEP) plan sponsor documentation, verified
2026-08-19: only the employer contributes, employees cannot make salary
deferrals, and the contribution RATE must be uniform across all eligible
employees. Self-employed compensation for the calculation is net earnings from
self-employment reduced by half of self-employment tax and by the contributor's
own SEP contribution.
"""

IRS_SEP = "https://www.irs.gov/retirement-plans/plan-sponsor/simplified-employee-pension-plan-sep"
IRS_401K = "https://www.irs.gov/retirement-plans/one-participant-401k-plans"
IRS_SIMPLE = "https://www.irs.gov/retirement-plans/plan-sponsor/simple-ira-plan"
IRS_IRA = "https://www.irs.gov/retirement-plans/individual-retirement-arrangements-iras"
IRS_LIMITS = "https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-ira-contribution-limits"


def _a(url, text):
    return f'<a href="{url}" rel="noopener" target="_blank">{text}</a>'


ARTICLES = [

# ---------------------------------------------------------------------------
{
 "slug": "ira-options-self-employed",
 "cat": "Tax Planning",
 "title": "IRA Options When You Work for Yourself",
 "desc": "The retirement accounts available to a self-employed person, what separates them, and the one question that usually decides which fits.",
 "keywords": "self employed ira, ira for self employed, self employment retirement plans, self employed retirement savings",
 "read": "7 min read",
 "lede": "People come to me asking which retirement account they should open, and the honest answer is that the account is the last decision, not the first. What decides it is whether you have employees, and how much of your income you can actually afford to set aside.",
 "sections": [
   ("Four accounts, and what actually separates them",
    "There are four you are likely to be choosing between: a traditional or Roth IRA, a "
    "SEP-IRA, a SIMPLE IRA, and a solo 401(k). They differ on three things that matter far "
    "more than the marketing does &mdash; how much you can put in, who else you have to "
    "cover, and how much administration you are signing up for. "
    + _a(IRS_IRA, "The IRS overview of IRAs") + " is the neutral starting point."),

   ("The question that usually settles it",
    "Do you have employees? Not contractors &mdash; employees. If the answer is no, the "
    "field is wide open and the decision comes down to contribution room versus paperwork. "
    "If the answer is yes, some of these options get expensive fast, because they oblige "
    "you to contribute for your people too. That single fact eliminates more options than "
    "anything else on the list."),

   ("If it is only you",
    "A SEP-IRA is the low-effort choice: little setup, no annual filing at typical sizes, "
    "and a contribution based on a percentage of your net self-employment earnings. A solo "
    "401(k) generally lets you get more in at the same income, because you contribute both "
    "as the employee and as the employer &mdash; but it is a real plan with real "
    "administration once the balance grows. "
    + _a(IRS_401K, "The IRS page on one-participant 401(k) plans") + " sets out the "
    "difference plainly."),

   ("If you have people on payroll",
    "This is where owners get caught. A SEP requires the employer to contribute at a "
    "<strong>uniform rate for every eligible employee</strong>. If you put in 20% for "
    "yourself, that same 20% of compensation goes in for everyone who qualifies. A SIMPLE "
    "IRA works differently, with employee deferrals plus a required employer match or "
    "contribution. Neither is wrong &mdash; but the cost of the two is very different once "
    "there is a payroll, and that should be modelled before the account is opened, not "
    "after."),

   ("The ordinary IRA still has a place",
    "A traditional or Roth IRA has a much lower ceiling than the business plans, and it is "
    "not tied to your business at all. That makes it the fallback when your self-employment "
    "income is modest, or a supplement alongside a business plan. Deductibility and Roth "
    "eligibility both depend on income and on whether you are covered by a workplace plan; "
    + _a(IRS_LIMITS, "the IRS publishes the current thresholds") + " and they move most "
    "years."),

   ("Where the tax benefit actually lands",
    "Contributions to the pre-tax versions generally reduce taxable income in the year you "
    "make them, which is what makes this one of the few decisions that helps now and later "
    "at the same time. But the deduction is only worth what your marginal rate makes it "
    "worth. In a low-income year, deferring the deduction &mdash; or using a Roth &mdash; "
    "can be the better call. That is a numbers question, and it is answerable before you "
    "commit."),

   ("What I do and what I do not",
    "I help owners work out what they can sustainably contribute, what each option costs "
    "once employees are in the picture, and what the deduction is actually worth against "
    "their marginal rate. I am not a registered investment adviser and I do not tell anyone "
    "what to invest in. Choosing the account and choosing the investments inside it are two "
    "different jobs."),
 ],
},

# ---------------------------------------------------------------------------
{
 "slug": "sep-ira-vs-traditional-ira",
 "cat": "Tax Planning",
 "title": "SEP-IRA vs. Traditional IRA: What Actually Differs",
 "desc": "Both are IRAs and both can be deductible, but they are funded by different people under different rules. The practical differences for someone self-employed.",
 "keywords": "traditional ira vs sep, sep ira vs traditional ira, self employed ira comparison",
 "read": "6 min read",
 "lede": "The names make these sound like variations on one thing. They are not. A traditional IRA is your personal account. A SEP-IRA is a business plan that happens to deposit into an IRA, and that difference drives everything else.",
 "sections": [
   ("Who puts the money in",
    "This is the cleanest way to keep them straight. You fund a traditional IRA yourself, "
    "out of personal money. A SEP-IRA is funded by the <strong>employer</strong> &mdash; "
    "which, when you are self-employed, is still you, but wearing the business hat. "
    + _a(IRS_SEP, "The IRS is explicit") + " that only the employer contributes to a SEP "
    "and that employees cannot make salary deferrals into one."),

   ("How much can go in",
    "A traditional IRA has a flat annual ceiling that applies to everyone, with a catch-up "
    "for older savers. A SEP is calculated as a percentage of compensation, up to a cap. For "
    "anyone with meaningful self-employment income, the SEP room is substantially larger. "
    "For someone with a small side income, the flat IRA limit may actually be the higher of "
    "the two. Both figures are indexed and move; check "
    + _a(IRS_LIMITS, "the current IRS numbers") + " rather than a blog post, including this "
    "one."),

   ("The compensation calculation is not what people expect",
    "For a self-employed person, the SEP contribution is not simply a percentage of profit. "
    "It is based on net earnings from self-employment <em>reduced by</em> half of your "
    "self-employment tax and by your own SEP contribution &mdash; which makes it circular, "
    "and is why the effective percentage is lower than the headline rate. This is the single "
    "most common place I see people over-contribute by accident."),

   ("Deductibility works differently",
    "A SEP contribution is a business deduction. A traditional IRA contribution is a "
    "personal deduction, and whether you get it at all depends on your income and on whether "
    "you or a spouse are covered by a workplace retirement plan. Two people with identical "
    "income can get very different answers on the traditional IRA and identical answers on "
    "the SEP."),

   ("You can often have both",
    "Having a SEP does not automatically bar you from a traditional or Roth IRA. It can, "
    "however, affect whether the traditional IRA contribution is deductible, because a SEP "
    "generally counts as being covered by a workplace plan. That is a real interaction and it "
    "catches people who assumed the two were independent."),

   ("The employee question, again",
    "If your business has eligible employees, the SEP obliges you to contribute for them at "
    "the same rate you use for yourself. A traditional IRA carries no such obligation because "
    "it is not a business plan at all. For an owner with staff, that difference can be larger "
    "than the contribution limits themselves."),
 ],
},

# ---------------------------------------------------------------------------
{
 "slug": "sep-ira-with-employees",
 "cat": "Tax Planning",
 "title": "The SEP-IRA Trap When You Have Employees",
 "desc": "A SEP requires the same contribution rate for every eligible employee. What that means in practice for an owner who wants to fund their own retirement.",
 "keywords": "sep ira employees, sep ira uniform contribution, sep ira small business employees",
 "read": "6 min read",
 "lede": "A SEP-IRA is the easiest business retirement plan to open, which is exactly why owners open one and then discover what it obliges them to do when they hire their second person.",
 "sections": [
   ("The rule in one sentence",
    "The contribution rate must be <strong>uniform for all eligible employees</strong>. "
    + _a(IRS_SEP, "The IRS states it directly") + ": the employer's contribution rate, large "
    "or small, is the same for everyone who qualifies. You cannot fund 20% for yourself and "
    "3% for the team."),

   ("Why that lands harder than it sounds",
    "For a solo operator, a SEP is close to free money in tax terms: contribute, deduct, "
    "done. Add employees and the same decision becomes a multiple. Deciding to put a large "
    "percentage away for yourself is simultaneously deciding to fund that percentage of "
    "payroll for everyone eligible. The plan does not get more expensive gradually &mdash; it "
    "gets more expensive the moment someone crosses the eligibility threshold."),

   ("Who counts as eligible",
    "Eligibility is set by the plan document within limits the IRS defines, typically based "
    "on age, how many of the past several years the person worked for you, and a minimum "
    "compensation floor. Part-time and seasonal staff can qualify, which surprises owners who "
    "assumed only full-timers counted. This is worth reading carefully before the plan is "
    "adopted, because the terms are much easier to set than to change."),

   ("What owners do instead",
    "Three common paths. Some tighten eligibility to the maximum the rules allow, which "
    "delays when new hires qualify. Some move to a solo 401(k) while they are still the only "
    "employee, and accept the extra administration in exchange for control. Some move to a "
    "SIMPLE IRA, where the employer obligation is a defined match or a fixed contribution "
    "rather than a mirror of whatever the owner takes. "
    + _a(IRS_SIMPLE, "The IRS SIMPLE IRA page") + " sets out that structure."),

   ("The mistake that costs the most",
    "Opening the SEP first and thinking about employees later. Once a plan is in place and "
    "people are eligible, unwinding it is not a paperwork exercise &mdash; it has real cost "
    "and real timing constraints. If hiring is anywhere in the next couple of years, the plan "
    "choice should be made with that in view, not revisited afterwards."),

   ("Where I come in",
    "I model what each option costs at your actual payroll, at the contribution level you "
    "actually want, and at the headcount you actually expect &mdash; before anything is "
    "opened. That is a spreadsheet question with a clear answer, and it is much cheaper to "
    "run now than to discover in the second year of a plan."),
 ],
},

# ---------------------------------------------------------------------------
{
 "slug": "sep-ira-alternatives",
 "cat": "Tax Planning",
 "title": "SEP-IRA Alternatives Worth Comparing",
 "desc": "If a SEP does not fit — because of employees, contribution room, or Roth treatment — these are the realistic alternatives and what each trades away.",
 "keywords": "sep ira alternatives, alternatives to sep ira, self employed retirement options",
 "read": "6 min read",
 "lede": "A SEP-IRA is a good default and a bad universal answer. People usually go looking for an alternative for one of three reasons: they hired someone, they want to put more away, or they want Roth treatment. Each reason points somewhere different.",
 "sections": [
   ("If the problem is employees",
    "A SIMPLE IRA is the usual next stop. Instead of the employer mirroring whatever rate "
    "the owner takes, employees defer their own salary and the employer provides a defined "
    "match or a fixed contribution. The employer cost becomes predictable rather than "
    "proportional to the owner's ambition. It comes with its own eligibility and notice "
    "requirements &mdash; " + _a(IRS_SIMPLE, "see the IRS SIMPLE IRA page") + "."),

   ("If the problem is contribution room",
    "A solo 401(k) generally allows a larger total contribution at the same income, because "
    "you contribute in two capacities: as the employee, through salary deferral, and as the "
    "employer. At lower income levels that difference is significant. The trade is "
    "administration &mdash; it is a genuine retirement plan, and once assets pass a threshold "
    "there is an annual filing obligation. "
    + _a(IRS_401K, "The IRS one-participant 401(k) page") + " covers the structure."),

   ("If the problem is Roth treatment",
    "A SEP is traditionally pre-tax: deduct now, pay tax on withdrawal. If you would rather "
    "pay tax now and withdraw tax-free later &mdash; which can make sense in a low-income "
    "year, or early in a business &mdash; a Roth IRA or a Roth option inside a solo 401(k) is "
    "the route. The right answer here depends on whether your marginal rate today is higher "
    "or lower than you expect it to be in retirement, which is a forecast, not a fact."),

   ("If the problem is that you have a job as well",
    "Plenty of self-employed people also have W-2 employment with a workplace plan. Your "
    "salary deferrals are limited across all plans in aggregate, not per plan, while employer "
    "contributions follow different rules. This is the situation where people most often "
    "over-contribute without realising, and it is worth checking before December rather than "
    "in April."),

   ("The option people forget",
    "Doing less. If cash flow is tight, a smaller contribution to a simpler account beats a "
    "larger contribution you have to pull back out. Excess contributions carry correction "
    "procedures and, if left, penalties. I would rather see someone contribute modestly and "
    "consistently than max out once and spend the next year unwinding it."),
 ],
},

# ---------------------------------------------------------------------------
{
 "slug": "403b-vs-sep-ira",
 "cat": "Tax Planning",
 "title": "403(b) vs. SEP-IRA: Using Both With a Job and a Side Business",
 "desc": "If you have a 403(b) at work and self-employment income on the side, the two interact. What is shared, what is separate, and where people over-contribute.",
 "keywords": "403b vs sep ira, 403b and sep ira same year, side business retirement plan",
 "read": "6 min read",
 "lede": "This comes up constantly with teachers, nurses, professors and hospital staff who consult on the side. You have a 403(b) through the job and self-employment income of your own, and the question is whether you can use both. Usually yes — but not in the way most people assume.",
 "sections": [
   ("They are different kinds of plan",
    "A 403(b) is an employer-sponsored plan you contribute to through salary deferral from "
    "your paycheque, typically at a school, hospital or non-profit. A SEP-IRA is a plan your "
    "own business sponsors and funds, with "
    + _a(IRS_SEP, "employer contributions only") + " and no salary deferral at all. Because "
    "the money enters through different doors, the two are not simply added together."),

   ("What is shared and what is not",
    "The critical distinction: your <strong>salary deferrals</strong> are limited in "
    "aggregate across plans, so deferrals into a 403(b) count against that shared ceiling. "
    "A SEP contribution is not a deferral &mdash; it is an employer contribution &mdash; so "
    "it is governed by a different limit. This is why someone already maxing a 403(b) can "
    "often still fund a SEP from genuine self-employment income. It is also why the arithmetic "
    "confuses people: two limits, two different scopes."),

   ("The self-employment income has to be real",
    "A SEP contribution has to be supported by actual net earnings from self-employment. "
    "Consulting, private practice, honoraria and freelance work generally qualify. Your "
    "salary from the 403(b) employer does not, no matter how the two feel from your side. If "
    "the side income is small, the SEP contribution will be small, because it is a percentage "
    "of that income and nothing else."),

   ("Where people get it wrong",
    "Three recurring errors. Treating total household income as the SEP base rather than net "
    "self-employment earnings. Assuming a 403(b) at work blocks a SEP entirely &mdash; it "
    "usually does not. And forgetting that being covered by a workplace plan affects whether "
    "a separate traditional IRA contribution is deductible, which is a different question "
    "again."),

   ("If there is also a 457(b)",
    "Many public-sector and non-profit employers offer a 457(b) alongside the 403(b), and it "
    "has its own limit that generally does not share with the 403(b). For someone with a "
    "403(b), a 457(b) and a side business, there is more room available than almost anyone "
    "expects &mdash; and more ways to trip over the interaction. That combination is worth "
    "mapping once, properly, rather than guessing each December."),

   ("What this is not",
    "This explains how the account types interact. It is not advice about your situation, and "
    "I am not a registered investment adviser &mdash; nothing here is a recommendation about "
    "what to invest in. What I can do is work out how much room you actually have across all "
    "of it, which is usually the question underneath the question."),
 ],
},

# ---------------------------------------------------------------------------
{
 "slug": "simple-ira-vs-sep-ira",
 "cat": "Tax Planning",
 "title": "SIMPLE IRA vs. SEP-IRA for a Business With Staff",
 "desc": "Once you have employees, these two plans put very different obligations on the employer. A practical comparison of what each one commits you to.",
 "keywords": "simple ira vs sep ira, small business retirement plan employees, sep or simple ira",
 "read": "6 min read",
 "lede": "For a business with people on payroll, this is the comparison that matters, and it is not really about contribution limits. It is about how much of the funding is yours versus theirs, and how predictable that cost is.",
 "sections": [
   ("Who funds it",
    "A SEP is funded entirely by the employer &mdash; employees put in nothing, and "
    + _a(IRS_SEP, "cannot make salary deferrals") + ". A SIMPLE IRA is funded primarily by "
    "employees deferring their own salary, with the employer providing either a match for "
    "those who participate or a fixed contribution for everyone eligible. That is the whole "
    "difference in one line, and everything else follows from it."),

   ("How the employer cost behaves",
    "Under a SEP, your cost scales with your own ambition: contribute a high percentage for "
    "yourself and you owe that percentage across the eligible payroll. Under a SIMPLE with a "
    "match, your cost scales with participation &mdash; you pay for the people who choose to "
    "save. For an owner who wants to put a lot away, the SEP is the expensive structure. For "
    "an owner who wants a predictable benefit line, the SIMPLE usually is not."),

   ("Contribution room for the owner",
    "A SEP generally allows a larger contribution for the owner at higher income, because it "
    "is a percentage of compensation up to a cap. A SIMPLE has a lower deferral ceiling. If "
    "maximising the owner's own savings is the point and there is a payroll, the SEP gets you "
    "there but bills you for the whole team on the way."),

   ("Administration and timing",
    "Both are light compared with a 401(k), but they are not identical. SIMPLE plans carry "
    "employee notice requirements and have specific windows for establishing the plan. SEPs "
    "are more forgiving on timing, which is one reason they get adopted late in a year. "
    "Neither is difficult; both are easier to set up correctly than to fix afterwards."),

   ("The honest way to choose",
    "Take your actual payroll, your actual eligible headcount, and the contribution you "
    "genuinely want to make for yourself, and cost both structures out. In my experience the "
    "answer is rarely ambiguous once the numbers are on the page &mdash; and it is frequently "
    "the opposite of what the owner assumed before they were. That modelling is the part I "
    "help with; the plan documents themselves come from the provider."),
 ],
},

# ---------------------------------------------------------------------------
{
 "slug": "solo-401k-vs-sep-ira-switch",
 "cat": "Tax Planning",
 "title": "When to Move From a SEP-IRA to a Solo 401(k)",
 "desc": "A SEP is the easier start. There are three specific situations where a solo 401(k) becomes worth the extra administration — and one where it does not.",
 "keywords": "sep ira to solo 401k, solo 401k vs sep ira, switch retirement plan self employed",
 "read": "6 min read",
 "lede": "Most one-person businesses start with a SEP-IRA because it takes ten minutes. That is a good reason, and for a lot of people it stays the right answer. Here is how to tell when it has stopped being one.",
 "sections": [
   ("Reason one: you want more in at the same income",
    "This is the main event. A SEP contribution is a percentage of compensation. A solo "
    "401(k) lets you contribute as the employee through salary deferral <em>and</em> as the "
    "employer &mdash; so at moderate income levels you can generally get more in than a SEP "
    "allows, sometimes substantially. The gap narrows as income rises. "
    + _a(IRS_401K, "The IRS one-participant 401(k) page") + " sets out both components."),

   ("Reason two: you want Roth treatment",
    "A SEP is a pre-tax vehicle. Many solo 401(k) plans offer a Roth deferral option, letting "
    "you pay tax now and withdraw tax-free later. In a year when your income is unusually low "
    "&mdash; a first year, a slow year, a year you took time off &mdash; the deduction is "
    "worth less and the Roth option is worth more. This is the reason people most often "
    "overlook."),

   ("Reason three: you want to borrow against it",
    "Solo 401(k) plans can permit participant loans. IRAs, including SEP-IRAs, cannot. "
    "Whether borrowing from your retirement plan is a good idea is a separate conversation "
    "&mdash; usually the answer is no &mdash; but if the option matters to you, only one of "
    "these two offers it."),

   ("The reason not to switch",
    "Administration. A solo 401(k) is a real plan: a plan document, more care at year end, "
    "and an annual filing obligation once plan assets pass a threshold. If your contribution "
    "is modest and a SEP already accommodates it, switching buys you paperwork and nothing "
    "else. I have talked more people out of this move than into it."),

   ("And the condition that ends the conversation",
    "A solo 401(k) is for a business with no eligible employees other than the owner and a "
    "spouse. Hire someone who qualifies and the plan stops being a solo 401(k) &mdash; it "
    "becomes a regular 401(k), with the testing and cost that implies. If hiring is on the "
    "horizon, factor that in before you move, not after."),

   ("Timing matters more than people think",
    "The two plans have different establishment deadlines, and a SEP is generally the more "
    "forgiving of the two late in a year. That is a genuine reason to leave a switch until "
    "the following year rather than rush it &mdash; and a genuine reason to decide in "
    "October rather than the following April."),
 ],
},

# ---------------------------------------------------------------------------
{
 "slug": "sep-ira-contribution-rules",
 "cat": "Tax Planning",
 "title": "How a SEP-IRA Contribution Is Actually Calculated",
 "desc": "The SEP percentage is not a percentage of profit, and the calculation is circular. Why the effective rate is lower than the headline rate.",
 "keywords": "sep ira self employed, sep ira contribution calculation, sep retirement account self employed",
 "read": "6 min read",
 "lede": "This is the one I get asked to check most often, because the number people arrive at is usually too high. The rule sounds simple until you apply it to a self-employed person, at which point it turns circular.",
 "sections": [
   ("What the contribution is based on",
    "Not revenue, and not profit as you think of it. For a self-employed person the SEP "
    "contribution is based on <strong>net earnings from self-employment</strong>, reduced by "
    "half of your self-employment tax <em>and</em> by your own SEP contribution. "
    + _a(IRS_SEP, "The IRS sets this out") + " in the plan sponsor material."),

   ("Why that last part makes it circular",
    "Read it again: the contribution depends on a figure that has already been reduced by the "
    "contribution. You cannot calculate one without the other, which is why the effective "
    "percentage of your net earnings works out lower than the headline rate. This is not a "
    "trick &mdash; it is the same logic that stops an employer deduction from inflating the "
    "base it is calculated from &mdash; but it is why a mental estimate is almost always too "
    "high."),

   ("The number that goes on the return",
    "The deduction for your own SEP contribution is taken as an adjustment on your personal "
    "return rather than as a business expense on the Schedule C itself. Contributions made "
    "for employees are a business deduction. Two different places, and mixing them up changes "
    "both your self-employment tax and your income tax."),

   ("Where people over-contribute",
    "Four ways I see regularly. Applying the headline percentage straight to net profit. "
    "Forgetting the self-employment tax adjustment. Including W-2 wages from an unrelated job "
    "in the base. And, for anyone with more than one plan, ignoring the aggregate limits. "
    "Excess contributions are correctable, but the process has deadlines and the correction "
    "is more work than getting it right was."),

   ("What to do before you fund it",
    "Run the calculation on your actual year-to-date figures before you move money, not "
    "after. If your income is still moving, contribute conservatively and top up once the "
    "year is closed &mdash; SEPs are relatively forgiving on timing, which makes that "
    "sequence practical. Current caps and percentages are indexed and move; "
    + _a(IRS_LIMITS, "check the IRS figures") + " for the year you are funding rather than "
    "carrying last year's number forward."),

   ("Where I help",
    "This is arithmetic against your real books, which is exactly the kind of thing that goes "
    "wrong when the books are behind. If your bookkeeping is current, the calculation takes "
    "minutes. If it is not, the calculation is a guess &mdash; and a guess is how the "
    "over-contribution happens in the first place."),
 ],
},

]
