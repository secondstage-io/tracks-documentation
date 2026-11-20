---
description: "Build branded, trackable campaign URLs with the Tracking Link Builders in your Ad Ops Helper Sheet."
---

# Tracking Link Builders

<p class="docs-audience">For: Marketing / Ad ops</p>

The **Tracking Link Builders** are a suite of tools located within your project's **Ad Ops Helper Sheet** (see the [Ad Ops Guide](adopshelper.md) if you don't have the sheet yet). They allow you to generate branded, trackable URLs for every aspect of your marketing mix—from influencer partnerships to direct media buys and organic content.

These builders serve two main purposes:

* **Branding:** They turn long, complex tracking URLs into clean "vanity" links (e.g., `connect.yourgame.com/contentcreator`) that are safe and professional to share publicly.
* **Attribution:** They automatically append all necessary parameters and tracking logic, ensuring that clicks (whether from a YouTube description or a PR article) are correctly attributed to installs and in-game events.

There are three distinct builders available, depending on your campaign type:

1.  **Influencer Link Builder:** For content creators and streamers.
2.  **Media Houses (Direct Buy):** For display ads, DOOH, and paid placements on gaming sites.
3.  **Organic Media:** For owned channels (blogs, social) and earned media (PR).

---

## Influencer Link Builder

Use this tab for influencer marketing campaigns where you are sending links to specific creators to share with their audience.

### How to Configure

1.  **Set the Global Destination**
    At the top of the sheet, locate the **Paste Destination URL** field. Enter the main landing page URL (e.g., your game's website).
    !!! note
        This destination applies to **all** links generated in this specific tab.

2.  **Input Campaign Details**
    Fill in the **Yellow Highlighted Cells** for each influencer. Use the dropdowns to ensure data consistency:
    * **Creator Name:** The name of the influencer.
    * **Platform:** Where the link will be shared (e.g., YouTube, Twitch).
    * **Content Type:** The format (e.g., Video, Short, Stream).
    * **Beat / Phase:** The campaign phase (e.g., Announce Beat).

3.  **Create the Short Key (Mandatory)**
    In **Column J**, enter a unique name for the link (e.g., the creator's name like `Pokimane` or `Shroud`).

4.  **Get Your Link**
    The sheet will generate a **Short Link** in the black column on the right. This is the branded link you should send to the influencer.

!!! warning "Important"
    Do not use special characters or spaces in the Short Key.

---

## Media Houses (Direct Buy) Link Builder

Use this tab for paid media placements that are not programmatic. This includes direct buys on gaming websites (e.g., IGN, Polygon), banner ads, or Digital Out-of-Home (DOOH) displays.

### How to Configure

1.  **Set the Global Destination**
    Similar to the Influencer builder, enter your target landing page in the **Paste Destination URL** field at the top of the sheet.

2.  **Input Media Details**
    Fill in the **Yellow Highlighted Cells** to define the placement:
    * **Media House Name:** The publisher or vendor (e.g., Polygon, TheGamer).
    * **Placement:** The specific slot (e.g., Sponsored Post, Banner).
    * **Strategy:** The goal of the buy (e.g., Awareness, Conversion).

3.  **Create the Short Key**
    In **Column J**, enter a unique identifier (e.g., `polygon_article`). This is required to generate the tracking logic.

### Output Options

* **Branded Short Link:** Use this for static placements (e.g., a sponsored article) where the URL is visible to users.
* **Long Link (for Dynamic Ad Ops):** If the publisher requires a raw URL to inject their own dynamic macros (such as dynamic country codes or timestamps), provide them with the **Long Link**.
  
!!! tip
    You can create multiple long URLs for different publisher activations if needed.

---

## Organic Media (Owned & Earned) Link Builder

Use this tab for your own marketing channels (Social Media, Dev Blogs, Newsletters) or PR efforts.

!!! abstract "Key Difference"
    Unlike the other builders, the **Organic Builder allows you to set a different destination URL for every single row**. This means you are able to send users not only to a campaign landing page, but also to other content like YouTube trailers, blog posts, Steam pages, or media articles.

### How to Configure

1.  **Define the Activity**
    Fill in the yellow cells to categorize the link (e.g., **Activity:** News, **Placement:** Blog).

2.  **Set the Target URL**
    Locate **Column F (Green Column): Target URL**. Paste the exact destination where you want the user to land for this specific link (e.g., a specific blog post URL or a store page).

3.  **Create the Short Key**
    In **Column G**, give your link a name (e.g., `blog_article`, `announce`, `steam_news`).

4.  **Get Your Link**
    Copy the **Short Link** from the column on the far right. Using these links in your press releases or social bio ensures that users who click through and eventually install the game are tracked correctly.

---

## Troubleshooting & FAQ

**Why is my link not appearing?**
Ensure you have filled out the **Short Key** column. The system cannot generate a branded URL without a unique key.

**Can I use spaces in the Short Key?**
No. Please use underscores (`_`) or hyphens (`-`) instead of spaces.

**My Organic link is going to the wrong page.**
Check **Column F (Target URL)** in the Organic Media tab. Ensure you pasted the correct specific URL for that row, rather than a generic homepage link.
