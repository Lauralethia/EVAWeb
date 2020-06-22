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
                 (3,'Naturalistic real-world [Dependent on social interactions or context, such as classroom-based testing or social interaction outcomes]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ2 = TextField(
        label='Please justify your answer below.',
        default='No comment')
    

#########################################################################################################################################################
        # TASK Q1
    Q4 = RadioField(
        label='3. Describe the kind of stimuli used in your tasks. How naturalistic are your stimuli?',
        coerce=int,
        choices=[(1,'Classic laboratory-based [Static stimuli presented on a screen, many different trials using the same stimuli]'),
                 (2,'Partially naturalistic [Dynamic stimuli that have context information, or meaning is dependent on the context (video, stories, virtual reality)]'),
                 (3,'Naturalistic real-world [Social interactions with peers]')],
        default=1,
        validators=[validators.InputRequired()])   
    TQ4 = TextField(
        label='Please justify your answer below.',
        default='No comment')

    Q3 = RadioField(
        label='4. Describe your experimental approach.',
        coerce=int,
        choices=[(1,'Classic laboratory-based [Measuring reaction times to faces presented on a screen]'),
                 (2,'Partially naturalistic [Peer presence during a lab task]'),
                 (3,'Naturalistic real-world [Social network analysis, in classroom behavior, EMA about social behavior]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ3 = TextField(
        label='Please justify your answer below.',
        default='No comment')

    Q5 = RadioField(
        label='5. Where is the testing taking place? (lab, home, classroom, public space e.g. museum or library)',
        coerce=int,
        choices=[(1,'Classic laboratory-based [In the lab or clinical facilities]'),
                 (2,'Partially naturalistic [In the lab which looks naturalistic (e.g. in lab classroom), ambulatory patients or institutionalized subjects]'),
                 (3,'Naturalistic real-world [In the classroom or the home with minimal researcher intervention on the environment]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ5 = TextField(
        label='Please justify your answer below.',
        default='No comment')

    Q6 = RadioField(
        label='6. What is your study measuring?',
        coerce=int,
        choices=[(1,'Classic laboratory-based [My study only measured in-lab task behavior and/or includes environmental variables only as covariates]'),
                 (2,'Partially naturalistic [My study evaluates self / parent report on outside lab behavior as variables of interest]'),
                 (3,'Naturalistic real-world [My study evaluates impact on real world grades/ test scores, incarceration, EMA or social network analysis]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ6 = TextField(
        label='Please justify your answer below.',
        default='No comment')
        
        # TASK Q2

          

    Q4b = RadioField(
        label='3.2 If you have a second task, describe the kind of stimuli used in your tasks. How naturalistic are your stimuli?',
        coerce=int,
        choices=[(1,'Classic laboratory-based [Static stimuli presented on a screen, many different trials using the same stimuli]'),
                 (2,'Partially naturalistic [Stimuli that have context information, or meaning is dependent on the context (video, stories, virtual reality)]'),
                 (3,'Naturalistic real-world [Interactive tasks with peers]'),
                 (4,'No second task')],

        default=4,
        validators=[validators.InputRequired()])   
    TQ4b = TextField(
        label='Please justify your answer below.',
        default='No comment')

    Q3b = RadioField(
        label='4.2 If you have a second task, describe your tasks.',
        coerce=int,
        choices=[(1,'Classic laboratory-based [Measuring reaction times to faces presented on a screen]'),
                 (2,'Partially naturalistic [Peer presence during a lab task]'),
                 (3,'Naturalistic real-world [Social network analysis, in classroom behavior, EMA about social behavior]'),
                 (4,'No second task')],
        default=4,
        validators=[validators.InputRequired()])
    TQ3b = TextField(
        label='Please justify your answer below.',
        default='No comment')


    Q5b = RadioField(
        label='5.2 If you have a second task, where is the testing taking place?',
        coerce=int,
        choices=[(1,'Classic laboratory-based [In the lab or clinical facilities]'),
                 (2,'Partially naturalistic [In the lab which looks naturalistic (e.g. in lab classroom), ambulatory patients or institutionalized subjects]'),
                 (3,'Naturalistic real-world [In the classroom or the home with minimal researcher intervention on the environment]'),
                 (4,'No second task')],

        default=4,
        validators=[validators.InputRequired()])
    TQ5b = TextField(
        label='Please justify your answer below.',
        default='No comment')

    Q6b = RadioField(
        label='6.2 If you have a second task, what is it measuring?',
        coerce=int,
        choices=[(1,'Classic laboratory-based [My study only measured in-lab task behavior and/or includes environmental variables only as covariates]'),
                 (2,'Partially naturalistic [My study evaluates self / parent report on outside lab behavior as variables of interest]'),
                 (3,'Naturalistic real-world [My study evaluates impact on real world grades/ test scores, incarceration, EMA or social network analysis]'),
                 (4,'No second task')],
        default=4,
        validators=[validators.InputRequired()])
    TQ6b = TextField(
        label='Please justify your answer below.',
        default='No comment')

        # TASK Q3
           

    Q4c = RadioField(
        label='3.3 If you have a second task, describe the kind of stimuli used in your tasks. How naturalistic are your stimuli?',
        coerce=int,
        choices=[(1,'Classic laboratory-based [Static stimuli presented on a screen, many different trials using the same stimuli]'),
                 (2,'Partially naturalistic [Stimuli that have context information, or meaning is dependent on the context (video, stories, virtual reality)]'),
                 (3,'Naturalistic real-world [Interactive tasks with peers]'),
                 (4,'No third task')],

        default=4,
        validators=[validators.InputRequired()])   

    Q3c = RadioField(
        label='4.3 If you have a third task, describe your tasks.',
        coerce=int,
        choices=[(1,'Classic laboratory-based [Measuring reaction times to faces presented on a screen]'),
                 (2,'Partially naturalistic [Peer presence during a lab task]'),
                 (3,'Naturalistic real-world [Social network analysis, in classroom behavior, EMA about social behavior]'),
                 (4,'No third task')],
        default=4,
        validators=[validators.InputRequired()])
    TQ3c = TextField(
        label='Please justify your answer below.',
        default='No comment')

    TQ4c = TextField(
        label='Please justify your answer below.',
        default='No comment')

    Q5c = RadioField(
        label='5.2 If you have a third task, where is the testing taking place?',
        coerce=int,
        choices=[(1,'Classic laboratory-based [In the lab or clinical facilities]'),
                 (2,'Partially naturalistic [In the lab which looks naturalistic (e.g. in lab classroom), ambulatory patients or institutionalized subjects]'),
                 (3,'Naturalistic real-world [In the classroom or the home with minimal researcher intervention on the environment]'),
                 (4,'No third task')],

        default=4,
        validators=[validators.InputRequired()])
    TQ5c = TextField(
        label='Please justify your answer below.',
        default='No comment')

    Q6c = RadioField(
        label='6.3 If you have a third task, what is it measuring?',
        coerce=int,
        choices=[(1,'Classic laboratory-based [My study only measured in-lab task behavior and/or includes environmental variables only as covariates]'),
                 (2,'Partially naturalistic [My study evaluates self / parent report on outside lab behavior as variables of interest]'),
                 (3,'Naturalistic real-world [My study evaluates impact on real world grades/ test scores, incarceration, EMA or social network analysis]'),
                 (4,'No third task')],
        default=4,
        validators=[validators.InputRequired()])
    TQ6c = TextField(
        label='Please justify your answer below.',
        default='No comment')
#########################################################################################################################################################################

    Q7 = RadioField(
        label='7. How does sample recruitment take place? Is your sample representative of your region? How important do you think this is for your particular question?',
        coerce=int,
        choices=[(1,'Classic laboratory-based [Convenience sample (e.g., students)]'),
                 (2,'Partially naturalistic [Community-based recruitment]'),
                 (3,'Naturalistic real-world [Nationally representative sample by demographics and socio-economic status]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ7 = TextField(
        label='Please justify your answer below.',
        default='No comment')

    Q8 = RadioField(
        label='8. Are non-research stakeholders involved? (teachers, parents, institutions, clinicians)',
        coerce=int,
        choices=[(1,'Classic laboratory-based [No involvement from other stakeholders besides facilitating the sample]'),
                 (2,'Partially naturalistic [Involvement in result interpretation / writing]'),
                 (3,'Naturalistic real-world [Involvement in study design / implementation]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ8 = TextField(
        label='Please justify your answer below.',
        default='No comment')

    IN1 = RadioField(
        label='9. Is there an intervention component?',
        coerce=int,
        choices=[(11,'yes'),(22,'no')],
        default=22,
        validators=[validators.InputRequired()])
    RIN1 = TextAreaField(
        label='10. If R9 is yes. Describe the intervention. (What kind of stimuli are you using for the intervention? How naturalistic are your stimuli? Where is the intervention taking place? Are non-research stakeholders involved?)',
        default='No intervention')

    Q11 = RadioField(
        label='11. If R9 is yes, please indicate where your intervention fits in best. ',
        coerce=int,
        choices=[(1,'Classic laboratory-based [***]'),
                 (2,'Partially naturalistic [***]'),
                 (3,'Naturalistic real-world [***]'),
                 (4,'No intervention component')],
        default=4,
        validators=[validators.InputRequired()])
    TQ11 = TextField(
        label='Please justify your answer below.',
        default='No comment')

    
    TQF = TextAreaField(
        label='12. Lastly, please indicate in which category (classic laboratory-based, partially naturalistic, and fully naturalistic) you see your research fits best and state the reasons.',
        default='No comment')
