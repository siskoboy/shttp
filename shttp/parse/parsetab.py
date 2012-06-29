
# shttp/parse/parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = 'b\x9cx\xb9\xe0\x01\xecN\xe3\xb2\x16\xf9~\xf2\xbe\x9f'
    
_lr_action_items = {'PROTO':([8,],[11,]),'URL':([3,],[8,]),'HVAL':([4,],[9,]),'HEADER':([1,6,9,11,],[4,4,-5,-2,]),'METHOD':([0,],[3,]),'$end':([1,2,5,6,7,9,10,11,],[-6,0,-1,-6,-4,-5,-3,-2,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'headers':([1,6,],[5,10,]),'reqstr':([0,],[1,]),'request':([0,],[2,]),'empty':([1,6,],[7,7,]),'aheader':([1,6,],[6,6,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> request","S'",1,None,None,None),
  ('request -> reqstr headers','request',2,'p_req','/Users/hansens/shttp/shttp/parse/parserdef.py',5),
  ('reqstr -> METHOD URL PROTO','reqstr',3,'p_reqstr','/Users/hansens/shttp/shttp/parse/parserdef.py',14),
  ('headers -> aheader headers','headers',2,'p_headers','/Users/hansens/shttp/shttp/parse/parserdef.py',18),
  ('headers -> empty','headers',1,'p_headers','/Users/hansens/shttp/shttp/parse/parserdef.py',19),
  ('aheader -> HEADER HVAL','aheader',2,'p_aheader','/Users/hansens/shttp/shttp/parse/parserdef.py',23),
  ('empty -> <empty>','empty',0,'p_empty','/Users/hansens/shttp/shttp/parse/parserdef.py',27),
]
