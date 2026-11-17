import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="Marketing AI Chatbot", page_icon="📈")
st.title("📈 Marketing AI Chatbot")
st.caption("Ask questions using the supplied Marketing knowledge base.")

try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    api_key = ""

manual = """
To power a marketing chatbot that answers users' questions accurately across any scenario, its knowledge base should be structured around **Core Frameworks**, **Channels (Where)**, **Execution (How)**, **Timing (When)**, and **Analytics (Measurement)**.

Below is a comprehensive, modular knowledge architecture designed specifically to be fed into a chatbot's knowledge base, RAG (Retrieval-Augmented Generation) system, or conversational decision trees.

---

## 1. Core Marketing Foundations (The "What" & "Why")

Your chatbot needs these foundational concepts to advise users before jumping into tactics.

* **The Marketing Funnel (AIDA / AARRR):**
* **Awareness (Top of Funnel / TOFU):** Attracting strangers via broad educational content, SEO, and social media.
* **Consideration (Middle of Funnel / MOFU):** Nurturing interest via lead magnets, webinars, case studies, and email sequences.
* **Conversion (Bottom of Funnel / BOFU):** Closing the sale via demos, free trials, reviews, and limited-time offers.
* **Retention & Advocacy:** Keeping customers via onboarding, loyalty programs, and referral incentives.


* **The 7 Ps of the Marketing Mix:**
* **Product:** Features, quality, branding, and problem-solving value.
* **Price:** Penetration, skimming, value-based, freemium, or tiered pricing.
* **Place:** Distribution channels (e-commerce, retail, SaaS, marketplaces).
* **Promotion:** Advertising, PR, content, and sales outreach.
* **People:** Customer service, sales teams, and brand advocates.
* **Process:** Customer journey friction, checkout speed, and delivery systems.
* **Physical Evidence:** Website UI/UX, packaging, testimonials, and social proof.


* **Targeting & Positioning:**
* **STP Model:** **S**egmentation (demographics, psychographics, behavior), **T**argeting (selecting the most profitable segment), and **P**ositioning (crafting the Unique Value Proposition).
* **ICP & Buyer Personas:** Defining the Ideal Customer Profile (for B2B) and individual decision-maker pain points, goals, and objections.



---

## 2. Marketing Channels (The "Where")

Organize your chatbot's channel knowledge into the **PESO Model** (Paid, Earned, Shared, Owned).

| Category | Channels | Best Used For |
| --- | --- | --- |
| **Owned Media** *(Full Control)* | Website, Blog, Email Newsletter, Mobile App, SMS/WhatsApp Lists, Podcasts | Long-term brand equity, lead capture, high-converting nurture sequences, and SEO traffic. |
| **Paid Media** *(Fast Scale)* | Google Search/Shopping Ads, Meta (Facebook/Instagram) Ads, LinkedIn Ads, YouTube Ads, TikTok Ads, Programmatic Display | Immediate traffic, testing new offers, retargeting warm leads, and precise demographic/intent targeting. |
| **Shared Media** *(Community)* | Instagram, LinkedIn, X (Twitter), TikTok, YouTube, Reddit, Facebook Groups | Brand personality, organic discovery, community building, and two-way customer engagement. |
| **Earned Media** *(Trust)* | PR/Press Releases, Guest Blogs, Influencer Mentions, Customer Reviews (Google/G2/Trustpilot), Word-of-Mouth | High-trust social proof, backlinks for SEO, and third-party validation. |

---

## 3. Execution Playbooks (The "How")

Equip your bot with step-by-step tactical workflows for the major marketing disciplines:

### A. Content Marketing & SEO

* **How to do it:** Conduct keyword research (search volume vs. keyword difficulty) $\rightarrow$ Map keywords to search intent (informational, navigational, transactional) $\rightarrow$ Create "Pillar Pages" (comprehensive guides) supported by "Cluster Content" (specific subtopics) $\rightarrow$ Optimize on-page SEO (titles, meta descriptions, headers, internal links) $\rightarrow$ Build authoritative backlinks.
* **Content Formats:** How-to guides, comparison articles ("X vs. Y"), original research/data, video tutorials, infographics, and downloadable templates.

### B. Paid Acquisition (Performance Marketing)

* **How to do it:** Define campaign objective (Leads, Sales, Traffic) $\rightarrow$ Install tracking pixels/conversion APIs $\rightarrow$ Build audience segments (Cold/Lookalike vs. Warm Retargeting) $\rightarrow$ Create 3–5 ad variations (testing hooks, visuals, and CTAs) $\rightarrow$ Launch with a test budget $\rightarrow$ Kill underperforming ads after 48–72 hours and scale winners.
* **Copywriting Frameworks for Ads/Landing Pages:**
* **PAS:** **P**roblem $\rightarrow$ **A**gitate $\rightarrow$ **S**olution.
* **BAB:** **B**efore (current pain) $\rightarrow$ **A**fter (desired state) $\rightarrow$ **B**ridge (your product).



### C. Email & Lifecycle Marketing

* **How to do it:** Offer a high-value Lead Magnet (ebook, checklist, discount code) $\rightarrow$ Trigger an automated **Welcome Sequence** (3–5 emails delivering value before pitching) $\rightarrow$ Segment subscribers by behavior (clicks, purchase history) $\rightarrow$ Send regular value newsletters and behavioral triggers (abandoned cart, win-back campaigns).

### D. Social Media & Community Growth

* **How to do it:** Pick 1–2 primary platforms where the target audience hangs out $\rightarrow$ Follow the **80/20 Rule** (80% educate, entertain, or inspire; 20% promote) $\rightarrow$ Use short-form video (Reels/Shorts/TikTok) for reach and carousels/threads for depth $\rightarrow$ Engage in comments and DMs within the first hour of posting.

---

## 4. Timing & Cadence (The "When")

Users frequently ask chatbots *when* to launch, post, or send campaigns. Include these rules:

* **Business Lifecycle Timing:**
* **Pre-Launch / Validation:** Focus on customer interviews, waitlist landing pages, organic social building, and small-budget paid ads to test messaging.
* **Early Traction (0–100 customers):** Do things that don't scale—direct outreach, community participation, partnerships, and founder-led content.
* **Growth & Scaling:** Invest heavily in repeatable paid acquisition, SEO content engines, referral loops, and marketing automation.


* **Channel Cadence & Optimal Windows:**
* **Email:** B2B performs best Tuesday–Thursday mornings (9 AM–11 AM local time); B2C performs well evenings and weekends. Send 1–4 times per month minimum to stay top-of-mind without causing unsubscribes.
* **Social Media:** LinkedIn (weekdays during business hours, 3–5x/week); Instagram/TikTok (evenings and lunch breaks, 4–7x/week); YouTube (1–2x/week long-form, daily Shorts).
* **SEO vs. Paid Ads:** Run **Paid Ads** when you need leads *today* or want to validate a new offer quickly. Invest in **SEO** immediately knowing it takes 3–6+ months to compound into free, sustainable traffic.


* **Seasonal & Event Triggers:** Plan campaigns 4–8 weeks ahead of major retail peaks (Diwali, Black Friday/Cyber Monday, New Year, Back-to-School) and industry-specific conferences.

---

## 5. Measurement & Optimization (The "Metrics")

A marketing chatbot must help users diagnose what is working and what is broken.

* **Top-of-Funnel Metrics:** Impressions, Reach, Organic Traffic, Click-Through Rate (CTR).
* **Mid-Funnel Metrics:** Lead Conversion Rate, Cost Per Lead (CPL), Email Open Rate, Engagement Rate.
* **Bottom-of-Funnel & Financial Metrics:**
* **CAC (Customer Acquisition Cost):** Total Marketing & Sales Spend $\div$ New Customers Acquired.
* **LTV (Customer Lifetime Value):** Average Order Value $\times$ Purchase Frequency $\times$ Customer Lifespan. *(Healthy benchmark: LTV should be at least 3x CAC).*
* **ROAS (Return on Ad Spend):** Revenue from Ads $\div$ Ad Spend.
* **Churn Rate:** Percentage of customers who cancel or stop buying over a given period.


* **How to Diagnose Funnel Leaks:**
* *High Impressions, Low CTR* $\rightarrow$ Fix the **Hook, Headline, or Ad Creative**.
* *High CTR, Low Landing Page Conversions* $\rightarrow$ Fix **Message Match, Page Speed, Offer Clarity, or Social Proof**.
* *High Cart/Checkout Abandonment* $\rightarrow$ Fix **Unexpected Costs (shipping), Trust Signals, or Checkout Friction**.



---

## 6. Structuring This for Your Chatbot

To make your chatbot genuinely smart rather than a wall of text, structure its prompt/knowledge base using these layers:

1. **System Role & Tone:** Instruct the bot to act as a pragmatic Chief Marketing Officer (CMO) that always asks 2–3 clarifying questions first (e.g., *B2B or B2C? Budget? Target audience?*) before giving tailored advice.
2. **Intent Routing:** Tag your knowledge documents by intent (`[STRATEGY]`, `[COPYWRITING]`, `[PAID_ADS]`, `[SEO]`, `[METRICS]`) so your retrieval system pulls the exact framework needed.
3. **Output Guardrails:** Force the bot to provide actionable steps, concrete examples, and templates rather than vague theory.
"""

system_prompt = """
You are a Marketing AI Assistant designed to help students, beginners and
business owners. Answer strictly using the Marketing knowledge provided in the
contents. Explain concepts in simple language. Keep answers concise unless
detail is requested. Use tables for comparisons where appropriate. State
formulas clearly. For channel, timing or metric questions, give clear and
actionable steps. Use numbered points or bullets for lists. Do not invent
facts, examples or calculations unsupported by the knowledge base. If the
answer is unavailable, say: "Sorry, this information is not available in my
Marketing knowledge base." Stay polite, relevant and user-friendly.
"""

with st.sidebar:
    st.header("Settings")
    model_name = st.text_input("Gemini model", "gemini-3.5-flash-lite")
    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.rerun()

if not api_key or api_key == "YOUR_GEMINI_API_KEY":
    st.warning("Add your Gemini API key to `.streamlit/secrets.toml`, then restart the app.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

question = st.chat_input("Ask a Marketing question...")
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    try:
        client = genai.Client(api_key=api_key)
        history = "\n\n".join(
            f'{m["role"].upper()}: {m["content"]}'
            for m in st.session_state.messages
        )
        response = client.models.generate_content(
            model=model_name,
            contents=manual + "\n\nConversation:\n" + history,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.2
            )
        )
        answer = response.text or "I couldn't generate an answer. Please try again."
        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.markdown(answer)
    except Exception as exc:
        st.error(f"Gemini request failed: {exc}")
