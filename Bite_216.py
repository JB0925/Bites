import re

EMAIL_HEADER = """Return-Path: <bounces+5555-7602-redacted-info>
...
Received: by 10.8.49.86 with SMTP id mf9.22328.51C1E5CDF
    Wed, 19 Jun 2013 17:09:33 +0000 (UTC)
Received: from NzI3MDQ (174.37.77.208-static.reverse.softlayer.com [174.37.77.208])
by mi22.sendgrid.net (SG) with HTTP id 13f5d69ac61.41fe.2cc1d0b
for <redacted-info>; Wed, 19 Jun 2013 12:09:33 -0500 (CST)
Content-Type: multipart/alternative;
boundary="===============8730907547464832727=="
MIME-Version: 1.0
From: redacted-address
To: redacted-address
Subject: A Test From SendGrid
Message-ID: <1371661773.974270694268263@mf9.sendgrid.net>
Date: Wed, 19 Jun 2013 17:09:33 +0000 (UTC)
X-SG-EID: P3IPuU2e1Ijn5xEegYUQ...
X-SendGrid-Contentd-ID: {"test_id":"1371661776"}"""  # noqa E501


def get_email_details(header: str) -> dict:
    """User re.search or re.match to capture the from, to, subject
       and date fields. Return the groupdict() of matching object, see:
       https://docs.python.org/3.7/library/re.html#re.Match.groupdict
       If not match, return None
    """
    # for line in header.splitlines():
    #     line = ' '.join(line.split())
    #     info = re.match(r'(?P<From>:\s\w+)(?P<To>\w+)(?P<Subject>:\s\w+)(?P<Date>:\s\w\d:,+)', line).groupdict()
    #     print(info)

    info = re.search(r'(?P<from>(?<=From: )[^\n]+).*(?P<to>(?<=To: )[^\n]+).*(?P<subject>(?<=Subject: )[^\n]+).*(?P<date>(?<=Date: )[\w\d\s,:]+[\d]{2})', header, re.DOTALL).groupdict()
    print(info)








print(get_email_details(EMAIL_HEADER))