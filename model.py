from wtforms import Form, RadioField, validators,TextField, TextAreaField, SubmitField

class InputForm(Form):
    Q1 = TextField(
        label='1.What is the aim of your study?',
        default='...',
        validators=[validators.InputRequired()])

    Q2 = RadioField(
        label='2. In which methods do you base your main conclusions on?',
        coerce=int,
        choices=[(1,'Classic laboratory-based [Subject based, focused in biological/physiological process (neuroimaging, biological samples, etc)]'),
                 (2,'Partially naturalistic [Subjective or cognitive performance scores, such as cognitive tests, free speech and natural language processing]'),
                 (3,'Fully naturalistic [Social context or dependent on social interactions, such as classroom based testing or social interaction outcomes]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ2 = TextAreaField(
        label='If you like, you can justify your answer below',
        default='No comment')
    

    Q3 = RadioField(
        label='3. Describe your tasks',
        coerce=int,
        choices=[(1,'Classic laboratory-based [Independent of the subject intentions, such as measuring reaction time to stimuli, cortisol, MRI]'),
                 (2,'Partially naturalistic [Subject under individual interactions, such as measuring behavior in response to people being observed]'),
                 (3,'Fully naturalistic [Social network analysis, in classroom behavior, EMA about social behavior]')],
        default=1,
        validators=[validators.InputRequired()])

    TQ3 = TextAreaField(
        label='If you like, you can justify your answer below',
        default='No comment')

    Q4 = RadioField(
        label='4. Describe the kind of stimuli used in your tasks. ',
        coerce=int,
        choices=[(1,'Classic laboratory-based [Independent of the subject environment or designed to Evoque the “natural response” such as static faces]'),
                 (2,'Partially naturalistic [Stimuli that have context information, or meaning is dependent on the context (video, stories, virtual reality)]'),
                 (3,'Fully naturalistic [Interactive tasks with peers such as games]')],
        default=1,
        validators=[validators.InputRequired()])
    
    TQ4 = TextAreaField(
        label='If you like, you can justify your answer below',
        default='No comment')

    Q5 = RadioField(
        label='5. How natural are your stimuli (similar to daily life stimuli)?',
        coerce=int,
        choices=[(1,'Classic laboratory-based [Not much, such as many different trials using the same stimuli]'),
                 (2,'Partially naturalistic [In some way, even though they fall in the same categories of stimuli but unique stimuli]'),
                 (3,'Fully naturalistic [Completely natural, such as unique interaction between real people in real scenarios]')],
        default=1,
        validators=[validators.InputRequired()])

    TQ5 = TextAreaField(
        label='If you like, you can justify your answer below',
        default='No comment')

    Q6 = RadioField(
        label='6. To assess your aims, recruitment is essential.  How does sample recruitment take place? Is your sample representative of your region? Of the nation’s demographics?',
        coerce=int,
        choices=[(1,'Classic laboratory-based [Convenience sample (psych 101 students)]'),
                 (2,'Partially naturalistic [Community based recruitment]'),
                 (3,'Fully naturalistic [Nationally representative sample by demographics and SES]')],
        default=1,
        validators=[validators.InputRequired()])

    TQ6 = TextAreaField(
        label='If you like, you can justify your answer below',
        default='No comment')

    Q7 = RadioField(
        label='7. Where is the testing taking place? (lab, home, classroom, public space e.g. museum or library)',
        coerce=int,
        choices=[(1,'Classic laboratory-based [In the lab or clinical facilities]'),
                 (2,'Partially naturalistic [In the lab which looks naturalistic (e.g. in lab classroom), ambulatory patients or institutionalized subjects]'),
                 (3,'Fully naturalistic [In the classroom or the home with minimal researcher intervention on the environment]')],
        default=1,
        validators=[validators.InputRequired()])
    
    TQ7 = TextAreaField(
        label='If you like, you can justify your answer below',
        default='No comment')

    Q8 = RadioField(
        label='8. Is your study measuring some real-world outcomes? Such as (real world test scores / grades, risk taking behavior, self report about outside of the lab, EMA, social network analyses or are there environmental measurements being recorded? ',
        coerce=int,
        choices=[(1,'Classic laboratory-based [My study only measured in-lab task behavior and/or includes environmental variables only as covariates]'),
                 (2,'Partially naturalistic [My study evaluates self / parent report on outside lab behavior as variables of interest]'),
                 (3,'Fully naturalistic [My study evaluates impact on real world grades/ test scores, incarceration, EMA or social network analysis]')],
        default=1,
        validators=[validators.InputRequired()])

    TQ8 = TextAreaField(
        label='If you like, you can justify your answer below',
        default='No comment')

    Q9 = RadioField(
        label='9. Are non-research stakeholders involved? (teachers, parents, institutions, clinicians)',
        coerce=int,
        choices=[(1,'Classic laboratory-based [No involvement from other stakeholders besides facilitating the sample]'),
                 (2,'Partially naturalistic [Involvement in interpretation / writing]'),
                 (3,'Fully naturalistic [Involvement in design / implementation]')],
        default=1,
        validators=[validators.InputRequired()])

    TQ9 = TextAreaField(
        label='If you like, you can justify your answer below',
        default='No comment')

    Q10 = RadioField(
        label='10. How can your conclusions inform an intervention component?',
        coerce=int,
        choices=[(1,'Classic laboratory-based [In the theoretical level giving physiological background to the process]'),
                 (2,'Partially naturalistic [In a subject based level, generating personal training/learning tools for individuals]'),
                 (3,'Fully naturalistic [In a hands-on level, generating stakeholders/community tools for community proposes]')],
        default=1,
        validators=[validators.InputRequired()])

    TQ10 = TextAreaField(
        label='If you like, you can justify your answer below',
        default='No comment')

    TQF = TextAreaField(
        label='Finnaly, if you like to add any general comment',
        default='No comment')
