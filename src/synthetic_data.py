thonimport datetime as _dt
import hashlib
import math
import random
from typing import Any, Dict, List

_COUNTRIES = ["US", "GB", "DE", "FR", "CA", "AU", "IN", "JP", "BR", "NL"]
_TECH_STACK = [
    "nginx",
    "apache",
    "cloudflare",
    "react",
    "vue",
    "angular",
    "django",
    "flask",
    "laravel",
    "wordpress",
]

def _rng_for_domain(domain: str) -> random.Random:
    digest = hashlib.sha256(domain.encode("utf-8")).hexdigest()
    seed = int(digest[:16], 16)
    return random.Random(seed)

def _normalize(weights: List[float]) -> List[float]:
    total = sum(weights)
    if total <= 0:
        return [1.0 / len(weights)] * len(weights)
    return [w / total for w in weights]

def _generate_age_distribution(rng: random.Random) -> List[Dict[str, Any]]:
    buckets = [
        (18, 24),
        (25, 34),
        (35, 44),
        (45, 54),
        (55, 64),
        (65, 100),
    ]
    weights = [rng.uniform(0.1, 1.0) for _ in buckets]
    normalized = _normalize(weights)
    return [
        {"minAge": low, "maxAge": high, "value": round(val, 3)}
        for (low, high), val in zip(buckets, normalized)
    ]

def _generate_gender_distribution(rng: random.Random) -> Dict[str, float]:
    male = rng.uniform(0.4, 0.7)
    female = 1.0 - male
    return {"male": round(male, 3), "female": round(female, 3)}

def _generate_geography(rng: random.Random) -> Dict[str, Any]:
    weights = [rng.uniform(0.1, 1.0) for _ in _COUNTRIES]
    shares = _normalize(weights)
    countries = [
        {"countryAlpha2Code": code, "visitsShare": round(share, 3)}
        for code, share in zip(_COUNTRIES, shares)
    ]
    return {"topCountriesTraffics": countries}

def _generate_traffic(rng: random.Random, base_visits: int) -> Dict[str, Any]:
    today = _dt.date.today().replace(day=1)
    months: List[Dict[str, Any]] = []
    for i in range(12):
        month_date = today - _dt.timedelta(days=30 * (11 - i))
        factor = 1 + rng.uniform(-0.15, 0.15)
        visits = max(int(base_visits * factor), 1)
        months.append(
            {
                "date": month_date.strftime("%Y-%m"),
                "visits": visits,
            }
        )

    visits_total = sum(m["visits"] for m in months)
    return {
        "historical": months,
        "visitsTotalCount": visits_total,
    }

def _generate_traffic_sources(rng: random.Random) -> Dict[str, float]:
    channels = ["direct", "search", "social", "referrals", "ads", "mail"]
    weights = [rng.uniform(0.2, 1.0) for _ in channels]
    shares = _normalize(weights)
    return {ch: round(share, 3) for ch, share in zip(channels, shares)}

def _generate_ranking(rng: random.Random) -> Dict[str, Any]:
    global_rank = rng.randint(100, 50000)
    country_rank = rng.randint(10, 10000)
    category_rank = rng.randint(10, 20000)
    return {
        "globalRank": global_rank,
        "countryRank": country_rank,
        "categoryRank": category_rank,
    }

def _generate_competitors(rng: random.Random, domain: str, base_visits: int) -> Dict[str, Any]:
    base_name = domain.split(".")[0]
    candidates = [
        f"{base_name}{suffix}.com"
        for suffix in ["app", "pro", "plus", "online", "site"]
    ]
    rng.shuffle(candidates)
    competitors: List[Dict[str, Any]] = []
    for i, comp_domain in enumerate(candidates[:5]):
        factor = 1 + rng.uniform(-0.5, 0.5)
        visits = max(int(base_visits * factor), 1)
        similarity = round(0.9 - 0.1 * i + rng.uniform(-0.05, 0.05), 3)
        similarity = max(0.1, min(similarity, 0.99))
        competitors.append(
            {
                "domain": comp_domain,
                "visitsTotalCount": visits,
                "similarityScore": similarity,
            }
        )
    return {"topSimilarityCompetitors": competitors}

def _generate_interests(rng: random.Random) -> List[Dict[str, Any]]:
    categories = [
        "Technology",
        "News & Media",
        "E-commerce",
        "Social Networks",
        "Finance",
        "Travel",
        "Gaming",
        "Education",
    ]
    rng.shuffle(categories)
    interests = []
    for idx, cat in enumerate(categories[:5]):
        score = round(0.9 - 0.1 * idx + rng.uniform(-0.05, 0.05), 3)
        score = max(0.1, min(score, 0.99))
        interests.append({"category": cat, "affinityScore": score})
    return interests

def _generate_technologies(rng: random.Random) -> List[str]:
    techs = list(_TECH_STACK)
    rng.shuffle(techs)
    count = rng.randint(3, 7)
    return techs[:count]

def _generate_recent_ads(rng: random.Random, domain: str) -> List[Dict[str, Any]]:
    ads: List[Dict[str, Any]] = []
    for i in range(3):
        ads.append(
            {
                "id": f"{domain.replace('.', '-')}-ad-{i+1}",
                "title": f"{domain} Campaign #{i+1}",
                "imageUrl": f"https://cdn.example.com/{domain}/ads/{i+1}.png",
                "clickUrl": f"https://{domain}/?utm_campaign=ad-{i+1}",
            }
        )
    return ads

def _generate_searches_source(rng: random.Random) -> Dict[str, Any]:
    organic = rng.uniform(0.4, 0.9)
    paid = 1.0 - organic
    return {
        "organicShare": round(organic, 3),
        "paidShare": round(paid, 3),
        "topKeywords": [
            {"keyword": "brand", "share": round(rng.uniform(0.05, 0.2), 3)},
            {"keyword": "login", "share": round(rng.uniform(0.05, 0.2), 3)},
        ],
    }

def _generate_referrals(rng: random.Random) -> Dict[str, Any]:
    referrers = []
    for i in range(5):
        ref_domain = f"referrer{i+1}.example.com"
        share = round(rng.uniform(0.01, 0.1), 3)
        referrers.append({"domain": ref_domain, "share": share})
    return {"topReferrals": referrers}

def _generate_ads_source(rng: random.Random) -> Dict[str, Any]:
    networks = ["Google Ads", "Meta Ads", "Programmatic", "Affiliate"]
    weights = [rng.uniform(0.1, 1.0) for _ in networks]
    shares = _normalize(weights)
    return {
        "networks": [
            {"network": name, "share": round(share, 3)}
            for name, share in zip(networks, shares)
        ]
    }

def _generate_social_sources(rng: random.Random) -> Dict[str, Any]:
    networks = ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube", "TikTok"]
    weights = [rng.uniform(0.1, 1.0) for _ in networks]
    shares = _normalize(weights)
    return {
        "networks": [
            {"network": name, "share": round(share, 3)}
            for name, share in zip(networks, shares)
        ]
    }

def generate_domain_payload(domain: str) -> Dict[str, Any]:
    rng = _rng_for_domain(domain)

    base_visits = rng.randint(2_000_000, 100_000_000)
    traffic = _generate_traffic(rng, base_visits)
    traffic_sources = _generate_traffic_sources(rng)
    ranking = _generate_ranking(rng)
    competitors = _generate_competitors(rng, domain, base_visits)
    age_distribution = _generate_age_distribution(rng)
    gender_distribution = _generate_gender_distribution(rng)
    geography = _generate_geography(rng)
    interests = _generate_interests(rng)
    technologies = _generate_technologies(rng)
    recent_ads = _generate_recent_ads(rng, domain)
    searches_source = _generate_searches_source(rng)
    referrals = _generate_referrals(rng)
    ads_source = _generate_ads_source(rng)
    social_sources = _generate_social_sources(rng)

    bounce_rate = round(rng.uniform(0.15, 0.7), 3)
    pages_per_visit = round(rng.uniform(2.0, 12.0), 2)
    avg_duration_seconds = rng.randint(60, 900)
    duration = _dt.timedelta(seconds=avg_duration_seconds)
    minutes, seconds = divmod(duration.seconds, 60)
    hours, minutes = divmod(minutes, 60)
    visits_total = traffic["visitsTotalCount"]

    overview = {
        "companyName": domain.split(".")[0].capitalize(),
        "visitsTotalCount": visits_total,
        "pagesPerVisit": pages_per_visit,
        "visitsAvgDurationFormatted": f"{hours:02d}:{minutes:02d}:{seconds:02d}",
        "bounceRate": bounce_rate,
    }

    payload: Dict[str, Any] = {
        "domain": domain,
        "overview": overview,
        "interests": interests,
        "competitors": competitors,
        "searchesSource": searches_source,
        "incomingReferrals": referrals,
        "adsSource": ads_source,
        "socialNetworksSource": social_sources,
        "technologies": technologies,
        "recentAds": recent_ads,
        "demographics": {
            "ageDistribution": age_distribution,
            "genderDistribution": gender_distribution,
        },
        "geography": geography,
        "trafficSources": traffic_sources,
        "ranking": ranking,
        "traffic": traffic,
    }

    return payload