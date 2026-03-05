from __future__ import annotations

from .models import LaunchKitOutput, LaunchProjectCreate

SUPPORTED_TONES = {"clear", "confident", "playful", "technical"}


def generate_launch_kit(brief: LaunchProjectCreate) -> LaunchKitOutput:
    tone = brief.tone.lower().strip()
    if tone not in SUPPORTED_TONES:
        raise ValueError(
            f"Unsupported tone '{brief.tone}'. Use one of: {', '.join(sorted(SUPPORTED_TONES))}."
        )

    landing = {
        "headline": f"{brief.product_name}: {brief.one_liner}",
        "subheadline": f"Built for {brief.target_audience.lower()} to {brief.launch_goal.lower()}.",
        "primary_cta": "Get early access",
        "key_bullets": [
            f"Tone: {tone}",
            f"Audience fit: {brief.target_audience}",
            f"Launch goal: {brief.launch_goal}",
        ],
    }

    product_hunt = {
        "tagline": brief.one_liner,
        "first_comment": (
            f"Hey Product Hunt 👋 We built {brief.product_name} for {brief.target_audience.lower()}. "
            f"Our goal: {brief.launch_goal.lower()}."
        ),
        "cta": "Try it and share feedback",
    }

    x_thread = {
        "hook": f"We built {brief.product_name} to solve one painful launch problem.",
        "tweets": [
            f"1/ {brief.one_liner}",
            f"2/ Built for: {brief.target_audience}",
            f"3/ Goal: {brief.launch_goal}",
            "4/ Want early access? Reply 'launch'.",
        ],
        "cta": "DM for invite",
    }

    email_sequence = [
        {
            "subject": f"{brief.product_name} is live for early users",
            "body": f"{brief.one_liner} Built for {brief.target_audience.lower()}.",
        },
        {
            "subject": f"How {brief.product_name} helps you ship faster",
            "body": f"If you want to {brief.launch_goal.lower()}, this is for you.",
        },
        {
            "subject": "Last call: join our launch cohort",
            "body": "We're closing early access this week. Reply to secure your spot.",
        },
    ]

    return LaunchKitOutput(
        landing_page=landing,
        product_hunt=product_hunt,
        x_thread=x_thread,
        email_sequence=email_sequence,
    )
