import streamlit as st


def render_turing_system(blockchain):
    st.header("Turing System")
    
    col1, col2 = st.columns(2)
    
    with col1:
        _render_state_evolution(blockchain)
    
    # with col2:
    #     _render_state_transition_function()


def _render_state_evolution(blockchain):
    st.write("**State Evolution:**")
    
    for i in range(len(blockchain.chain)):
        temp_chain = blockchain.chain[:i+1]
        state = _calculate_state(temp_chain)
        
        with st.expander(f"State at Block {i}", expanded=(i == len(blockchain.chain)-1)):
            if state:
                for acc, bal in sorted(state.items()):
                    st.write(f"**{acc}:** {bal:.2f} coins")
            else:
                st.write("*Genesis State*")


def _calculate_state(chain):
    state = {}
    for block in chain:
        for tx in block.transactions:
            state[tx.sender] = state.get(tx.sender, 1000.0) - tx.amount
            state[tx.receiver] = state.get(tx.receiver, 0.0) + tx.amount
    return state


# def _render_state_transition_function():
#     """Render explanation of state transition function."""
#     st.write("**State Transition Function:**")
#     st.code("""State[n+1] = f(State[n], Input[n])

# def state_transition(state, tx):
#     new_state = state.copy()
#     new_state[tx.sender] -= tx.amount
#     new_state[tx.receiver] += tx.amount
#     return new_state

# # Properties:
# # • Deterministic
# # • State-based computation
# # • Turing-complete
# """, language="python")


def render_summary(blockchain):
    st.divider()
    st.write("**Summary:**")
    
    is_valid, _ = blockchain.is_chain_valid()
    total_tx = sum(len(b.transactions) for b in blockchain.chain)
    
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.metric("Total Blocks", len(blockchain.chain))
    with c2:
        st.metric("Chain Status", "Valid ✅" if is_valid else "Invalid ❌")
    with c3:
        st.metric("Active Accounts", len(blockchain.get_state()))
    with c4:
        st.metric("Total Transactions", total_tx)