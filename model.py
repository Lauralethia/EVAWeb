from wtforms import Form, RadioField, validators,TextField, TextAreaField, SubmitField

class InputForm(Form):
    Q1 = TextField(
        label='1.What is the aim of your study? What situation/context do you intend to generalize the results to (e.g. Is your sample representative of your region)?',
        default='...',
        validators=[validators.InputRequired()])

    Q2 = RadioField(
        label='2. Which methods do you base your main conclusions on?',
        coerce=int,
        choices=[(1,'CLR [Subject based, focused on biological/physiological process (neuroimaging, biological samples, etc)]'),
                 (2,'PNLRA [Subjective or cognitive performance scores, such as cognitive tests, free speech and natural language processing]'),
                 (3,'NRWRA [Dependent on social interactions or context, such as classroom-based testing or social interaction outcomes]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ2 = TextField(
        label='Please justify your answer below.',
        default='No comment')
    

#########################################################################################################################################################
        # TASK Q1
    Q4 = RadioField(
        label='3. Describe the kind of stimuli used in your tasks.',
        coerce=int,
        choices=[(1,'CLR [Static stimuli, typical for perceptual/cognitive studies, like face images]'),
                 (2,'PNLRA [Dynamic stimuli, like dynamic faces on video]'),
                 (3,'NRWRA [Fully naturalistically sampled stimuli in the real world, like persons during a social interaction]')],
        default=1,
        validators=[validators.InputRequired()])   
    TQ4 = TextField(
        label='Please justify your answer below.',
        default='No comment')

    Q3 = RadioField(
        label='4. Describe your experimental approach.',
        coerce=int,
        choices=[(1,'CLR [Working memory task for shapes presented on a screen]'),
                 (2,'PNLRA [Test of memory after viewing a movie]'),
                 (3,'NRWRA [Test of memory of an interaction after a prolonged delay that involved other activities]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ3 = TextField(
        label='Please justify your answer below.',
        default='No comment')

    Q5 = RadioField(
        label='5. Where is the testing taking place? (lab, home, classroom, public space e.g. museum or library)',
        coerce=int,
        choices=[(1,'CLR [Lab or clinical testing room]'),
                 (2,'PNLRA [Lab set up to look like a classroom]'),
                 (3,'NRWRA [School classroom with little/no experimenter presence and interference into teaching activities')],
        default=1,
        validators=[validators.InputRequired()])
    TQ5 = TextField(
        label='Please justify your answer below.',
        default='No comment')

    Q6 = RadioField(
        label='6. What are your measures?',
        coerce=int,
        choices=[(1,'CLR [Well-understood, well-researched brain correlates of a specific cognitive process, such as the Event-Related Potential (ERP) components P1 or N2 (or a cognitive contrast in fMRI), tested in typical conditions]'),
                 (2,'PNLRA [Testing the canonical brain correlates in non-traditional laboratory settings and/or using more portable brain imaging tools, like EEG or fNIRS]'),
                 (3,'NRWRA [Using portable brain imaging tools in veridical external environments to test for canonical brain EEG/ERP ‘correlates’ of cognitive processes or for spectral features as correlates of mental states (engagement)]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ6 = TextField(
        label='Please justify your answer below.',
        default='No comment')
        
        # TASK Q2

          

    Q4b = RadioField(
        label='3.2 If you have a second task, describe the kind of stimuli used in your tasks. How naturalistic are your stimuli?',
        coerce=int,
        choices=[(1,'CLR [Static stimuli presented on a screen, many different trials using the same stimuli]'),
                 (2,'PNLRA [Dynamic stimuli that have context information, or meaning is dependent on the context (video, stories, etc)]'),
                 (3,'NRWRA [Interactive tasks with peers]'),
                 (4,'No second task')],

        default=4,
        validators=[validators.InputRequired()])   
    TQ4b = TextField(
        label='Please justify your answer below.',
        default='No comment')

    Q3b = RadioField(
        label='4.2 If you have a second task, describe your tasks.',
        coerce=int,
        choices=[(1,'CLR [Measuring reaction times to faces presented on a screen]'),
                 (2,'PNLRA [Peer presence during a lab task]'),
                 (3,'NRWRA [Social network analysis, in classroom behavior, EMA about social behavior]'),
                 (4,'No second task')],
        default=4,
        validators=[validators.InputRequired()])
    TQ3b = TextField(
        label='Please justify your answer below.',
        default='No comment')


    Q5b = RadioField(
        label='5.2 If you have a second task, where is the testing taking place?',
        coerce=int,
        choices=[(1,'CLR [In the lab or clinical facilities]'),
                 (2,'PNLRA [In the lab which looks naturalistic (e.g. in lab classroom), ambulatory patients or institutionalized subjects]'),
                 (3,'NRWRA [In the classroom or the home with minimal researcher intervention on the environment]'),
                 (4,'No second task')],

        default=4,
        validators=[validators.InputRequired()])
    TQ5b = TextField(
        label='Please justify your answer below.',
        default='No comment')

    Q6b = RadioField(
        label='6.2 If you have a second task, what is it measuring?',
        coerce=int,
        choices=[(1,'CLR [My study only measured in-lab task behavior and/or includes environmental variables only as covariates]'),
                 (2,'PNLRA [My study evaluates self / parent report on outside lab behavior as variables of interest]'),
                 (3,'NRWRA [My study evaluates impact on real world grades/ test scores, incarceration, EMA or social network analysis]'),
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
        choices=[(1,'CLR [Static stimuli presented on a screen, many different trials using the same stimuli]'),
                 (2,'PNLRA [Dynamic stimuli that have context information, or meaning is dependent on the context (video, stories, etc)]'),
                 (3,'NRWRA [Interactive tasks with peers]'),
                 (4,'No third task')],

        default=4,
        validators=[validators.InputRequired()])   

    Q3c = RadioField(
        label='4.3 If you have a third task, describe your tasks.',
        coerce=int,
        choices=[(1,'CLR [Measuring reaction times to faces presented on a screen]'),
                 (2,'NLRA [Peer presence during a lab task]'),
                 (3,'NRWRA [Social network analysis, in classroom behavior, EMA about social behavior]'),
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
        choices=[(1,'CLR [In the lab or clinical facilities]'),
                 (2,'PNLRA [In the lab which looks naturalistic (e.g. in lab classroom), ambulatory patients or institutionalized subjects]'),
                 (3,'NRWRA [In the classroom or the home with minimal researcher intervention on the environment]'),
                 (4,'No third task')],

        default=4,
        validators=[validators.InputRequired()])
    TQ5c = TextField(
        label='Please justify your answer below.',
        default='No comment')

    Q6c = RadioField(
        label='6.3 If you have a third task, what is it measuring?',
        coerce=int,
        choices=[(1,'CLR [My study only measured in-lab task behavior and/or includes environmental variables only as covariates]'),
                 (2,'PNLRA [My study evaluates self / parent report on outside lab behavior as variables of interest]'),
                 (3,'NRWRA [My study evaluates impact on real world grades/ test scores, incarceration, EMA or social network analysis]'),
                 (4,'No third task')],
        default=4,
        validators=[validators.InputRequired()])
    TQ6c = TextField(
        label='Please justify your answer below.',
        default='No comment')
#########################################################################################################################################################################

    Q7 = RadioField(
        label='7. How important your recruitment approach is for generalizing from your results? When answering this question, consider how you recruit participants for your study, and whether your sample is representative of, e.g., your region.',
        coerce=int,
        choices=[(1,'CLR [Convenience sample, such as undergraduate students at a university]'),
                 (2,'PNLRA [Community-based recruitment]'),
                 (3,'NRWRA [A large, nationally representative sample of school districts in a city]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ7 = TextField(
        label='Please justify your answer below.',
        default='No comment')

    Q8 = RadioField(
        label='8. Are non-research stakeholders involved? (teachers, parents, institutions, clinicians)',
        coerce=int,
        choices=[(1,'CLR [Stakeholders only facilitate access to the sample]'),
                 (2,'PNLRA [Stakeholders involved in conception OR interpretation/writing up the results]'),
                 (3,'NRWRA [Involvement in conception of project AND interpretation/writing up the results]')],
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
        choices=[(1,'CLR [Children play a game on a laptop/ tablet at the lab/ clinic supervised by experimenters and/or parents]'),
                 (2,'PNLRA [Children play a game on a laptop/ tablet at home supervised by parents]'),
                 (3,'NRWRA [Children play an online application at home by themselves when they feel like it]'),
                 (4,'No intervention component')],
        default=4,
        validators=[validators.InputRequired()])
    TQ11 = TextField(
        label='Please justify your answer below.',
        default='No comment')

    
    TQF = TextAreaField(
        label='12. Lastly, please indicate in which category (CLR, PNLRA, and NRWRA) you see your research fits best and state the reasons.',
        default='No comment')
