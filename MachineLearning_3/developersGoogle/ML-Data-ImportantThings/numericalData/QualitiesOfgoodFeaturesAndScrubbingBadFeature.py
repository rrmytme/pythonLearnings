'''
Qualities of good numerical features:
1. Clearly named, ex: house_age_years: 27
2. Checked or tested before training ex: feature should be user_age_in_years: 24 instead of user_age_in_years: 224
3. Sensible: A "magic value" is a purposeful discontinuity in an otherwise continuous feature. 
For example, suppose a continuous feature named watch_time_in_seconds can hold any floating-point 
value between 0 and 30 but represents the absence of a measurement with the magic value -1 should be avoided
instead it should be,
watch_time_in_seconds: 4.82
is_watch_time_in_seconds_defined=True


watch_time_in_seconds: 0
is_watch_time_in_seconds_defined=False

Scrubbing is a process of find following problems and fix/remove from te dataset 

Problem category	Example
Omitted values	A census taker fails to record a resident's age.
Duplicate examples	A server uploads the same logs twice.
Out-of-range feature values.	A human accidentally types an extra digit.
Bad labels	A human evaluator mislabels a picture of an oak tree as a maple.
'''