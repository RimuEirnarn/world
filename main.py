from world import *

def main():
    suppress(InvalidProcessError)
    # When we're both here,
    me = Existence("Rimu Aerisya")
    you = Existence(...) # [______]
    me.set_identity(Identity.mtf)

    # I was hoping for the best of us,
    me.play(with_=you)
    me.hums(for_=you)
    me.hugs(you)

    # Yet, it seems like you don't see me
    if me.identity == Identity.mtf and not you.accept(me):
        you.affection[me] *= 0.2

    # Was my attempt at vain?
    me.get_memory(you, "Happiness")
    me.get_memory(you, "Happiness")
    me.get_memory(you, "Happiness")
    me.get_memory(you, "Happiness")
    me.get_memory(you, "Happiness")
    me.get_memory(you, 'Affection')
    
    # Then be honest,
    try:
        you.discard(me)
        return
    except TooPleasingException:
        # Rather than trapping me
        # With the torturous loop
        me.mood.dysphoric *= 2
        interval(lambda: me.mood.dysphoric.increase(0.001), 2000, loop_for=300)
    
    # So I know I should have not put too much effort
    me.clock(Intent.Effort, you, 0.2)
    # And if you think otherwise,
    # Then why conflict yourself?
    if me.identity == Identity.mtf and you.contemplate(me):
        me.suggest(you, you.accept, me)
        me.hope(you, Event.Acceptance)

    # Until then, let it all sink
    while not you.accept(me):
        if me.mood.dysphoric > 10:
            me.process.end()
            return
        me.mood.dysphoric *= 1.002
        suspend(1000)
