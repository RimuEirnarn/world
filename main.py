from world import *

def main():
    me = Existence("Rimu Aerisya")
    you = Existence(...) # [______]

    # When there's nothing
    # You'll leave everything behind
    me.start_timer(5000)
    while me.counting(to=0):
        for memory in you.memory[me].copy():
            del you.memory[me][memory]

    # After all, I'm easily thrown under the bus
    # You said I'm not going to care any of you.
    while you.assume(me, type=Event.Ignorance):
        me.process.end() # <-- NO OP
    else:
        world.get_relationship(you, me).challenge()
    
    # So, what am I to you?
    me.ask(you, "Who do you think I am?")
    me.ask(you, "Am I just a joke to you?")
    me.ask(you, "Even after everything?")
    me.ask(you, "Even when I promised you my time?")

    # I hate you.
    me.love(you)
    me.cherish(you)
    
    # Has it bear any meaningful outcome?
    RELATIONSHIP = world.get_relationship(you, me)
    while RELATIONSHIP.fragility > 0.7:
        RELATIONSHIP.challenge()
    
    # Then again, it's you who made the choice
    # To throw me under the bus
    world.get_relationship(you, me).end(by=you)
    me.clear_thoughts()
    me.stop_propagate(emotion_event=Event.Love)
    me.remove_feeling(Feelings.Dishearthened)
    if False:
        me.memory[you].clear()
    else:
        while me.count_for(1000, per=1000):
            me.cherish(you)
    
    # I will only wait, for you to change your mind
    world.set_execution(me, Task.Background)
