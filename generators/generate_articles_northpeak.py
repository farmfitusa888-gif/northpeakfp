#!/usr/bin/env python3
"""Generate 25 SEO-optimized accounting articles as standalone HTML files."""
import os, html, json, pathlib

OUT = os.environ.get("NP_ROOT_ARTICLES") or str(
    pathlib.Path(__file__).resolve().parent.parent / "site" / "articles")
os.makedirs(OUT, exist_ok=True)

# ============================================================
# CLIENT CONFIG — edit these values, everything else updates
# ============================================================
SITE       = "https://northpeakfp.com"
FIRM       = "NorthPeak Financial Partners"
AUTHOR     = "NorthPeak Financial Partners"   # swap to founder's name once known
CREDENTIAL = "Accounting &amp; Advisory"
EMAIL      = "info@northpeakfp.com"
PHONE      = "(847) 644-2288"
LOCATION   = "Wilmette, IL"
FOUNDER    = "Chaudhry Ahmad"
FOUNDER_TITLE = "Founder &amp; Principal"
SHOW_DATE  = False       # visible post date hidden; schema dates still used
PUBDATE    = "2026-07-29"
SEO_TITLES = {'quarterly-estimated-taxes': 'Quarterly Estimated Taxes: A Guide for the Self-Employed', 'bookkeeping-basics': 'Bookkeeping Basics: What New Business Owners Must Track', 'sales-tax-guide': 'Sales Tax for Small Business: When You Owe & How to Collect', 'cash-vs-accrual': 'Cash vs. Accrual Accounting: Which Fits Your Business?', 'business-expense-categories': 'Business Expense Categories for Maximum Deductions', 'home-office-deduction': 'Home Office Deduction: Do You Qualify & How to Claim It', 'section-179-deduction': 'Section 179: Deduct Equipment the Year You Buy It', 'retirement-plans-self-employed': 'Self-Employed Retirement: SEP-IRA vs. Solo 401(k)', 'mileage-deduction-guide': 'Mileage Deduction: How to Track & Claim Business Driving', 'deductible-vs-nondeductible': 'Deductible vs. Non-Deductible Business Expenses', 'choosing-business-entity': 'Choosing a Business Entity: Sole Prop, LLC, or Corp'}


# Each article: slug, category, title, meta_desc, keywords, lede, and sections
# Sections are (heading, paragraph) tuples. Authoritative outbound links included inline.
ARTICLES = [
    {
        "slug": "tax-deductions-small-business",
        "cat": "Small Business Tax",
        "title": "7 Tax Deductions Small Businesses Miss Every Year",
        "desc": "I break down seven commonly overlooked small business tax deductions, plus how to document each so it survives an audit.",
        "keywords": "small business tax deductions, accountant for small business, self-employed deductions, tax savings",
        "read": "6 min read",
        "lede": "Most small business owners leave money on the table not because they cheat the system, but because they never knew a deduction existed. Here are seven of the most common ones I see missed.",
        "sections": [
            ("Home Office Expenses", "If you use part of your home regularly and exclusively for business, you can deduct a portion of your rent or mortgage interest, utilities, and insurance. The <a href=\"https://www.irs.gov/businesses/small-businesses-self-employed/home-office-deduction\" rel=\"noopener\" target=\"_blank\">IRS simplified method</a> lets you deduct a flat rate per square foot, which keeps the paperwork light. Keep a photo of the space and a measurement on file."),
            ("Vehicle & Mileage", "Driving to a client, the bank, or the supply store all counts. You can track actual expenses or take the standard mileage rate — usually mileage wins for simplicity. The key is a log: date, destination, purpose, and miles."),
            ("Retirement Contributions", "A SEP-IRA or Solo 401(k) lets self-employed people set aside far more than a standard IRA, and the contribution lowers taxable income dollar for dollar. It's one of the largest levers a profitable small business has."),
            ("Health Insurance Premiums", "If you're self-employed and pay for your own health insurance, those premiums are often deductible — including coverage for your spouse and dependents. It's an above-the-line deduction, so you get it even without itemizing."),
            ("Startup & Organizational Costs", "Legal fees, market research, and initial advertising spent getting the business off the ground can be deducted, up to a limit in the first year with the rest amortized over time."),
            ("Software & Subscriptions", "Accounting software, cloud storage, professional memberships, and industry publications are ordinary business expenses that add up to a meaningful deduction across a full year."),
            ("Professional Fees", "Fees paid to an accountant, bookkeeper, or attorney for your business are fully deductible. The cost of getting your taxes done correctly is itself a write-off."),
        ],
    },
    {
        "slug": "llc-vs-s-corp",
        "cat": "Business Structure",
        "title": "LLC vs. S-Corp: Which Saves You More in Taxes?",
        "desc": "A plain-English comparison of LLC and S-Corp taxation for small business owners, and the income level where an S-Corp election starts to pay off.",
        "keywords": "LLC vs S-Corp, S-Corp election, self-employment tax, business structure, small business taxes",
        "read": "7 min read",
        "lede": "The LLC-versus-S-Corp question comes up in almost every new-client meeting. The honest answer is: it depends on your profit. Here's how to think about it.",
        "sections": [
            ("What an LLC Actually Is", "An LLC is a legal structure, not a tax status. By default a single-member LLC is taxed as a sole proprietorship, which means all profit is subject to self-employment tax. The liability protection is real; the tax savings, by default, are not."),
            ("What Changes With an S-Corp Election", "An LLC can elect to be taxed as an S-Corp. You then pay yourself a reasonable salary (subject to payroll tax) and take remaining profit as distributions, which are not subject to self-employment tax. That split is where the savings come from."),
            ("The Break-Even Point", "The extra payroll filings and bookkeeping an S-Corp requires cost money, so the election only pays off above a certain profit level — often around the point where net profit clears roughly $40,000–$50,000, though it varies. See the <a href=\"https://www.irs.gov/businesses/small-businesses-self-employed/s-corporations\" rel=\"noopener\" target=\"_blank\">IRS S-Corp overview</a> for the rules."),
            ("The Reasonable Salary Rule", "The IRS requires S-Corp owners to pay themselves a reasonable salary before taking distributions. Setting it too low to dodge payroll tax is a common audit trigger."),
            ("How to Decide", "Run the numbers on your actual profit, factor in the added compliance cost, and revisit the decision yearly as income grows. This is exactly the kind of calculation worth doing with a professional."),
        ],
    },
    {
        "slug": "quarterly-estimated-taxes",
        "cat": "Tax Planning",
        "title": "Quarterly Estimated Taxes: A Simple Guide for the Self-Employed",
        "desc": "When quarterly estimated taxes are due, how to calculate them, and how to avoid the underpayment penalty — explained simply.",
        "keywords": "quarterly estimated taxes, self-employed taxes, estimated tax payments, underpayment penalty",
        "read": "5 min read",
        "lede": "When you're self-employed, no one withholds taxes for you. The IRS expects you to pay as you go — four times a year. Here's how to stay ahead of it.",
        "sections": [
            ("Why You Have to Pay Quarterly", "Employees have taxes withheld from every paycheck. When you work for yourself, that job falls to you. The IRS wants its share throughout the year, not just in April."),
            ("The Four Due Dates", "Estimated payments are generally due in April, June, September, and January of the following year. Mark them on a calendar — the deadlines don't move to suit your cash flow. The <a href=\"https://www.irs.gov/businesses/small-businesses-self-employed/estimated-taxes\" rel=\"noopener\" target=\"_blank\">IRS estimated taxes page</a> lists the exact dates each year."),
            ("How to Estimate the Amount", "A common approach is to set aside a percentage of every payment you receive — often 25–30% — into a separate account. A safer method is the safe-harbor rule below."),
            ("The Safe-Harbor Rule", "If you pay at least 100% of last year's tax liability (110% for higher earners), you generally avoid the underpayment penalty even if you owe more at filing. It's the simplest way to stay protected."),
            ("Avoiding the Penalty", "Underpaying triggers an interest-based penalty. Paying on time and using safe harbor keeps you clear. A quick mid-year check-in helps you adjust before it's too late."),
        ],
    },
    {
        "slug": "bookkeeping-basics",
        "cat": "Bookkeeping",
        "title": "Bookkeeping Basics: What Every New Business Owner Needs to Track",
        "desc": "The essential records every small business should keep, how long to keep them, and the simplest system to stay organized year-round.",
        "keywords": "bookkeeping basics, small business bookkeeping, record keeping, business expenses tracking",
        "read": "6 min read",
        "lede": "Good bookkeeping isn't about being an accountant — it's about never scrambling at tax time. Here's the minimum every owner should track.",
        "sections": [
            ("Separate Business and Personal", "Open a dedicated business bank account and card on day one. Mixing personal and business spending is the single biggest bookkeeping mistake new owners make, and it complicates everything downstream."),
            ("Track Income and Expenses", "Every dollar in and out needs a record. Modern accounting software connects to your bank and categorizes most of it automatically, turning hours of work into minutes."),
            ("Keep Your Receipts", "Digital copies are fine and easier to store. A quick photo at the point of purchase saves you from a shoebox in March. The <a href=\"https://www.irs.gov/businesses/small-businesses-self-employed/recordkeeping\" rel=\"noopener\" target=\"_blank\">IRS recordkeeping guidance</a> explains what to retain."),
            ("Know What to Keep and For How Long", "As a general rule, keep tax records for at least three years, and longer for anything involving property or major assets. When in doubt, keep it."),
            ("Reconcile Monthly", "Matching your books against your bank statement once a month catches errors early and gives you a real picture of the business instead of a year-end surprise."),
        ],
    },
    {
        "slug": "1099-vs-w2",
        "cat": "Payroll",
        "title": "1099 vs. W-2: How to Classify Your Workers Correctly",
        "desc": "The difference between independent contractors and employees, why misclassification is risky, and how to get worker classification right.",
        "keywords": "1099 vs W2, worker classification, independent contractor, employee classification, payroll taxes",
        "read": "6 min read",
        "lede": "Calling a worker a contractor when they're really an employee is one of the costliest mistakes a small business can make. Here's how to classify correctly.",
        "sections": [
            ("The Core Difference", "An employee (W-2) works under your direction and control. An independent contractor (1099) runs their own business and controls how the work gets done. The distinction is about control, not job title."),
            ("Why It Matters", "For employees you withhold and pay payroll taxes; for contractors you don't. Misclassifying employees as contractors to save on payroll tax can lead to back taxes and penalties."),
            ("The IRS Tests", "The IRS looks at behavioral control, financial control, and the relationship between the parties. No single factor decides it — it's the whole picture. The <a href=\"https://www.irs.gov/businesses/small-businesses-self-employed/independent-contractor-self-employed-or-employee\" rel=\"noopener\" target=\"_blank\">IRS classification guide</a> walks through each test."),
            ("Common Misclassification Traps", "Long-term, full-time workers doing core business functions usually look like employees no matter what the contract says. Be honest about the working relationship."),
            ("When You're Not Sure", "If a role sits in the gray area, it's worth a professional review before tax season. Fixing classification proactively is far cheaper than fixing it after an audit."),
        ],
    },
    {
        "slug": "sales-tax-guide",
        "cat": "Sales Tax",
        "title": "Sales Tax for Small Businesses: When You Owe It and How to Collect",
        "desc": "I explain sales tax nexus, when you're required to collect, and how to stay compliant across states without losing your mind.",
        "keywords": "sales tax small business, sales tax nexus, collecting sales tax, economic nexus, sales tax compliance",
        "read": "6 min read",
        "lede": "Sales tax used to be simple: you collected it where you had a store. Online selling changed everything. Here's what applies now.",
        "sections": [
            ("What Sales Tax Nexus Means", "Nexus is the connection that requires you to collect sales tax in a state. It's created by physical presence — an office, inventory, employees — or, increasingly, by economic activity."),
            ("Economic Nexus and Online Sales", "After a landmark Supreme Court decision, states can require out-of-state sellers to collect tax once they cross a sales threshold in that state. If you sell online, you may owe tax in states you've never set foot in."),
            ("Registering to Collect", "Before collecting, you register with each state's tax authority. Collecting without registering — or registering and not filing — both cause problems."),
            ("Filing and Remitting", "You collect the tax, hold it, and remit it on the state's schedule. It's not your money; treat it as pass-through you're holding in trust."),
            ("Getting Help Early", "Multi-state sales tax gets complex fast. Setting up a system early, ideally with professional help, prevents a painful cleanup later."),
        ],
    },
    {
        "slug": "cash-vs-accrual",
        "cat": "Accounting Methods",
        "title": "Cash vs. Accrual Accounting: Which Method Fits Your Business?",
        "desc": "The difference between cash and accrual accounting, the pros of each, and how to choose the right method for your small business.",
        "keywords": "cash vs accrual accounting, accounting methods, small business accounting, accrual basis",
        "read": "5 min read",
        "lede": "Cash or accrual? The method you choose changes when income and expenses hit your books — and sometimes your tax bill. Here's the difference.",
        "sections": [
            ("Cash Basis Explained", "Under cash accounting, you record income when money lands and expenses when you pay them. It's simple and mirrors your bank balance, which is why most small businesses start here."),
            ("Accrual Basis Explained", "Accrual records income when it's earned and expenses when they're incurred, regardless of when cash moves. It gives a truer picture of profitability over time."),
            ("The Trade-Offs", "Cash is simpler and helps with cash-flow visibility. Accrual is more accurate for businesses with inventory, receivables, or investors who want a real performance picture."),
            ("Which One You're Allowed to Use", "Smaller businesses can generally choose, but past a certain size or with inventory, the IRS may require accrual. The rules are worth confirming before you commit."),
            ("Switching Methods", "You can change methods, but it requires IRS approval and careful handling. Choosing well upfront saves that hassle."),
        ],
    },
    {
        "slug": "tax-prep-checklist",
        "cat": "Tax Planning",
        "title": "The Small Business Tax Prep Checklist for Filing Season",
        "desc": "Everything you need to gather before filing your small business taxes, organized into a simple checklist so nothing gets missed.",
        "keywords": "tax prep checklist, small business tax filing, tax documents, filing season, tax preparation",
        "read": "5 min read",
        "lede": "The businesses that dread tax season are usually the ones scrambling for documents. Gather these ahead of time and filing becomes routine.",
        "sections": [
            ("Income Records", "Pull together all revenue records: sales reports, 1099s you received, merchant statements, and bank deposits. Your reported income should reconcile to these."),
            ("Expense Documentation", "Assemble categorized expenses with receipts — supplies, rent, utilities, software, professional fees, and mileage logs. Clean categories make deductions easy to claim."),
            ("Payroll and Contractor Forms", "If you have workers, gather payroll summaries and copies of the 1099s and W-2s you issued. These need to match what you filed with the IRS."),
            ("Prior-Year Return", "Last year's return is a roadmap — it shows carryovers, depreciation schedules, and comparisons that flag anything unusual this year."),
            ("Big Purchases and Asset Changes", "Note any major equipment purchases, vehicle changes, or asset sales. These affect depreciation and may unlock deductions like Section 179."),
        ],
    },
    {
        "slug": "when-to-hire-accountant",
        "cat": "Working With an Accountant",
        "title": "When Should a Small Business Hire an Accountant?",
        "desc": "The signs it's time to bring on a professional accountant, what they actually do for you, and how to weigh the cost against the value.",
        "keywords": "when to hire an accountant, small business accountant, accounting services, bookkeeper vs accountant",
        "read": "5 min read",
        "lede": "Plenty of owners handle their own books at first — and should. But there's a point where doing it yourself costs more than it saves. Here's how to spot it.",
        "sections": [
            ("You're Spending Hours on Books Instead of the Business", "If bookkeeping is eating the time you'd otherwise spend earning, the math has already tipped. Your hourly value in the business usually exceeds an accountant's fee."),
            ("Your Taxes Got Complicated", "Adding employees, selling in multiple states, or restructuring the business all add complexity that's easy to get wrong and expensive to fix."),
            ("You're Making Big Decisions", "Buying equipment, taking a loan, or changing structure all have tax consequences. A quick professional read before you act can save far more than it costs."),
            ("Bookkeeper vs. Accountant", "A bookkeeper records transactions while an accountant interprets them, handles your filings, and helps with planning and strategy. Match the level of help to what your business actually needs."),
            ("The Real Return", "The goal isn't just a filed return — it's fewer mistakes, less stress, and tax strategy you'd never spot alone. That's where the value shows up."),
        ],
    },
    {
        "slug": "business-expense-categories",
        "cat": "Bookkeeping",
        "title": "Business Expense Categories: How to Organize for Maximum Deductions",
        "desc": "A clear breakdown of common business expense categories and how organizing them correctly protects your deductions at tax time.",
        "keywords": "business expense categories, deductible expenses, expense tracking, small business deductions",
        "read": "5 min read",
        "lede": "Deductions live or die by organization. Sort your spending into the right categories all year, and tax time becomes a copy-paste job.",
        "sections": [
            ("Why Categories Matter", "The IRS return groups expenses into standard categories. Matching your bookkeeping to those categories means your deductions are ready to transfer directly, with documentation behind each."),
            ("The Common Categories", "Advertising, supplies, rent, utilities, insurance, professional fees, travel, meals, and equipment cover most small businesses. Getting these consistent is 90% of the job."),
            ("Meals and Travel", "These are legitimate but scrutinized. Record who, what, and the business purpose. A vague 'dinner' won't hold up; 'client strategy dinner — Acme Corp, Q3 planning' will."),
            ("Equipment vs. Supplies", "Small consumables are supplies you deduct now; larger, longer-lasting purchases are assets that may be depreciated or expensed under special rules. The line matters for how you claim them."),
            ("Keeping It Consistent", "Pick your categories once and apply them the same way every month. Consistency is what makes the numbers trustworthy — and audit-proof."),
        ],
    },
    {
        "slug": "cash-flow-management",
        "cat": "Financial Management",
        "title": "Cash Flow Management: How to Keep Your Business Solvent",
        "desc": "Practical cash flow strategies for small businesses, including how to forecast, manage timing, and build a buffer against lean months.",
        "keywords": "cash flow management, small business cash flow, cash flow forecast, working capital",
        "read": "6 min read",
        "lede": "Profitable businesses still fail when cash runs out at the wrong moment. Managing the timing of money is a survival skill. Here's the practical version.",
        "sections": [
            ("Profit Is Not Cash", "You can be profitable on paper and broke in the bank if customers pay slowly or you buy inventory upfront. Cash flow tracks the actual timing of money, which is what keeps the lights on."),
            ("Forecast the Next 90 Days", "A rolling forecast of expected money in and out for the coming quarter turns nasty surprises into planned decisions. It doesn't need to be fancy — just honest."),
            ("Speed Up Money In", "Invoice promptly, make paying easy, and consider deposits or milestone billing for larger jobs. Every day faster is a day of cushion earned."),
            ("Slow Down Money Out (Sensibly)", "Use the full payment terms vendors offer without going late, and time large purchases for stronger months. Don't pay in January what's not due until February."),
            ("Build a Buffer", "A reserve covering a few months of expenses turns emergencies into inconveniences. Build it gradually from good months and protect it."),
        ],
    },
    {
        "slug": "home-office-deduction",
        "cat": "Small Business Tax",
        "title": "The Home Office Deduction: Do You Qualify and How to Claim It",
        "desc": "Who qualifies for the home office deduction, the two methods for calculating it, and how to claim it without raising red flags.",
        "keywords": "home office deduction, work from home taxes, self-employed home office, home office expenses",
        "read": "5 min read",
        "lede": "The home office deduction has an undeserved scary reputation. Claimed correctly, it's straightforward and legitimate. Here's how it works.",
        "sections": [
            ("The Qualification Rules", "The space must be used regularly and exclusively for business, and generally be your principal place of business. 'Exclusively' is the word that trips people up — a spare room used only for work qualifies; the kitchen table doesn't."),
            ("The Simplified Method", "Deduct a flat rate per square foot of office space, up to a cap. Minimal records, no tracking individual home bills — ideal for smaller spaces. The <a href=\"https://www.irs.gov/businesses/small-businesses-self-employed/home-office-deduction\" rel=\"noopener\" target=\"_blank\">IRS home office page</a> lists the current rate."),
            ("The Actual-Expense Method", "Deduct the business percentage of real home costs — mortgage interest, utilities, insurance, repairs. More paperwork, but often a larger deduction for bigger offices."),
            ("Who Can't Claim It", "W-2 employees generally can't claim it for work-from-home under current rules. It's primarily for the self-employed and business owners."),
            ("Documenting It Right", "Keep a photo, a measurement, and the home bills if you use the actual method. Good records turn a 'red flag' into a non-issue."),
        ],
    },
    {
        "slug": "section-179-deduction",
        "cat": "Small Business Tax",
        "title": "Section 179: How to Deduct Equipment Purchases the Year You Buy",
        "desc": "How the Section 179 deduction lets small businesses write off equipment immediately, what qualifies, and how to use it strategically.",
        "keywords": "section 179 deduction, equipment deduction, bonus depreciation, business equipment write-off",
        "read": "5 min read",
        "lede": "Normally you deduct equipment slowly over years. Section 179 lets you deduct it all now — a powerful tool if you use it deliberately.",
        "sections": [
            ("What Section 179 Does", "It lets you deduct the full cost of qualifying equipment in the year you put it into service, instead of depreciating it over its useful life. That front-loaded deduction can meaningfully lower a profitable year's taxes."),
            ("What Qualifies", "Business equipment, machinery, computers, off-the-shelf software, and certain vehicles generally qualify. It must be used more than half the time for business. See the <a href=\"https://www.irs.gov/publications/p946\" rel=\"noopener\" target=\"_blank\">IRS Publication 946</a> for specifics."),
            ("The Limits", "There's an annual dollar cap and a spending threshold above which the deduction phases out. It's built for small and mid-sized businesses, not massive capital programs."),
            ("Section 179 vs. Bonus Depreciation", "Bonus depreciation is a related tool with its own rules. Sometimes they're used together. Which comes first affects the outcome, so it's worth planning."),
            ("Using It Strategically", "Because it's optional, you can time purchases and elect it in years when the deduction helps most. Don't buy equipment just for the write-off — but if you need it, timing matters."),
        ],
    },
    {
        "slug": "retirement-plans-self-employed",
        "cat": "Tax Planning",
        "title": "Retirement Plans for the Self-Employed: SEP-IRA vs. Solo 401(k)",
        "desc": "Compare the top retirement plans for self-employed people and small business owners, and how each one cuts your tax bill.",
        "keywords": "self-employed retirement, SEP-IRA, Solo 401k, small business retirement plan, retirement tax savings",
        "read": "6 min read",
        "lede": "Working for yourself means no company 401(k) — but the options you do have are often more generous. And they cut your taxes today.",
        "sections": [
            ("Why This Is a Tax Play, Too", "Contributions to these plans generally reduce your taxable income now while building retirement savings. It's one of the few moves that helps you today and decades from now."),
            ("The SEP-IRA", "Simple to set up and maintain, a SEP-IRA lets you contribute a percentage of net self-employment income up to a high cap. Great for a one-person business that wants minimal admin."),
            ("The Solo 401(k)", "For a business with no employees besides an owner and spouse, a Solo 401(k) often allows even larger contributions because you contribute as both employee and employer. See the <a href=\"https://www.irs.gov/retirement-plans/one-participant-401k-plans\" rel=\"noopener\" target=\"_blank\">IRS Solo 401(k) page</a>."),
            ("Which One Fits", "SEP-IRAs win on simplicity; Solo 401(k)s often win on maximum contribution and flexibility. Income level and whether you want to save aggressively drive the choice."),
            ("Deadlines Matter", "Setup and funding deadlines differ by plan and can fall before you file. Miss them and the tax benefit for the year is gone — plan ahead."),
        ],
    },
    {
        "slug": "avoiding-irs-audit",
        "cat": "Tax Planning",
        "title": "How to Reduce Your Chances of an IRS Audit",
        "desc": "The common red flags that draw IRS attention and the simple habits that keep your small business return clean and defensible.",
        "keywords": "avoid IRS audit, audit red flags, small business audit, tax audit prevention",
        "read": "6 min read",
        "lede": "You can't audit-proof a return, but you can avoid the patterns that draw attention — and be ready if attention comes anyway.",
        "sections": [
            ("Report All Your Income", "The IRS receives copies of your 1099s and W-2s. If your return doesn't match what they already have, their systems notice automatically. Reconcile before you file."),
            ("Keep Deductions Reasonable and Documented", "Unusually large deductions relative to income can draw scrutiny. The deductions themselves are fine — what protects you is documentation behind each one."),
            ("Be Careful With Round Numbers", "Returns full of suspiciously round figures suggest estimates rather than records. Real numbers have cents. Precision signals honest bookkeeping."),
            ("Mind the Home Office and Vehicle Claims", "These are legitimate but historically flagged. Claim them — just keep the logs and measurements that prove them, as covered in our other guides."),
            ("If You Do Get a Notice", "Most IRS notices are routine and resolvable with the right paperwork. Don't panic, don't ignore it, and get professional help before responding. See <a href=\"https://www.irs.gov/individuals/understanding-your-irs-notice-or-letter\" rel=\"noopener\" target=\"_blank\">the IRS notices guide</a>."),
        ],
    },
    {
        "slug": "financial-statements-explained",
        "cat": "Financial Management",
        "title": "The 3 Financial Statements Every Owner Should Understand",
        "desc": "A plain-language guide to the income statement, balance sheet, and cash flow statement — and what each one tells you about your business.",
        "keywords": "financial statements, income statement, balance sheet, cash flow statement, small business finances",
        "read": "6 min read",
        "lede": "You don't need an accounting degree to run a business, but you do need to read three reports. Here's what each one actually tells you.",
        "sections": [
            ("The Income Statement", "Also called profit and loss, it shows revenue minus expenses over a period — whether you made money. It answers the most basic question: is the business profitable right now?"),
            ("The Balance Sheet", "A snapshot of what you own (assets), what you owe (liabilities), and what's left over (equity) at a moment in time. It shows financial health, not just performance."),
            ("The Cash Flow Statement", "This tracks actual cash moving in and out, reconciling the profit on your income statement with the money in your bank. It explains the gap between 'profitable' and 'liquid.'"),
            ("How They Work Together", "Profit on the income statement, strength on the balance sheet, and liquidity on the cash flow statement together give the full picture. Reading one alone can mislead you."),
            ("Using Them to Decide", "Reviewed monthly, these statements turn gut feelings into informed decisions about hiring, spending, and growth. That's the real point of keeping books."),
        ],
    },
    {
        "slug": "startup-tax-tips",
        "cat": "Business Structure",
        "title": "Tax Tips for Brand-New Businesses in Their First Year",
        "desc": "The tax moves that matter most in your first year of business, from choosing a structure to tracking startup costs and setting up systems.",
        "keywords": "startup tax tips, first year business taxes, new business taxes, startup costs deduction",
        "read": "5 min read",
        "lede": "The habits you set in year one echo for years. Get these tax basics right early and you'll save yourself expensive cleanup later.",
        "sections": [
            ("Choose Your Structure Deliberately", "Sole proprietorship, LLC, or S-Corp each carry different tax and liability consequences. The default isn't always best — a quick professional conversation upfront can shape years of savings."),
            ("Track Startup Costs From Day One", "Money spent before you officially open — research, legal setup, initial marketing — can often be deducted or amortized. Capture it now; reconstructing it later is painful."),
            ("Get an EIN and Separate Accounts", "An EIN and dedicated business banking establish a clean line between you and the business, which matters for both taxes and liability protection."),
            ("Set Up Bookkeeping Before You Need It", "Starting with clean books beats reconstructing a year of transactions in April. Pick a system early and use it consistently."),
            ("Plan for Self-Employment Tax", "First-time owners are often blindsided by self-employment tax and quarterly payments. Set money aside from the first dollar so it's never a shock."),
        ],
    },
    {
        "slug": "mileage-deduction-guide",
        "cat": "Small Business Tax",
        "title": "The Mileage Deduction: How to Track and Claim Business Driving",
        "desc": "How the business mileage deduction works, the standard rate versus actual expenses, and how to keep a log the IRS will accept.",
        "keywords": "mileage deduction, business mileage, standard mileage rate, vehicle expenses, mileage log",
        "read": "5 min read",
        "lede": "Business driving is real money back in your pocket — but only if you track it. Here's how to claim it without leaving anything on the table.",
        "sections": [
            ("What Counts as Business Miles", "Driving between job sites, to clients, to the bank, or to buy supplies counts. Your regular commute from home to a main workplace generally does not."),
            ("Standard Rate vs. Actual Expenses", "You can multiply business miles by the IRS standard rate, or track the actual costs of operating the vehicle and deduct the business percentage. Most people find the standard rate simpler. The <a href=\"https://www.irs.gov/tax-professionals/standard-mileage-rates\" rel=\"noopener\" target=\"_blank\">IRS standard mileage rates</a> update yearly."),
            ("Keeping a Log the IRS Accepts", "Record the date, destination, purpose, and miles for each trip. Apps that track this automatically from your phone remove almost all the friction."),
            ("The Commuting Trap", "Personal and commuting miles aren't deductible. Mixing them into your business total is a common, avoidable error that undermines the whole deduction."),
            ("Consistency Wins", "Whichever method you pick, apply it carefully and keep the records. A contemporaneous log beats a reconstructed guess every time."),
        ],
    },
    {
        "slug": "payroll-setup-guide",
        "cat": "Payroll",
        "title": "Setting Up Payroll for Your First Employee",
        "desc": "A step-by-step overview of what small businesses need to do to run payroll legally, from registrations to withholding and filings.",
        "keywords": "payroll setup, first employee, payroll taxes, small business payroll, withholding taxes",
        "read": "6 min read",
        "lede": "Hiring your first employee is a milestone — and a new set of obligations. Here's the payroll groundwork you need to get right.",
        "sections": [
            ("Get Your EIN and Register", "You'll need a federal EIN and, in most cases, state employer registrations for withholding and unemployment. These come before the first paycheck, not after."),
            ("Collect the Right Paperwork", "Every new hire completes a W-4 for withholding and an I-9 for work eligibility. Keep these on file from day one."),
            ("Understand What You Withhold", "You withhold income tax, Social Security, and Medicare from employees, and pay the employer share of Social Security and Medicare plus unemployment taxes. The <a href=\"https://www.irs.gov/businesses/small-businesses-self-employed/employment-taxes\" rel=\"noopener\" target=\"_blank\">IRS employment taxes page</a> lays out the details."),
            ("Deposit and File on Schedule", "Withheld taxes must be deposited on the IRS's schedule and reported on regular payroll filings. Missing these deadlines carries steep penalties."),
            ("Consider a Payroll Service", "Modern payroll software or a service handles calculations, deposits, and filings automatically. For most small businesses it's well worth the modest cost."),
        ],
    },
    {
        "slug": "tax-planning-vs-tax-prep",
        "cat": "Working With an Accountant",
        "title": "Tax Planning vs. Tax Preparation: Why the Difference Matters",
        "desc": "The difference between reactive tax preparation and proactive tax planning, and why planning is where the real savings happen.",
        "keywords": "tax planning vs tax preparation, proactive tax planning, tax strategy, small business tax savings",
        "read": "5 min read",
        "lede": "Most people only think about taxes in April. By then, the year is over and your options are gone. Planning is a different game entirely.",
        "sections": [
            ("Preparation Is Backward-Looking", "Tax prep reports what already happened. It's necessary, but by filing time the decisions that affect your bill were made months ago. You're just recording history."),
            ("Planning Is Forward-Looking", "Tax planning shapes decisions during the year — timing income and purchases, choosing structures, funding retirement — to lower next April's bill before it's set."),
            ("Where the Savings Live", "The biggest tax savings almost always come from planning, not preparation. A good preparer files correctly; a good planner changes the number you owe."),
            ("A Year-Round Conversation", "Planning means checking in at key moments — mid-year, before big purchases, when income shifts — not once at the deadline. Small adjustments compound."),
            ("Making the Shift", "Moving from reactive to proactive is the single highest-value change most small businesses can make with their finances. It's the difference between reporting and strategy."),
        ],
    },
    {
        "slug": "deductible-vs-nondeductible",
        "cat": "Small Business Tax",
        "title": "Deductible vs. Non-Deductible: What You Can and Can't Write Off",
        "desc": "A clear guide to which business expenses are deductible, which aren't, and the gray areas where owners most often go wrong.",
        "keywords": "deductible expenses, non-deductible expenses, business write-offs, tax deductions",
        "read": "5 min read",
        "lede": "Not every business expense is a write-off, and claiming ones that aren't invites trouble. Here's where the line actually falls.",
        "sections": [
            ("The Basic Test", "To be deductible, an expense generally must be ordinary and necessary for your business. That's the standard the IRS applies, and most legitimate costs meet it."),
            ("Clearly Deductible", "Supplies, rent, utilities, professional fees, business insurance, advertising, and employee wages are all standard deductions when they're genuinely for the business."),
            ("Clearly Not Deductible", "Personal expenses, most commuting, political contributions, and fines or penalties generally can't be written off, no matter how you frame them."),
            ("The Gray Areas", "Meals, travel that mixes business and personal, and use of your car or phone for both need careful splitting. Deduct only the business portion, and document it."),
            ("When in Doubt", "If you're unsure whether something qualifies, ask before you claim it. A quick check is cheaper than defending a bad deduction later."),
        ],
    },
    {
        "slug": "small-business-tax-credits",
        "cat": "Tax Planning",
        "title": "Tax Credits Small Businesses Often Overlook",
        "desc": "Valuable tax credits that many small businesses qualify for but never claim, and why credits beat deductions dollar for dollar.",
        "keywords": "small business tax credits, tax credits, R&D credit, work opportunity credit, business tax savings",
        "read": "5 min read",
        "lede": "Deductions lower your taxable income; credits lower your tax bill directly, dollar for dollar. That makes overlooked credits some of the most valuable money you can find.",
        "sections": [
            ("Credits vs. Deductions", "A deduction reduces the income you're taxed on. A credit reduces the tax itself. A dollar of credit is worth far more than a dollar of deduction — which is why missing one hurts."),
            ("The Research Credit", "Businesses that develop or improve products, processes, or software may qualify for a research credit — and the definition is broader than many owners assume. Worth investigating if you build anything."),
            ("Hiring-Related Credits", "Credits like the Work Opportunity Tax Credit reward hiring from certain groups. If you're hiring anyway, you may be leaving money on the table by not checking eligibility."),
            ("Retirement Plan Startup Credit", "Small businesses that set up a retirement plan can claim a credit for the startup costs. See the <a href=\"https://www.irs.gov/retirement-plans/retirement-plans-startup-costs-tax-credit\" rel=\"noopener\" target=\"_blank\">IRS startup cost credit page</a>."),
            ("Finding the Ones You Qualify For", "Credits are specific and easy to miss. Reviewing eligibility with a professional often uncovers savings that more than cover the review itself."),
        ],
    },
    {
        "slug": "year-end-tax-moves",
        "cat": "Tax Planning",
        "title": "Year-End Tax Moves to Make Before December 31",
        "desc": "Smart tax moves small businesses can make before year-end to lower their bill, from timing income to funding retirement accounts.",
        "keywords": "year-end tax moves, year-end tax planning, defer income, small business tax strategy",
        "read": "5 min read",
        "lede": "The last weeks of the year are your final window to influence your tax bill. A few deliberate moves before December 31 can pay off in April.",
        "sections": [
            ("Time Your Income and Expenses", "If you expect a lower-tax year ahead, you may defer income into January and pull deductible expenses into December. Cash-basis businesses have the most flexibility here."),
            ("Make Needed Purchases", "If you genuinely need equipment, buying and placing it in service before year-end can unlock a current-year deduction under Section 179, as covered in our equipment guide."),
            ("Fund Retirement Accounts", "Contributing to a SEP-IRA or Solo 401(k) lowers taxable income while building your future. Some deadlines fall at or after year-end, but planning happens now."),
            ("Review Your Books", "A year-end review catches missed deductions, miscategorized expenses, and surprises while there's still time to act. Don't wait for your preparer to find them in April."),
            ("Check Your Estimated Payments", "Make sure you've paid enough through the year to avoid a penalty. A catch-up payment before the deadline can save you interest."),
        ],
    },
    {
        "slug": "choosing-business-entity",
        "cat": "Business Structure",
        "title": "Choosing a Business Entity: Sole Proprietor, LLC, or Corporation",
        "desc": "A comparison of the main business entity types, their tax treatment, liability protection, and which fits different kinds of small businesses.",
        "keywords": "business entity, sole proprietorship, LLC, corporation, choosing business structure",
        "read": "6 min read",
        "lede": "Your business structure affects your taxes, your liability, and your paperwork for as long as you operate. It's worth choosing on purpose, not by default.",
        "sections": [
            ("Sole Proprietorship", "The simplest structure — no formation needed, all profit flows to your personal return. The catch is no liability protection: your personal assets are exposed if the business is sued."),
            ("Limited Liability Company (LLC)", "An LLC adds a legal shield between you and the business while keeping tax treatment flexible. It's the popular middle ground for most small businesses starting out."),
            ("Corporations (C and S)", "Corporations offer strong liability protection and specific tax treatments. An S-Corp election can reduce self-employment tax; a C-Corp is usually for businesses with different growth or investment plans."),
            ("Weighing Liability vs. Simplicity", "More protection generally means more paperwork. The right balance depends on your risk, income, and growth plans — there's no universal best answer."),
            ("Revisit as You Grow", "The structure that fit at launch may not fit at scale. Reviewing your entity as income and complexity grow keeps it working in your favor. The <a href=\"https://www.sba.gov/business-guide/launch-your-business/choose-business-structure\" rel=\"noopener\" target=\"_blank\">SBA structure guide</a> is a solid overview."),
        ],
    },
    {
        "slug": "personal-tax-tips",
        "cat": "Individual Taxes",
        "title": "10 Tax Tips for Individuals Filing on Their Own",
        "desc": "Practical tax tips for individuals, from choosing the standard deduction to timing charitable gifts and avoiding common filing mistakes.",
        "keywords": "individual tax tips, personal taxes, standard deduction, itemizing, tax filing tips",
        "read": "6 min read",
        "lede": "You don't have to run a business to leave money on the table. These are the tax basics that help ordinary filers keep more of what they earn.",
        "sections": [
            ("Standard Deduction vs. Itemizing", "Most filers now take the standard deduction because it's larger than their itemized total. But if you have significant mortgage interest, state taxes, or charitable giving, run both ways and take whichever is bigger."),
            ("Don't Miss Above-the-Line Deductions", "Certain deductions — like student loan interest, HSA contributions, and self-employed health insurance — reduce your income even if you take the standard deduction. They're easy to overlook."),
            ("Contribute to Tax-Advantaged Accounts", "IRA and HSA contributions can lower your taxable income, and some can be made right up until the filing deadline. The <a href=\"https://www.irs.gov/retirement-plans/individual-retirement-arrangements-iras\" rel=\"noopener\" target=\"_blank\">IRS IRA page</a> explains the limits."),
            ("Time Your Charitable Giving", "Bunching several years of donations into one year can push you over the itemizing threshold in that year. A donor-advised fund is one tool people use for this."),
            ("Check Your Withholding", "A giant refund means you lent the government money interest-free all year; a big bill means a possible penalty. Adjusting your W-4 aims you toward break-even, where your money stays in your pocket."),
            ("Keep Good Records", "Save documents supporting income, deductions, and credits. If a return is ever questioned, records are what turn a stressful notice into a quick reply."),
        ],
    },
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | {firm}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<meta name="author" content="{author}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{site}/{slug}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="{firm}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{site}/{slug}">
<meta property="og:image" content="{site}/images/{slug}.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{site}/images/{slug}.jpg">
<script type="application/ld+json">
{jsonld}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root{{
    --ink:#12261f;--ink-soft:#3d5148;--paper:#faf8f3;--paper-alt:#f0ece1;
    --accent:#1f6f54;--accent-deep:#164634;--rule:#d9d2c2;--gold:#b08423;
  }}
  *{{box-sizing:border-box;margin:0;padding:0}}
  html{{scroll-behavior:smooth}}
  body{{font-family:'Inter',system-ui,sans-serif;color:var(--ink);background:var(--paper);line-height:1.7;font-size:1.06rem;-webkit-font-smoothing:antialiased}}
  .wrap{{max-width:720px;margin:0 auto;padding:0 24px}}
  header{{border-bottom:1px solid var(--rule);background:var(--paper)}}
  .masthead{{display:flex;align-items:center;justify-content:space-between;padding:20px 0}}
  .brand{{font-family:'Fraunces',serif;font-weight:600;font-size:1.25rem;letter-spacing:-0.01em;color:var(--ink);text-decoration:none;display:flex;align-items:baseline;gap:8px}}
  .brand .mark{{color:var(--gold)}}
  .nav a{{color:var(--ink-soft);text-decoration:none;font-size:.92rem;font-weight:500;margin-left:24px}}
  .nav a:hover{{color:var(--accent)}}
  @media(max-width:560px){{.nav{{display:none}}}}
  .eyebrow{{font-size:.78rem;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);margin:56px 0 20px}}
  h1{{font-family:'Fraunces',serif;font-weight:600;font-size:clamp(2.1rem,5vw,3.1rem);line-height:1.08;letter-spacing:-0.02em;color:var(--ink);margin-bottom:22px}}
  .lede{{font-size:1.2rem;color:var(--ink-soft);line-height:1.6;margin-bottom:28px}}
  .byline{{display:flex;align-items:center;gap:12px;flex-wrap:wrap;padding:16px 0;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);font-size:.9rem;color:var(--ink-soft)}}
  .byline strong{{color:var(--ink);font-weight:600}}
  .dot{{width:4px;height:4px;border-radius:50%;background:var(--gold)}}
  article{{padding:8px 0 40px}}
  article h2{{font-family:'Fraunces',serif;font-weight:600;font-size:1.6rem;line-height:1.2;color:var(--accent-deep);margin:44px 0 14px;letter-spacing:-0.01em}}
  article h2 .num{{color:var(--gold);font-size:1rem;font-weight:600;display:block;margin-bottom:4px;letter-spacing:.05em}}
  article p{{margin-bottom:20px}}
  article a{{color:var(--accent);text-decoration:underline;text-underline-offset:2px}}
  blockquote{{border-left:3px solid var(--gold);background:var(--paper-alt);padding:18px 22px;margin:28px 0;font-family:'Fraunces',serif;font-size:1.15rem;color:var(--accent-deep);border-radius:0 6px 6px 0}}
  .cta{{background:var(--accent-deep);color:#f2efe6;border-radius:14px;padding:40px 34px;margin:48px 0;text-align:center}}
  .cta h3{{font-family:'Fraunces',serif;font-weight:600;font-size:1.5rem;margin-bottom:10px;color:#fff}}
  .cta p{{color:#c9d6cf;margin-bottom:24px;font-size:1rem}}
  .btn{{display:inline-block;background:var(--gold);color:#1a1405;font-weight:600;text-decoration:none;padding:14px 30px;border-radius:8px;font-size:1rem;transition:transform .15s ease}}
  .btn:hover{{transform:translateY(-2px)}}
  .related{{margin:48px 0;padding-top:8px}}
  .related h3{{font-family:'Fraunces',serif;font-weight:600;font-size:1.3rem;color:var(--accent-deep);margin-bottom:16px}}
  .related ul{{list-style:none}}
  .related li{{margin-bottom:10px}}
  .related a{{color:var(--accent);text-decoration:none;font-weight:500}}
  .related a:hover{{text-decoration:underline}}
  footer{{border-top:1px solid var(--rule);background:var(--paper-alt);padding:36px 0;font-size:.88rem;color:var(--ink-soft);text-align:center}}
  footer a{{color:var(--accent);text-decoration:none}}
  @media(prefers-reduced-motion:reduce){{*{{scroll-behavior:auto}}.btn{{transition:none}}}}
  :focus-visible{{outline:2px solid var(--gold);outline-offset:3px;border-radius:3px}}
</style>
</head>
<body>
<header>
  <div class="wrap masthead">
    <a href="../index.html" class="brand">{firm}<span class="mark">.</span></a>
    <nav class="nav">
      <a href="../index.html">Home</a>
      <a href="../services.html">Services</a>
      <a href="index.html">Articles</a>
      <a href="../contact.html">Contact</a>
    </nav>
  </div>
</header>
<main class="wrap">
  <p class="eyebrow">{cat}</p>
  <h1>{title}</h1>
  <p class="lede">{lede}</p>
  <div class="byline">
    <span>By <strong>{author}</strong></span>
    {datespan}<span class="dot"></span><span>{read}</span>
  </div>
  <article>
{body}
    <div class="cta">
      <h3>Have a question about your situation?</h3>
      <p>Book a free 20-minute consultation and we'll walk through it together.</p>
      <a href="../contact.html" class="btn">Schedule a Consultation</a>
    </div>
    <p><em>This article is for general information and isn't specific tax or financial advice. Every situation is different &mdash; reach out and we'll look at yours directly.</em></p>
  </article>
  <nav class="related">
    <h3>Related Articles</h3>
    <ul>
{related}
    </ul>
  </nav>
</main>
<footer>
  <div class="wrap">
    <p><strong>{firm}</strong> &mdash; Accounting, Controller &amp; CFO Advisory Services</p>
    <p style="margin-top:8px">{contactline}</p>
  </div>
</footer>
</body>
</html>
"""

def build(outdir=None):
    global OUT
    if outdir: OUT = outdir
    os.makedirs(OUT, exist_ok=True)
    n = len(ARTICLES)

    contact_bits = []
    if LOCATION: contact_bits.append(LOCATION)
    contact_bits.append(f'<a href="mailto:{EMAIL}">{EMAIL}</a>')
    if PHONE: contact_bits.append(f'<a href="tel:{PHONE}">{PHONE}</a>')
    contactline = " &nbsp;&middot;&nbsp; ".join(contact_bits)

    datespan = ('<span class="dot"></span><span>' + PUBDATE + '</span>\n    ') if SHOW_DATE else ''

    for i, a in enumerate(ARTICLES):
        body_parts = []
        for j, (h, p) in enumerate(a["sections"], 1):
            body_parts.append(
                f'    <h2><span class="num">{j:02d}</span>{html.escape(h)}</h2>\n    <p>{p}</p>')
        body = "\n".join(body_parts)

        rel = []
        for k in range(1, 4):
            r = ARTICLES[(i + k) % n]
            rel.append(f'      <li><a href="{r["slug"]}.html">{html.escape(r["title"])}</a></li>')
        related = "\n".join(rel)

        jsonld = json.dumps({
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": a["title"],
            "description": a["desc"],
            "author": {"@type": "Organization", "name": AUTHOR},
            "publisher": {"@type": "Organization", "name": FIRM,
                          "logo": {"@type": "ImageObject", "url": f"{SITE}/logo.png"}},
            "datePublished": PUBDATE,
            "dateModified": PUBDATE,
            "mainEntityOfPage": f"{SITE}/articles/{a['slug']}",
        }, indent=2)

        page = TEMPLATE.format(
            title=html.escape(a["title"]), desc=html.escape(a["desc"]),
            keywords=html.escape(a["keywords"]), site=SITE, slug=a["slug"],
            cat=html.escape(a["cat"]), lede=html.escape(a["lede"]), read=a["read"],
            body=body, related=related, jsonld=jsonld,
            firm=FIRM, author=AUTHOR, datespan=datespan, contactline=contactline,
        )
        with open(os.path.join(OUT, f"{a['slug']}.html"), "w") as fh:
            fh.write(page)
    print(f"Generated {n} articles -> {OUT}")
    return ARTICLES

# ---------------------------------------------------------------------------
# Self-employed retirement cluster. Kept in its own module so the eight new
# articles are reviewable on their own rather than buried in this file, and so
# the reason each topic exists (a specific Search Console query) stays attached
# to them. See articles_retirement.py for the query data and the sourcing note.
from articles_retirement import ARTICLES as _RETIREMENT
ARTICLES.extend(_RETIREMENT)

# Quarterly estimated tax cluster. Same rationale as the retirement one: eight
# distinct queries were landing on a single page at position 74.2 with 132
# impressions and zero clicks. See articles_quarterly.py for the query data and
# the IRS sourcing note.
from articles_quarterly import ARTICLES as _QUARTERLY
ARTICLES.extend(_QUARTERLY)

SEO_TITLES.update({
    "solo-401k-vs-sep-ira-switch": "When to Move From a SEP-IRA to a Solo 401(k)",
    "403b-vs-sep-ira": "403(b) vs. SEP-IRA: Using Both With a Side Business",
    "sep-ira-contribution-rules": "How a SEP-IRA Contribution Is Actually Calculated",
    "first-year-self-employed-taxes": "First Year Self-Employed: When Quarterly Taxes Start",
    "how-to-calculate-estimated-taxes": "How to Work Out What You Owe in Quarterly Taxes",
    "uneven-income-estimated-taxes": "Estimated Taxes When Your Income Is Uneven",
})

if __name__ == "__main__":
    raise SystemExit(
        "\n  generate_articles_northpeak.py is the DATA MODULE, not a build step.\n"
        "  Running it calls build(), which overwrites all 25 article pages with the\n"
        "  legacy standalone TEMPLATE at the top of this file — no site nav, no\n"
        "  footer, no analytics, and og:image URLs pointing at /images/<slug>.jpg\n"
        "  which do not exist. The real article builder is build_articles_shell.py,\n"
        "  which renders the same ARTICLES data through the shared site shell.\n\n"
        "  Build the site with:  python3 generators/build.py\n"
    )
