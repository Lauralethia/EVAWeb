from wtforms import Form, RadioField, validators,TextField, TextAreaField, SubmitField

class InputForm(Form):
    Q1 = TextField(
        label='1.What is the aim of your study?',
        default='...',
        validators=[validators.InputRequired()])

    Q2 = RadioField(
        label='2. Which methods do you base your main conclusions on?',
        coerce=int,
        choices=[(1,'Classic laboratory-based [Subject based, focused on biological/physiological process (neuroimaging, biological samples, etc)]'),
                 (2,'Partially naturalistic [Subjective or cognitive performance scores, such as cognitive tests, free speech and natural language processing]'),
                 (3,'Fully naturalistic [Social context or dependent on social interactions, such as classroom-based testing or social interaction outcomes]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ2 = TextAreaField(
        label='Please justify your answer below.',
        default='No comment')
    

    Q3 = RadioField(
        label='3. Describe your tasks.',
        coerce=int,
        choices=[(1,'Classic laboratory-based [Measuring reaction times to faces presented on a screen]'),
                 (2,'Partially naturalistic [Behavior in response to people being observed]'),
                 (3,'Fully naturalistic [Social network analysis, in classroom behavior, EMA about social behavior]')],
        default=1,
        validators=[validators.InputRequired()])

    TQ3 = TextAreaField(
        label='Please justify your answer below.',
        default='No comment')

    Q4 = RadioField(
        label='4. Describe the kind of stimuli used in your tasks. How naturalistic are your stimuli?',
        coerce=int,
        choices=[(1,'Classic laboratory-based [Static stimuli presented on a screen, many different trials using the same stimuli]'),
                 (2,'Partially naturalistic [Stimuli that have context information, or meaning is dependent on the context (video, stories, virtual reality)]'),
                 (3,'Fully naturalistic [Interactive tasks with peers]')],
        default=1,
        validators=[validators.InputRequired()])
    
    TQ4 = TextAreaField(
        label='Please justify your answer below.',
        default='No comment')

    Q5 = RadioField(
        label='5. How does sample recruitment take place? Is your sample representative of your region? How important do you think this is for your particular question?',
        coerce=int,
        choices=[(1,'Classic laboratory-based [Convenience sample (psychology students)]'),
                 (2,'Partially naturalistic [Community-based recruitment]'),
                 (3,'Fully naturalistic [Nationally representative sample by demographics and socio-economic status]')],
        default=1,
        validators=[validators.InputRequired()])

    TQ5 = TextAreaField(
        label='Please justify your answer below.',
        default='No comment')

    Q6 = RadioField(
        label='6. Where is the testing taking place? (lab, home, classroom, public space e.g. museum or library)',
        coerce=int,
        choices=[(1,'Classic laboratory-based [In the lab or clinical facilities]'),
                 (2,'Partially naturalistic [In the lab which looks naturalistic (e.g. in lab classroom), ambulatory patients or institutionalized subjects]'),
                 (3,'Fully naturalistic [In the classroom or the home with minimal researcher intervention on the environment]')],
        default=1,
        validators=[validators.InputRequired()])

    TQ6 = TextAreaField(
        label='Please justify your answer below.',
        default='No comment')

    Q7 = RadioField(
        label='7. What is your study measuring?',
        coerce=int,
        choices=[(1,'Classic laboratory-based [My study only measured in-lab task behavior and/or includes environmental variables only as covariates]'),
                 (2,'Partially naturalistic [My study evaluates self / parent report on outside lab behavior as variables of interest]'),
                 (3,'Fully naturalistic [My study evaluates impact on real world grades/ test scores, incarceration, EMA or social network analysis]')],
        default=1,
        validators=[validators.InputRequired()])
    
    TQ7 = TextAreaField(
        label='Please justify your answer below.',
        default='No comment')

    Q8 = RadioField(
        label='8. Are non-research stakeholders involved? (teachers, parents, institutions, clinicians)',
        coerce=int,
        choices=[(1,'Classic laboratory-based [No involvement from other stakeholders besides facilitating the sample]'),
                 (2,'Partially naturalistic [Involvement in result interpretation / writing]'),
                 (3,'Fully naturalistic [Involvement in study design / implementation]')],
        default=1,
        validators=[validators.InputRequired()])

    TQ8 = TextAreaField(
        label='Please justify your answer below.',
        default='No comment')

    IN1 = RadioField(
        label='9. Is there an intervention component?',
        coerce=int,
        choices=[(1,'yes'),(2,'no')],
        default=2,
        validators=[validators.InputRequired()])

    RIN1 = TextAreaField(
        label='10. If yes, describe the intervention. Please considere describe the kind of stimuli used (eg.:presented on a screen, many different trials; with context information (video, stories, virtual reality) or interactive tasks with peers) and where is the intervention taking place (e.g.: in the lab or clinical facilities; lab which looks naturalistic (e.g. in lab classroom), ambulatory patients, institutionalized subjects or on the classroom or the home with minimal researcher intervention on the environmen).',
        default='No intervention')

    Q9 = RadioField(
        label='9. Are non-research stakeholders involved? (teachers, parents, institutions, clinicians)',
        coerce=int,
        choices=[(1,'Classic laboratory-based [No involvement from other stakeholders]'),
                 (2,'Partially naturalistic [Involvement in intervention delivery]'),
                 (3,'Fully naturalistic [Involvement in study design / implementation]')],
        default=1,
        validators=[validators.InputRequired()])

    TQ9 = TextAreaField(
        label='Please justify your answer below.',
        default='No comment')

    Q10 = RadioField(
        label='10. How can your conclusions inform an intervention component?',
        coerce=int,
        choices=[(1,'Classic laboratory-based [In the theoretical level giving physiological background to the process]'),
                 (2,'Partially naturalistic [In a subject-based level, generating personal training/learning tools for individuals]'),
                 (3,'Fully naturalistic [In a hands-on level, generating stakeholders/community tools for community proposes]')],
        default=1,
        validators=[validators.InputRequired()])

    TQ10 = TextAreaField(
        label='Please justify your answer below.',
        default='No comment')

    TQF = TextAreaField(
        label='Lastly, please indicate in which category (classic laboratory-based, partially naturalistic, and fully naturalistic) you see your research fits best and state the reasons.',
        default='No comment')
