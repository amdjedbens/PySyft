# stdlib
# import gc

# third party
# import pytest
# import torch

# # syft absolute
# import syft as sy


# @pytest.mark.slow
# def test_same_var_for_ptr_gc() -> None:
#     """
#     Test for checking if the gc is correctly triggered
#     when the last reference to the ptr is overwritten
#     """
#     node = sy.VirtualMachine(name="alice")
#     client = node.get_client()

#     x = torch.tensor([1, 2, 3, 4])

#     for _ in range(100):
#         """
#         Override the ptr multiple times to make sure we trigger
#         the gc
#         """
#         ptr = x.send(client, pointable=False)

#     assert len(node.store) == 1

#     ptr.get()
# gc.collect()

# assert len(node.store) == 0


# def test_send_same_obj_gc() -> None:
#     """
#     Test if sending the same object multiple times, register the
#     object multiple times - because each send generated another
#     remote object
#     """
#     node = sy.VirtualMachine(name="alice")
#     root_client = node.get_root_client()

#     x = torch.tensor([1, 2, 3, 4])
#     ptr = []

#     for _ in range(100):
#         ptr.append(x.send(root_client, pointable=False))

# gc.collect()
# assert len(node.store) == 100

# del ptr

# gc.collect()
# assert len(node.store) == 0
