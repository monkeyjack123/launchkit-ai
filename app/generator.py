from __future__ import annotations

from .models import LaunchKitOutput, LaunchProjectCreate

SUPPORTED_TONES = {"clear", "confident", "playful", "technical"}


def _build_landing_page(brief: LaunchProjectCreate, tone: str) -> dict[str, object]:
    return {
        "headline": f"{brief.product_name}: {brief.one_liner}",
        "subheadline": f"Built for {brief.target_audience.lower()} to {brief.launch_goal.lower()}.",
        "primary_cta": "Get early access",
        "proof_points": [
            "No fake metrics or unverified claims.",
            "Concrete problem-to-outcome framing.",
            "One clear CTA for launch conversion.",
        ],
        "key_bullets": [
            f"Tone: {tone}",
            f"Audience fit: {brief.target_audience}",
            f"Launch goal: {brief.launch_goal}",
        ],
    }


def _build_product_hunt(brief: LaunchProjectCreate) -> dict[str, str]:
    tagline = brief.one_liner[:60].rstrip()
    first_comment = (
        f"Hey Product Hunt 👋 We built {brief.product_name} for {brief.target_audience.lower()} to "
        f"{brief.launch_goal.lower()}. We're sharing the real scope and would love candid feedback."
    )
    return {
        "tagline": tagline,
        "first_comment": first_comment,
        "launch_checklist": "Demo, pricing, and setup details are verified before posting.",
        "cta": "Try it and share feedback",
    }


def generate_launch_kit(brief: LaunchProjectCreate) -> LaunchKitOutput:
    tone = brief.tone.lower().strip()
    if tone not in SUPPORTED_TONES:
        raise ValueError(
            f"Unsupported tone '{brief.tone}'. Use one of: {', '.join(sorted(SUPPORTED_TONES))}."
        )

    landing = _build_landing_page(brief, tone)

    product_hunt = _build_product_hunt(brief)

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
